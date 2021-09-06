from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod

class State(ABC):

    @property
    def vending_machine(self) -> VendingMachine:
        return self._vending_machine

    @vending_machine.setter
    def vending_machine(self, vending_machine: VendingMachine) -> None:
        self._vending_machine = vending_machine

    @abstractmethod
    def display_stock(self) -> None:
        pass

    @abstractmethod
    def select_item(self, productCode) -> None:
        pass

    @abstractmethod
    def collect_cash(self, amount) -> None:
        pass

    @abstractmethod
    def dispense_item(self) -> None:
        pass

    @abstractmethod
    def dispense_change(self) -> None:
        pass

    @abstractmethod
    def cancel_transaction(self) -> None:
        pass
