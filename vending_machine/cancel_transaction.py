from __future__ import annotations
from vending_machine.state import State

class CancelTransaction(State):

    def display_stock(self) -> None:
        raise RuntimeError(f"Can't display stock in a cancelled transaction")


    def select_item(self, product_code) -> None:
        raise RuntimeError(f"Can't select item in a cancelled transaction")


    def collect_cash(self, amount) -> None:
        raise RuntimeError(f"Can't collect cash in a cancelled transaction")


    def dispense_item(self) -> None:
        raise RuntimeError(f"Can't dispense item in a cancelled transaction")


    def dispense_change(self) -> None:
        raise RuntimeError(f"Can't dispense change in a cancelled transaction")


    def cancel_transaction(self) -> None:
        print("Task CancelTransaction")
        self.vending_machine.collected_cash = 0
        self.vending_machine.selected_item = None
        self.vending_machine.set_state(self.vending_machine.idle)



