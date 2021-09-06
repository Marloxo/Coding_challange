import argparse
import logging
import sys
import textwrap
from vending_machine.vending_machine import VendingMachine

# TODO: add documentation readme /requirements. python3.6+


def main():
    vending_machine = VendingMachine()
    vending_machine.get_state()
    vending_machine.display_stock()
    vending_machine.get_state()
    vending_machine.select_item(1)
    vending_machine.collect_cash(2)

    vending_machine.cancel_transaction()

    vending_machine.get_collected_cash()
    vending_machine.get_selected_item()

    # TODO: add CLI

    # TODO: UI options
    # 1- list stocks
    # 2- select items
    # 3- insert coins
    # 4- show total collected_cash
    # 5- show selected_item


if __name__ == '__main__':
    main()
