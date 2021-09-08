from __future__ import annotations
from vending_machine.state import State
import logging

class CollectCash(State):

    def display_stock(self) -> None:
        logging.critical(f"Can't display stock in a collect cash state, please cancel transaction first and select new item again")


    def select_item(self, product_code) -> None:
        logging.critical(f"Can't select item in a collect cash state, please cancel transaction first and select new item again")


    def collect_cash(self, amount) -> None:
        logging.debug("Task CollectCash")

        try:
            if not amount.isdigit():
                raise ValueError(f"Invalid coin: ({amount}$), please enter valid coin number")

            amount = int(amount)
            if amount not in self.vending_machine.allowed_coins:
                raise ValueError(f"Invalid coin: ({amount}$), please select from allowed coins list")

            self.vending_machine.collected_cash += amount
            logging.info(f"Total Collected Cash: {self.vending_machine.collected_cash}$")

            if self.vending_machine.collected_cash >= self.vending_machine.selected_item['price']:
                self.vending_machine.set_state(self.vending_machine.dispenseItem)
                self.vending_machine.dispense_item()
        except Exception as e:
            logging.critical(f'An exception of type {type(e).__name__} occurred. {str(e)}')


    def dispense_item(self) -> None:
        logging.critical(f"Can't dispense item in a collect cash state")


    def dispense_change(self) -> None:
        logging.critical(f"Can't dispense change in a collect cash state")


    def cancel_transaction(self) -> None:
        self.vending_machine.set_state(self.vending_machine.cancelTransaction)
        self.vending_machine.cancel_transaction()

