import argparse
import logging
import sys
import textwrap
from vending_machine.vending_machine import VendingMachine

# TODO: add documentation readme /requirements. python3.6+


LOG_FORMAT = '%(message)s'


def display_menu(vending_machine):
    mylist = []
    operation = input('''Select operation:
    [1] List Available Snacks
    [2] Select a Snack
    [3] Insert a Coin
    [4] Show Total Collected Money
    [5] Show Selected Snack
    [6] Cancel Transaction
    [7] Show Machine State Information
>> ''')

    if operation == '1':
        logging.info("list of available snacks: ")
        vending_machine.display_stock()

    elif operation == '2':
        snack_code = input('Please enter snack code\n>> ')
        vending_machine.select_item(snack_code)

    elif operation == '3':
        allowed_coins = vending_machine.get_allowed_coins()
        logging.info(f"Insert a coin from the following coins list: [{'$, '.join(map(str, allowed_coins))}]")
        amount = input('\n>> ')
        vending_machine.collect_cash(amount)

    elif operation == '4':
        logging.info(f"Total collected cash: {vending_machine.get_collected_cash()}$")

    elif operation == '5':
        selected_item = vending_machine.get_selected_item()
        if selected_item:
            logging.info(f"Selected item: '{selected_item['name']}' with price of ({selected_item['price']}$)")
        else:
            logging.info("No item has been selected, please select item first")

    elif operation == '6':
        vending_machine.cancel_transaction()

    elif operation == '7':
        logging.info(f"VM currently in {type(vending_machine.get_state()).__name__} state")

    else:
        logging.info('You have not chosen a valid option, please try again.')

    again(vending_machine)


def again(vending_machine):
    list_again = input('\nWould you like to see main menu again? (Y/N) ')

    if list_again.upper() == 'Y':
        display_menu(vending_machine)
    elif list_again.upper() == 'N':
        logging.info('OK. Bye bye. :)')
    else:
        again(vending_machine)


def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=LOG_FORMAT)

    vending_machine = VendingMachine()
    display_menu(vending_machine)
    # TODO: documentation




if __name__ == '__main__':
    main()
