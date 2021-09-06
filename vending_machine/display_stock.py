from __future__ import annotations
from vending_machine.state import State

class DisplayStock(State):

    def display_stock(self) -> None:
        print("Task DisplayStock")
        # TODO: add way for print with number to select
        print(self.vending_machine.stocks)


    def select_item(self, product_code) -> None:
        self.vending_machine.set_state(self.vending_machine.selectItem)
        self.vending_machine.select_item(product_code)


    def collect_cash(self, amount) -> None:
        raise RuntimeError(f"Can't collect cash in a display stock state")


    def dispense_item(self) -> None:
        raise RuntimeError(f"Can't dispense item in a display stock state")


    def dispense_change(self) -> None:
        raise RuntimeError(f"Can't cancel transaction in a display stock state")


    def cancel_transaction(self) -> None:
        raise RuntimeError(f"Can't cancel transaction in a display stock state")
