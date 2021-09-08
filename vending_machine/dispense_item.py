from __future__ import annotations
from vending_machine.state import State
import logging


class DispenseItem(State):

    def display_stock(self) -> None:
        logging.critical("Can't display stock in dispense Item state")

    def select_item(self, product_code) -> None:
        logging.critical("Can't select item in dispense Item state")

    def collect_cash(self, amount) -> None:
        logging.critical("Can't collect cash in dispense Item state")

    def dispense_item(self) -> None:
        logging.info(f"Dispensing item {self.vending_machine.selected_item['name']}")

        self.vending_machine.set_state(self.vending_machine.dispenseChange)
        self.vending_machine.dispense_change()

    def dispense_change(self) -> None:
        logging.critical("Can't dispense change in dispense Item state")

    def cancel_transaction(self) -> None:
        logging.critical("Can't cancel transaction in dispense Item state")
