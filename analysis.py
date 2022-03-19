from config import Config
from typing import List, Dict, Tuple

from numpy import linspace


# ----------------------------------------------- #


def new_rewards(previous_rewards,
                staked_value: float,
                day_step: int,
                apr: float
                ) -> float:

    return ((staked_value + previous_rewards) * day_step * apr / 365
            - Config.staking_fees / Config.USD_over_asset
            + previous_rewards
            )


# ----------------------------------------------- #


def stake_every_k_day(period: int,
                      staked_value: float,
                      day_step: int = 1
                      ) -> Tuple[List[int], List[float]]:

    days_list: List[int] = [i for i in range(1, period, day_step)]

    if days_list[-1] != period:
        days_list.append(period)

    rewards: List[float] = [- Config.staking_fees / Config.USD_over_asset]

    for day in days_list[:-2]:
        rewards.append(new_rewards(previous_rewards=rewards[-1],
                                   staked_value=staked_value,
                                   day_step=day_step,
                                   apr=Config.APR
                                   )
                       )

    buffer = days_list[-1] - days_list[-2]
    rewards.append(new_rewards(previous_rewards=rewards[-1],
                               staked_value=staked_value,
                               day_step=buffer,
                               apr=Config.APR
                               )
                   )

    return days_list, rewards


# ----------------------------------------------- #


def best_basic_compound_period(period: int,
                               staked_value: float
                               ) -> int:

    result_dict: Dict[str, float] = {}

    for day_step in range(1, period - 1, 1):
        splitted_staking = stake_every_k_day(period=period,
                                             day_step=day_step,
                                             staked_value=staked_value
                                             )
        result_dict[f"{day_step}"] = splitted_staking[1][-1]

    try:
        return int(max(result_dict, key=result_dict.get))

    except:
        return 1


# ----------------------------------------------- #


def best_optimized_staking_period(period: int,
                                  staked_value: float
                                  ) -> None:

    dynamic_compound_rewards(period=period,
                             initial_stacked_value=staked_value
                             )


# ----------------------------------------------- #


def dynamic_compound_period(min_asset_value: float,
                            max_asset_value: float,
                            period: int,
                            step: float = 0.01
                            ) -> Tuple[List[float], List[float]]:

    asset_values = linspace(min_asset_value,
                            max_asset_value,
                            num=int((max_asset_value - min_asset_value) / step)
                            )
    period_values: List[float] = []

    for asset_value in asset_values:
        period_values.append(best_basic_compound_period(period,
                                                        staked_value=asset_value
                                                        )
                             )

    return asset_values, period_values


# ----------------------------------------------- #


def dynamic_compound_rewards(initial_stacked_value: float,
                             period: int
                             ) -> Tuple[List[int], List[float]]:
    dynamic_rewards: List[float] = [- Config.staking_fees / Config.USD_over_asset]
    days_list: List[int] = [0]

    current_period: int = best_basic_compound_period(period=period,
                                                     staked_value=initial_stacked_value
                                                     )
    print(f"\nAt the beginning, compound every {current_period} day(s)\n")

    current_day: int = 0
    rewards: float = 0

    while current_day < period:

        refreshed_period: int = best_basic_compound_period(period=period - current_day,
                                                           staked_value=initial_stacked_value + rewards
                                                           )

        if current_period != refreshed_period:
            print(
                f"Change in the period of compounding on the {current_day}th day : compound every {refreshed_period} day(s)")
            print(f"   ---> Balance at this time : {initial_stacked_value + rewards}\n")
            current_period = refreshed_period

        rewards = new_rewards(previous_rewards=rewards,
                              staked_value=initial_stacked_value,
                              day_step=current_period,
                              apr=Config.APR
                              )

        current_day += current_period

        dynamic_rewards.append(rewards)
        days_list.append(current_day)

    return days_list, dynamic_rewards


# ----------------------------------------------- #


def positive_int_input(text) -> int:

    value = int(input(text))

    if value < 0 or type(value) != int:
        raise ValueError

    return value


# ----------------------------------------------- #


def positive_float_input(text) -> float:

    value = float(input(text))

    if value < 0 or type(value) != float:
        raise ValueError

    return value
