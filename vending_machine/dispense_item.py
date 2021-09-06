from __future__ import annotations
from vending_machine.state import State

class DispenseItem(State):

    def display_stock(self) -> None:
        raise RuntimeError(f"Can't display stock in dispense Item state")


    def select_item(self, product_code) -> None:
        raise RuntimeError(f"Can't select item in dispense Item state")


    def collect_cash(self, amount) -> None:
        raise RuntimeError(f"Can't collect cash in dispense Item state")


    def dispense_item(self) -> None:
        print(f"Dispensing item {self.vending_machine.selected_item['item']}")

        self.vending_machine.set_state(self.vending_machine.dispenseChange)
        self.vending_machine.dispense_change()


    def dispense_change(self) -> None:
        raise RuntimeError(f"Can't dispense change in dispense Item state")


    def cancel_transaction(self) -> None:
        raise RuntimeError(f"Can't cancel transaction in dispense Item state")

