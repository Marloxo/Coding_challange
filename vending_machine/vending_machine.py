from __future__ import annotations
from vending_machine.idle import Idle
from vending_machine.display_stock import DisplayStock
from vending_machine.select_item import SelectItem
from vending_machine.collect_cash import CollectCash
from vending_machine.dispense_item import DispenseItem
from vending_machine.dispense_change import DispenseChange
from vending_machine.cancel_transaction import CancelTransaction
import logging


class VendingMachine():

    def __init__(self) -> None:
        self.collected_cash = 0
        self.selected_item = None
        self.current_state = None
        self.stocks = {
            1: {'name': 'Coke', 'price': 6},
            2: {'name': 'Sprite', 'price': 7},
            3: {'name': 'Ice Lemon Tea', 'price': 12},
            4: {'name': 'Fanta Grape', 'price': 16},
        }
        self.allowed_coins = [1, 2, 5, 10, 20, 50]

        self.idle = Idle()
        self.displayStock = DisplayStock()
        self.selectItem = SelectItem()
        self.collectCash = CollectCash()
        self.dispenseItem = DispenseItem()
        self.dispenseChange = DispenseChange()
        self.cancelTransaction = CancelTransaction()

        self.set_state(self.idle)

    def get_allowed_coins(self):
        return self.allowed_coins

    def get_collected_cash(self):
        return self.collected_cash

    def get_selected_item(self):
        return self.selected_item

    def get_state(self):
        return self.current_state

    def set_state(self, state):
        logging.debug(f'{type(self.current_state).__name__} -> {type(state).__name__}')
        self.current_state = state
        self.current_state.vending_machine = self

    def display_stock(self):
        self.current_state.display_stock()

    def select_item(self, product_code):
        self.current_state.select_item(product_code)

    def collect_cash(self, amount):
        self.current_state.collect_cash(amount)

    def cancel_transaction(self):
        self.current_state.cancel_transaction()

    def dispense_item(self):
        self.current_state.dispense_item()

    def dispense_change(self):
        self.current_state.dispense_change()
