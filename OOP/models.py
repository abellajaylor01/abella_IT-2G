"""
Models module for the Ordering System.
Encapsulates domain concepts into object-oriented classes.
"""

from typing import Dict, List, Optional


class MenuItem:
    """Represents an individual item on the menu."""

    def __init__(self, item_id: int, name: str, price: float):
        self.item_id = item_id
        self.name = name
        self.price = price

    def calculate_subtotal(self, quantity: int) -> float:
        """Calculates subtotal for a given quantity of this item."""
        return self.price * quantity


class CartItem:
    """Represents an item added to the customer's cart."""

    def __init__(self, menu_item: MenuItem, quantity: int):
        self.menu_item = menu_item
        self.quantity = quantity

    @property
    def subtotal(self) -> float:
        """Dynamically calculates the subtotal for this cart entry."""
        return self.menu_item.calculate_subtotal(self.quantity)


class ShoppingCart:
    """Manages the collection of items selected by a customer."""

    def __init__(self):
        self._items: List[CartItem] = []

    @property
    def items(self) -> List[CartItem]:
        """Returns an immutable view of items in the cart."""
        return self._items.copy()

    def is_empty(self) -> bool:
        """Checks if the cart has any items."""
        return len(self._items) == 0

    def add_item(self, menu_item: MenuItem, quantity: int) -> CartItem:
        """Adds a new item to the cart."""
        cart_item = CartItem(menu_item, quantity)
        self._items.append(cart_item)
        return cart_item

    def calculate_total(self) -> float:
        """Calculates total cost of all items in the cart."""
        return sum(item.subtotal for item in self._items)


class PaymentProcessor:
    """Handles payment validation and change calculation."""

    def __init__(self, total_due: float):
        self.total_due = total_due

    def is_sufficient(self, payment_amount: float) -> bool:
        """Validates if the tendered cash covers the total due."""
        return payment_amount >= self.total_due

    def calculate_shortage(self, payment_amount: float) -> float:
        """Calculates how much money is still owed."""
        return max(0.0, self.total_due - payment_amount)

    def calculate_change(self, payment_amount: float) -> float:
        """Calculates change owed to the customer."""
        return max(0.0, payment_amount - self.total_due)


class MenuCatalog:
    """Manages available menu items."""

    def __init__(self):
        self._catalog: Dict[int, MenuItem] = {}
        self._load_default_menu()

    def _load_default_menu(self) -> None:
        """Populates initial catalog data."""
        default_data = [
            (1, "Burger Combo", 150.00),
            (2, "Chicken Meal", 180.00),
            (3, "Spaghetti Special", 120.00),
            (4, "Fries & Drink", 75.00),
            (5, "Iced Tea", 45.00),
            (6, "JAY Tea", 55.00),
            (7, "Burger Extra Large", 220.00),
            (8, "Popcorn & Milkshake", 130.00)
        ]
        for item_id, name, price in default_data:
            self._catalog[item_id] = MenuItem(item_id, name, price)

    def get_item(self, item_id: int) -> Optional[MenuItem]:
        """Fetches an item by ID, returning None if not found."""
        return self._catalog.get(item_id)

    def get_all_items(self) -> Dict[int, MenuItem]:
        """Returns all items in the catalog."""
        return self._catalog