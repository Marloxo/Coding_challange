from __future__ import annotations
from vending_machine.state import State
import logging
class Idle(State):

    def display_stock(self) -> None:
        self.vending_machine.set_state(self.vending_machine.displayStock)
        self.vending_machine.display_stock()


    def select_item(self, product_code) -> None:
        self.vending_machine.set_state(self.vending_machine.selectItem)
        self.vending_machine.select_item(product_code)


    def collect_cash(self, amount) -> None:
        logging.critical("Can't accept cash, please select item first")


    def dispense_item(self) -> None:
        logging.critical(f"Can't dispense item in Idle")


    def dispense_change(self) -> None:
        logging.critical(f"Can't dispense change in Idle")


    def cancel_transaction(self) -> None:
        logging.critical(f"Can't cancel uninitialized transaction")

