from __future__ import annotations
from vending_machine.state import State

class CollectCash(State):

    def display_stock(self) -> None:
        raise RuntimeError(f"Can't display stock in a collect cash state")


    def select_item(self, productCode) -> None:
        raise RuntimeError(f"Can't select item in a collect cash state")


    def collect_cash(self, amount) -> None:
        print("Task CollectCash")
        if amount not in self.vending_machine.allowed_coins:
            raise ValueError("Invalid coin")

        self.vending_machine.collected_cash += amount
        print(f"Total CollectCash: {self.vending_machine.collected_cash}")

        if self.vending_machine.collected_cash >= self.vending_machine.selected_item[0]:
            self.set_state(self, self.dispenseItem)
            self.vending_machine.dispense_item()


    def dispense_item(self) -> None:
        raise RuntimeError(f"Can't dispense item in a collect cash state")


    def dispense_change(self) -> None:
        raise RuntimeError(f"Can't dispense change in a collect cash state")


    def cancel_transaction(self) -> None:
        self.set_state(self, self.cancelTransaction)
        self.vending_machine.cancel_transaction()

