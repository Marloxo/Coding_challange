from __future__ import annotations
from vending_machine.state import State
import logging

class DispenseChange(State):

    def display_stock(self) -> None:
        logging.critical(f"Can't display stock in dispense change state")


    def select_item(self, product_code) -> None:
        logging.critical(f"Can't select item in dispense change state")


    def collect_cash(self, amount) -> None:
        logging.critical(f"Can't collect cash in dispense change state")


    def dispense_item(self) -> None:
        logging.critical(f"Can't dispense item in dispense change state")


    def dispense_change(self) -> None:
        logging.debug("Dispensing change")
        remaining_amount = self.vending_machine.collected_cash - self.vending_machine.selected_item['price']
        if remaining_amount:
            logging.info(f"returning {remaining_amount}$ cash")
        else:
            logging.info(f"No remaining amount")

        self.vending_machine.collected_cash = 0
        self.vending_machine.selected_item = None
        self.vending_machine.set_state(self.vending_machine.idle)


    def cancel_transaction(self) -> None:
        logging.critical(f"Can't cancel transaction in dispense change state")

