"""
Branch: ABELLAJAYLORD
Project: Interactive Ordering & Payment System
Description: Terminal user interface, table layout, and receipt generation.
"""

from datetime import datetime
from typing import Dict, List, Tuple


class TerminalUIABELLAJAYLORD:
    """Provides clean terminal alignment, indention, and output formatting."""

    BORDER_LINE = "+" + "-" * 10 + "+" + "-" * 30 + "+" + "-" * 12 + "+"

    @staticmethod
    def print_header(title: str) -> None:
        """Prints a styled section header."""
        print("\n" + "=" * 56)
        print(f"{title.center(56)}")
        print("=" * 56)

    @classmethod
    def display_menu(cls, menu: Dict[int, Dict[str, float]]) -> None:
        """Displays the menu in a clean tabular format."""
        cls.print_header("BRANCH [ABELLAJAYLORD] - MENU OPTIONS")
        print(cls.BORDER_LINE)
        print(f"| {'Item No.':<10} | {'Item Name':<30} | {'Price':<12} |")
        print(cls.BORDER_LINE)
        for item_num, details in menu.items():
            price_str = f"P{details['price']:.2f}"
            print(f"| {item_num:<10} | {details['name']:<30} | {price_str:<12} |")
        print(cls.BORDER_LINE)

    @classmethod
    def print_receipt(
            cls,
            customer_name: str,
            cart: List[Tuple[str, int, float]],
            total: float,
            payment: float,
            change: float
    ) -> None:
        """Prints a structured final receipt to the terminal."""
        cls.print_header("OFFICIAL ORDER RECEIPT")
        print(f"  Branch        : ABELLAJAYLORD")
        print(f"  Customer Name : {customer_name}")
        print(f"  Transaction   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        print("  Ordered Items:")
        print("  " + "-" * 50)
        for item_name, qty, subtotal in cart:
            print(f"    • {item_name:<25} x{qty:<3} : P{subtotal:>8.2f}")
        print("  " + "-" * 50)

        print(f"  Total Amount Due  : P{total:>8.2f}")
        print(f"  Amount Tendered   : P{payment:>8.2f}")
        print(f"  Change            : P{change:>8.2f}")
        print("=" * 56 + "\n")