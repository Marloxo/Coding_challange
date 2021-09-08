from __future__ import annotations
from vending_machine.state import State
import logging


class CancelTransaction(State):

    def display_stock(self) -> None:
        logging.critical("Can't display stock in a cancelled transaction")

    def select_item(self, product_code) -> None:
        logging.critical("Can't select item in a cancelled transaction")

    def collect_cash(self, amount) -> None:
        logging.critical("Can't collect cash in a cancelled transaction")

    def dispense_item(self) -> None:
        logging.critical("Can't dispense item in a cancelled transaction")

    def dispense_change(self) -> None:
        logging.critical("Can't dispense change in a cancelled transaction")

    def cancel_transaction(self) -> None:
        logging.debug('Task CancelTransaction')
        if self.vending_machine.collected_cash:
            logging.info(f'Returning collected cash: {self.vending_machine.collected_cash}$')
        else:
            logging.info('No cash has been collected')

        self.vending_machine.collected_cash = 0
        self.vending_machine.selected_item = None
        self.vending_machine.set_state(self.vending_machine.idle)
        logging.info('Transaction Cancelled')
