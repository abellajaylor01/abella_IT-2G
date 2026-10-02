"""
Main application controller that orchestrates user interactions,
cart additions, and payment processing through object instances.
"""

from models import MenuCatalog, ShoppingCart, PaymentProcessor
from ui import TerminalUI


class StoreSystem:
    """Master controller managing the ordering process state."""

    def __init__(self, branch_name: str):
        self.branch_name = branch_name
        self.catalog = MenuCatalog()
        self.ui = TerminalUI(branch_name)
        self.cart = ShoppingCart()
        self.customer_name = "Guest Customer"

    def run(self) -> None:
        """Starts the main application loop."""
        self.ui.print_header(f"WELCOME TO {self.branch_name} STORE")

        entered_name = input("  Enter Customer Name: ").strip()
        if entered_name:
            self.customer_name = entered_name

        self.ui.display_menu(self.catalog)
        self._process_order_loop()
        payment_amount = self._process_payment_loop()

        # Final Receipt
        payment_processor = PaymentProcessor(self.cart.calculate_total())
        change = payment_processor.calculate_change(payment_amount)
        self.ui.print_receipt(
            self.customer_name,
            self.cart,
            payment_amount,
            change
        )

    def _process_order_loop(self) -> None:
        """Interactively collects items from customer."""
        while True:
            try:
                choice = int(input("\n  Enter Item Number to order (1-8, or 0 to finish): "))
                if choice == 0:
                    if self.cart.is_empty():
                        print("  [!] Cart is empty. Please select at least one item.")
                        continue
                    break

                menu_item = self.catalog.get_item(choice)
                if not menu_item:
                    print("  [!] Invalid choice. Pick an item number from 1 to 8.")
                    continue

                quantity = int(input(f"  Enter quantity for {menu_item.name}: "))
                if quantity <= 0:
                    print("  [!] Quantity must be at least 1.")
                    continue

                added_item = self.cart.add_item(menu_item, quantity)
                print(f"  [✓] Added: {quantity}x {menu_item.name} (Subtotal: P{added_item.subtotal:.2f})")

            except ValueError:
                print("  [!] Invalid input. Please enter numbers only.")

    def _process_payment_loop(self) -> float:
        """Handles user cash entry until payment threshold is met."""
        total_due = self.cart.calculate_total()
        processor = PaymentProcessor(total_due)

        print("\n  ==================================================")
        print(f"  TOTAL AMOUNT DUE: P{total_due:.2f}")
        print("  ==================================================")

        while True:
            try:
                payment = float(input("  Enter Cash Payment Amount: P"))
                if not processor.is_sufficient(payment):
                    shortage = processor.calculate_shortage(payment)
                    print(f"  [!] Insufficient cash. You still owe P{shortage:.2f}.")
                else:
                    return payment
            except ValueError:
                print("  [!] Invalid cash amount. Please enter a valid number.")


if __name__ == "__main__":
    app = StoreSystem(branch_name="ABELLAJAYLORD")
    app.run()