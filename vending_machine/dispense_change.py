from __future__ import annotations
from vending_machine.state import State

class DispenseChange(State):

    def display_stock(self) -> None:
        raise RuntimeError(f"Can't display stock in dispense change state")


    def select_item(self, productCode) -> None:
        raise RuntimeError(f"Can't select item in dispense change state")


    def collect_cash(self, amount) -> None:
        raise RuntimeError(f"Can't collect cash in dispense change state")


    def dispense_item(self) -> None:
        raise RuntimeError(f"Can't dispense item in dispense change state")


    def dispense_change(self) -> None:
        print("Dispensing change")
        self.vending_machine.collected_cash = 0
        self.vending_machine.set_state(self.vending_machine.idle)


    def cancel_transaction(self) -> None:
        raise RuntimeError(f"Can't cancel transaction in dispense change state")

