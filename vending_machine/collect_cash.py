from __future__ import annotations
from vending_machine.state import State

class CollectCash(State):

    def display_stock(self) -> None:
        raise RuntimeError(f"Can't display stock in a collect cash state")


    def select_item(self, product_code) -> None:
        raise RuntimeError(f"Can't select item in a collect cash state")


    def collect_cash(self, amount) -> None:
        print("Task CollectCash")

        try:
            if amount not in self.vending_machine.allowed_coins:
                raise ValueError(f"Invalid coin: {amount}")

            self.vending_machine.collected_cash += amount
            print(f"Total Collected Cash: {self.vending_machine.collected_cash}")

            if self.vending_machine.collected_cash >= self.vending_machine.selected_item['price']:
                self.vending_machine.set_state(self.vending_machine.dispenseItem)
                self.vending_machine.dispense_item()
        except Exception as e:
            print(f'An exception occurred while collecting cash: {str(e)}')


    def dispense_item(self) -> None:
        raise RuntimeError(f"Can't dispense item in a collect cash state")


    def dispense_change(self) -> None:
        raise RuntimeError(f"Can't dispense change in a collect cash state")


    def cancel_transaction(self) -> None:
        self.vending_machine.set_state(self.vending_machine.cancelTransaction)
        self.vending_machine.cancel_transaction()

