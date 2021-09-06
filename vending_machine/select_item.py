from __future__ import annotations
from vending_machine.state import State


class SelectItem(State):

    def display_stock(self) -> None:
        self.vending_machine.set_state(self.vending_machine.displayStock)


    def select_item(self, productCode) -> None:
        print("Task SelectItem")
        try:
            if productCode not in self.vending_machine.stocks:
                raise ValueError(f'Invalid productCode: {productCode}')

            selected_item = self.vending_machine.stocks.get(productCode, None)

            if not selected_item:
                raise RuntimeError(f'Item productCode: {productCode} Not Found')

            self.vending_machine.selected_item = selected_item
            print(f"item {self.vending_machine.selected_item} selected")

        except Exception as e:
            print(f'An exception occurred while selecting item: {str(e)}')

        self.vending_machine.set_state(self.vending_machine.collectCash)


    def collect_cash(self, amount) -> None:
        raise RuntimeError(f"Can't collect cash in select item state")


    def dispense_item(self) -> None:
        raise RuntimeError(f"Can't dispense item in select item state")


    def dispense_change(self) -> None:
        raise RuntimeError(f"Can't dispense change in select item state")


    def cancel_transaction(self) -> None:
        raise RuntimeError(f"Can't cancel transaction in select item state")
