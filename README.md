# Coding challenge

## Vending Machine

So starting with assumption for simple vending machines design, we will assume the machine start by:
User start interacting with the machine by checking list of snacks/prices, select a snack, put money into the machine, receive money back, etc.

So list snacks -> select -> receive money (for example only 1$, 2$, 5$ until money inserted >= price) -> dispense item -> dispense change.

with the following diagram: [TODO: attach diagram]

### Requirements

- A person should be able to browse machine available items
- A person should be able to choose an item & insert cash into the machine
- The Machine should keep track of the inserted cash with the price of the selected item
- The machine must display an option to cancel the operation
- Finally, if all the above steps succeed then the user gets the selected item and the remaining cash

### Create a Skeleton Implementation

### Advantages and Disadvantages

You can avoid writing massive conditional blocks for switching between states by using the state pattern instead of hard-coding state-specific behavior. It allows you to develop a flexible and maintainable application. You can add new states and transitions to the Context without changing it.

It's a good idea to use the state pattern if the logic of each state is complex and the states change frequently. Otherwise, it complicates simple things by bringing a plethora of classes and objects. The state pattern adds another level of indirection by imposing clients to rely on a State object, and it extends the context class to allow State objects to change the state of the Context.
