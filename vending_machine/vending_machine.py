from __future__ import annotations
from abc import ABC, abstractmethod
from vending_machine.idle import Idle
from vending_machine.display_stock import DisplayStock
from vending_machine.select_item import SelectItem
from vending_machine.collect_cash import CollectCash
from vending_machine.dispense_item import DispenseItem
from vending_machine.dispense_change import DispenseChange
from vending_machine.cancel_transaction import CancelTransaction

class VendingMachine():

    def __init__(self) -> None:
        self.collected_cash = 0
        self.selected_item = None
        self.current_state = None
        self.stocks = { 1: {'item': 'coke', 'price': 6},
                        2: {'item': 'sprite', 'price': 7},
                        3: {'item': 'ice_lemon_tea', 'price': 12},
                        4: {'item': 'fanta_grape', 'price': 16},
                        }
        self.allowed_coins = [1,2,5,10,20,50]

        self.idle = Idle()
        self.displayStock = DisplayStock()
        self.selectItem = SelectItem()
        self.collectCash = CollectCash()
        self.dispenseItem = DispenseItem()
        self.dispenseChange = DispenseChange()
        self.cancelTransaction = CancelTransaction()

        self.set_state(self.idle)

    def get_state(self):
        print(f"VM is in {type(self.current_state).__name__}")

    def set_state(self, state):
        print(f"{type(self.current_state).__name__} -> {type(state).__name__}")
        self.current_state = state
        self.current_state.vending_machine = self

    def get_collected_cash(self):
        print(f"Total collected cash: {self.collected_cash}")

    def get_selected_item(self):
        print(f"Selected item: {self.selected_item}")


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


