import matplotlib.pyplot as plt
from analysis import (dynamic_compound_rewards,
                      dynamic_compound_period,
                      stake_every_k_day
                      )

from typing import Dict


# ----------------------------------------------- #


def display_optimized_strategy(number_of_days: int,
                               staked_value: int
                               ) -> None:
    intelligent_compounding = dynamic_compound_rewards(initial_stacked_value=staked_value,
                                                       period=number_of_days
                                                       )

    plt.plot(intelligent_compounding[0],
             intelligent_compounding[1]
             )
    plt.xlabel("Day number")
    plt.ylabel("Stacking rewards")
    plt.grid(visible=True)
    plt.show()


# ----------------------------------------------- #


def display_basic_strategies(number_of_days: int,
                             staked_value: int,
                             min_compound_day: int,
                             max_compound_day: int
                             ) -> None:

    result_dict: Dict[str, float] = {}

    for day in range(min_compound_day, max_compound_day+1, 1):
        current_strat = stake_every_k_day(period=number_of_days,
                                          day_step=day,
                                          staked_value=staked_value
                                          )
        result_dict[f"Every {day} day(s)"] = current_strat[1][-1]
        plt.plot(current_strat[0], current_strat[1], label=f"Staking every {day} day(s)")

    print(f"\n  -->  The best choice is to compound rewards {max(result_dict, key=result_dict.get).lower()}.")

    plt.xlabel("Day number")
    plt.ylabel("Stacking rewards")
    plt.grid(visible=True)
    plt.legend()
    plt.show()


# ----------------------------------------------- #


def display_all_strategies(number_of_days: int,
                           staked_value: int,
                           min_compound_day: int,
                           max_compound_day: int
                           ) -> None:

    for day in range(min_compound_day, max_compound_day + 1, 1):
        current_strat = stake_every_k_day(period=number_of_days,
                                          day_step=day,
                                          staked_value=staked_value
                                          )

        plt.plot(current_strat[0],
                 current_strat[1],
                 label=f"Every {day} day(s)"
                 )

    intelligent_compounding = dynamic_compound_rewards(initial_stacked_value=staked_value,
                                                       period=number_of_days
                                                       )

    plt.plot(intelligent_compounding[0],
             intelligent_compounding[1],
             label="Dynamic compounding"
             )

    plt.xlabel("Day number")
    plt.ylabel("Stacking rewards")
    plt.grid(visible=True)
    plt.legend()
    plt.show()


# ----------------------------------------------- #


def display_parametric_chart(number_of_days: int,
                             max_asset_value: float,
                             min_asset_value: float
                             ) -> None:

    results = dynamic_compound_period(min_asset_value=min_asset_value,
                                      max_asset_value=max_asset_value,
                                      period=number_of_days
                                      )

    plt.plot(results[0],
             results[1]
             )

    plt.xlabel("Stacked value")
    plt.ylabel("Recommended compounding period")
    plt.grid(visible=True)
    plt.show()
