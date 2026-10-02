"""
UI module for managing terminal output, headers, menus, and receipts.
"""

from datetime import datetime
from models import MenuCatalog, ShoppingCart


class TerminalUI:
    """Encapsulates UI output formatting and styling."""

    BORDER_LINE = "+" + "-" * 10 + "+" + "-" * 30 + "+" + "-" * 12 + "+"

    def __init__(self, branch_name: str):
        self.branch_name = branch_name

    def print_header(self, title: str) -> None:
        """Prints a styled section header."""
        print("\n" + "=" * 56)
        print(f"{title.center(56)}")
        print("=" * 56)

    def display_menu(self, catalog: MenuCatalog) -> None:
        """Displays the menu catalog in tabular format."""
        self.print_header(f"BRANCH [{self.branch_name}] - MENU OPTIONS")
        print(self.BORDER_LINE)
        print(f"| {'Item No.':<10} | {'Item Name':<30} | {'Price':<12} |")
        print(self.BORDER_LINE)

        for item_id, item in catalog.get_all_items().items():
            price_str = f"P{item.price:.2f}"
            print(f"| {item_id:<10} | {item.name:<30} | {price_str:<12} |")

        print(self.BORDER_LINE)

    def print_receipt(
            self,
            customer_name: str,
            cart: ShoppingCart,
            payment_amount: float,
            change: float
    ) -> None:
        """Prints an official structured receipt."""
        self.print_header("OFFICIAL ORDER RECEIPT")
        print(f"  Branch        : {self.branch_name}")
        print(f"  Customer Name : {customer_name}")
        print(f"  Transaction   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        print("  Ordered Items:")
        print("  " + "-" * 50)
        for item in cart.items:
            print(
                f"    • {item.menu_item.name:<25} "
                f"x{item.quantity:<3} : P{item.subtotal:>8.2f}"
            )
        print("  " + "-" * 50)

        total_due = cart.calculate_total()
        print(f"  Total Amount Due  : P{total_due:>8.2f}")
        print(f"  Amount Tendered   : P{payment_amount:>8.2f}")
        print(f"  Change            : P{change:>8.2f}")
        print("=" * 56 + "\n")