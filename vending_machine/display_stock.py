from __future__ import annotations
from vending_machine.state import State
import logging


class DisplayStock(State):

    def display_stock(self) -> None:
        logging.debug('Task DisplayStock')
        for key, obj in self.vending_machine.stocks.items():
            logging.info(f'[{key}] {obj["name"]} ({obj["price"]}$)')

    def select_item(self, product_code) -> None:
        self.vending_machine.set_state(self.vending_machine.selectItem)
        self.vending_machine.select_item(product_code)

    def collect_cash(self, amount) -> None:
        logging.critical("Can't collect cash in a display stock state")

    def dispense_item(self) -> None:
        logging.critical("Can't dispense item in a display stock state")

    def dispense_change(self) -> None:
        logging.critical("Can't cancel transaction in a display stock state")

    def cancel_transaction(self) -> None:
        logging.critical("Can't cancel transaction in a display stock state")
