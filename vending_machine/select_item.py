from __future__ import annotations
from vending_machine.state import State
import logging


class SelectItem(State):

    def display_stock(self) -> None:
        self.vending_machine.set_state(self.vending_machine.displayStock)

    def select_item(self, product_code) -> None:
        logging.debug('Task SelectItem')
        try:
            if not product_code.isdigit():
                raise ValueError(f'Invalid product Code: ({product_code}), please enter valid product number')

            product_code = int(product_code)
            if product_code not in self.vending_machine.stocks:
                raise ValueError(f'Invalid product Code: ({product_code}), please enter product number from stock list')

            selected_item = self.vending_machine.stocks.get(product_code, None)

            if not selected_item:
                raise RuntimeError(f'Item product Code: ({product_code}) Not Found')

            self.vending_machine.selected_item = selected_item
            logging.info(f"----- Item '{self.vending_machine.selected_item['name']}' with price of ({self.vending_machine.selected_item['price']}$) selected  -----")
            self.vending_machine.set_state(self.vending_machine.collectCash)

        except Exception as e:
            logging.critical(f'An exception of type {type(e).__name__} occurred. {str(e)}')

    def collect_cash(self, amount) -> None:
        logging.critical("Can't collect cash in select item state")

    def dispense_item(self) -> None:
        logging.critical("Can't dispense item in select item state")

    def dispense_change(self) -> None:
        logging.critical("Can't dispense change in select item state")

    def cancel_transaction(self) -> None:
        logging.critical("Can't cancel transaction in select item state")
