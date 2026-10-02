"""
Branch: ABELLAJAYLORD
Project: Interactive Ordering & Payment System
Description: Main interactive execution script.
"""

from typing import List, Tuple
from models import OrderingSystemABELLAJAYLORD
from ui import TerminalUIABELLAJAYLORD


def main() -> None:
    """Main execution routine for branch ABELLAJAYLORD."""

    TerminalUIABELLAJAYLORD.print_header("WELCOME TO ABELLAJAYLORD STORE")
    customer_name = input("  Enter Customer Name: ").strip()
    if not customer_name:
        customer_name = "Guest Customer"

    menu = OrderingSystemABELLAJAYLORD.get_menu()
    TerminalUIABELLAJAYLORD.display_menu(menu)

    cart: List[Tuple[str, int, float]] = []

    # --- Item Selection Loop ---
    while True:
        try:
            choice = int(input("\n  Enter Item Number to order (1-8, or 0 to finish): "))
            if choice == 0:
                if not cart:
                    print("  [!] Cart is empty. Please select at least one item.")
                    continue
                break

            if choice not in menu:
                print("  [!] Invalid choice. Please pick an item number from 1 to 8.")
                continue

            quantity = int(input(f"  Enter quantity for {menu[choice]['name']}: "))
            if quantity <= 0:
                print("  [!] Quantity must be at least 1.")
                continue

            item_name = menu[choice]["name"]
            unit_price = menu[choice]["price"]
            subtotal = unit_price * quantity

            cart.append((item_name, quantity, subtotal))
            print(f"  [✓] Added: {quantity}x {item_name} (Subtotal: P{subtotal:.2f})")

        except ValueError:
            print("  [!] Invalid input. Please enter numbers only.")

    # --- Payment Processing Loop ---
    total_amount = OrderingSystemABELLAJAYLORD.calculate_total(cart)
    print(f"\n  ==================================================")
    print(f"  TOTAL AMOUNT DUE: P{total_amount:.2f}")
    print(f"  ==================================================")

    while True:
        try:
            payment = float(input("  Enter Cash Payment Amount: P"))
            if payment < total_amount:
                shortage = total_amount - payment
                print(f"  [!] Insufficient cash. You still owe P{shortage:.2f}.")
            else:
                break
        except ValueError:
            print("  [!] Invalid cash amount. Please enter a valid number.")

    # --- Final Receipt Generation ---
    change = OrderingSystemABELLAJAYLORD.calculate_change(payment, total_amount)
    TerminalUIABELLAJAYLORD.print_receipt(customer_name, cart, total_amount, payment, change)


if __name__ == "__main__":
    main()