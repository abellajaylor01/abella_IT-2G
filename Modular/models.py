"""
Branch: ABELLAJAYLORD
Project: Interactive Ordering & Payment System
Description: Core business logic and data structures.
"""

from typing import Dict, List, Tuple


class OrderingSystemABELLAJAYLORD:
    """Handles item menu selection, cost computation, and cash payments."""

    MENU: Dict[int, Dict[str, float]] = {
        1: {"name": "Burger Combo", "price": 150.00},
        2: {"name": "Chicken Meal", "price": 180.00},
        3: {"name": "Spaghetti Special", "price": 120.00},
        4: {"name": "Fries & Drink", "price": 75.00},
        5: {"name": "Iced Tea", "price": 45.00},
        6: {"name": "JAY Tea", "price": 55.00},
        7: {"name": "Burger Extra Large", "price": 220.00},
        8: {"name": "Popcorn & Milkshake", "price": 130.00}
    }

    @classmethod
    def get_menu(cls) -> Dict[int, Dict[str, float]]:
        """Returns the current menu catalog."""
        return cls.MENU

    @staticmethod
    def calculate_total(cart: List[Tuple[str, int, float]]) -> float:
        """Calculates the gross total price of all items in the cart."""
        return sum(quantity * price for _, quantity, price in cart)

    @staticmethod
    def calculate_change(payment: float, total: float) -> float:
        """Calculates change owed to customer."""
        return payment - total