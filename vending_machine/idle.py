from __future__ import annotations
from vending_machine.state import State

class Idle(State):

    def display_stock(self) -> None:
        self.vending_machine.set_state(self.vending_machine.displayStock)
        self.vending_machine.display_stock()


    def select_item(self, productCode) -> None:
        self.vending_machine.set_state(self.vending_machine.selectItem)
        self.vending_machine.select_item()


    def collect_cash(self, amount) -> None:
        raise RuntimeError(f"Can't collect cash in Idle")


    def dispense_item(self) -> None:
        raise RuntimeError(f"Can't dispense item in Idle")


    def dispense_change(self) -> None:
        raise RuntimeError(f"Can't dispense change in Idle")


    def cancel_transaction(self) -> None:
        raise RuntimeError(f"Can't cancel transaction in Idle")

