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


    # TODO: add CLI


if __name__ == '__main__':
    main()
