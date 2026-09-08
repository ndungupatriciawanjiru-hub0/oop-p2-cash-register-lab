#!/usr/bin/env python3


class CashRegister:
    """A cash register that can add items, apply a percentage discount,
    and void the most recently added item."""

    def __init__(self, discount=0):
        self.discount = discount          # validated via the property setter
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Must be an integer between 0 and 100 inclusive
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        """Add `item` at `price`, `quantity` times, to the register."""
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        # Track this transaction so it can later be voided
        self.previous_transactions.append(
            {"item": item, "price": price, "quantity": quantity}
        )

    def apply_discount(self):
        """Apply the register's discount percentage to the current total."""
        if self.discount:
            discounted_total = self.total - (self.total * (self.discount / 100))

            # Show a whole number instead of e.g. 800.0 when there's no
            # fractional part, to match "the total comes to $800."
            if discounted_total == int(discounted_total):
                discounted_total = int(discounted_total)

            self.total = discounted_total
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Remove the most recently added item(s) from the register."""
        if self.previous_transactions:
            last_transaction = self.previous_transactions.pop()

            self.total -= last_transaction["price"] * last_transaction["quantity"]

            for _ in range(last_transaction["quantity"]):
                if self.items:
                    self.items.pop()
        else:
            print("There is no transaction to void.")
