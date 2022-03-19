from analysis import *
from plot import *

# ----------------------------------------------- #


in_app: bool = True

print("\nWelcome to the compound tool. This tool will help you to determine the frequencies in which you need to "
      "recompound your stacking rewards.\n")

while in_app:

    print("\nWhat action do you want to perform ?\n"
          "  1.  Know what is the best basic stacking period\n"
          "  2.  Know what is the best optimized stacking period\n"
          "  3.  Display the chart of different strategies\n"
          "  4.  Display the chart of the optimized stately\n"
          "  5.  Display the chart of all the strategies\n"
          "  6.  Display the chart of the compounding period as a function of stacked asset\n\n"
          )

    try:

        user_choice = positive_int_input("Type 1, 2, 3, 4, 5 or 6 according to the feature you want to use : ")

        if user_choice == 1:
            period = positive_int_input("\nHow many days do you plan to stake ?  -->  ")
            stacked_value = positive_float_input("How much asset do you stake ?  -->  ")

            print(f"\n  -->  The best basic choice is to compound rewards every "
                  f"{best_basic_compound_period(period=period,staked_value=stacked_value)}"
                  " day(s)."
                  )

        elif user_choice == 2:
            period = positive_int_input("\nHow many days do you plan to stake ?  -->  ")
            stacked_value = positive_float_input("How much asset do you stake ?  -->  ")

            best_optimized_staking_period(period=period,
                                          staked_value=stacked_value
                                          )

        elif user_choice == 3:
            period = positive_int_input("\nHow many days do you plan to stake ?  -->  ")
            stacked_value = positive_float_input("How much asset do you stake ?  -->  ")
            min_day: int = positive_int_input("From how many day(s) are you ready to compound ?  -->  ")
            max_day: int = positive_int_input("To how many day(s) are you ready to compound ?  -->  ")

            display_basic_strategies(number_of_days=period,
                                     staked_value=stacked_value,
                                     min_compound_day=min_day,
                                     max_compound_day=max_day
                                     )

        elif user_choice == 4:
            period = positive_int_input("\nHow many days do you plan to stake ?  -->  ")
            stacked_value = positive_float_input("How much asset do you stake ?  -->  ")

            display_optimized_strategy(number_of_days=period,
                                       staked_value=stacked_value
                                       )

        elif user_choice == 5:
            period = positive_int_input("\nHow many days do you plan to stake ?  -->  ")
            stacked_value = positive_float_input("How much asset do you stake ?  -->  ")
            min_day: int = positive_int_input("From how many day(s) are you ready to compound ?  -->  ")
            max_day: int = positive_int_input("To how many day(s) are you ready to compound ?  -->  ")

            display_all_strategies(number_of_days=period,
                                   staked_value=stacked_value,
                                   min_compound_day=min_day,
                                   max_compound_day=max_day
                                   )

        elif user_choice == 6:
            period = positive_int_input("\nHow many days do you plan to stake ?  -->  ")
            min_day: int = positive_float_input("From how much asset value do you want to analyze ?  -->  ")
            max_day: int = positive_float_input("To how much asset value do you want to analyze ?  -->  ")

            display_parametric_chart(min_asset_value=min_day,
                                     max_asset_value=max_day,
                                     number_of_days=period
                                     )

        else:
            raise ValueError

        user_choice = input("\nDo you want to perform another action ? (y/n)  -->  ")

        if user_choice.lower() == 'y':
            in_app = True

        else:
            in_app = False

    except(ValueError, TypeError):
        print("\nThe parameter you typed is wrong ! Please try again.")
