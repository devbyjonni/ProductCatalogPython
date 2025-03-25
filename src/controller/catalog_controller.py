from decimal import Decimal, InvalidOperation

from src.model.product import Product


class ProductCatalogController:
    def __init__(self):
        self.products = []

    def run(self):
        while True:
            self.clear_screen()
            print('🟡 To enter a new product - follow the steps | To quit - enter: "Q"')

            category = self.get_user_input("Enter a Category: ")
            if category is None:
                self.display_products()
                return

            name = self.get_user_input("Enter a Product Name: ")
            if name is None:
                self.display_products()
                return

            price = self.read_valid_price("Enter a Price: ")
            if price is None:
                self.display_products()
                return

            self.products.append(Product(category, name, price))
            self.print_success("✅ The product was successfully added!")

    def get_user_input(self, prompt: str) -> str | None:
        while True:
            value = input(prompt).strip()
            if not value:
                self.print_error("❌ Input cannot be empty.")
                continue
            if value.upper() == "Q":
                return None
            return value

    def read_valid_price(self, prompt: str) -> Decimal | None:
        while True:
            value = input(prompt).strip()
            if value.upper() == "Q":
                return None
            try:
                price = Decimal(value)
                if price <= 0:
                    raise InvalidOperation
                return price
            except (InvalidOperation, ValueError):
                self.print_error("❌ Invalid price. Please enter a positive number.")

    def display_products(self):
        self.clear_screen()
        print("🟡 Category\tProduct\tPrice")

        sorted_products = sorted(self.products, key=lambda p: p.price)
        for product in sorted_products:
            print(product)

        total = sum(p.price for p in sorted_products)
        print(f"\nTotal amount: {total}")

        self.print_command_menu()
        self.handle_user_choice()

    def handle_user_choice(self):
        while True:
            choice = input("\nEnter a command: ").strip().upper()
            if choice == "P":
                self.run()
                return
            elif choice == "S":
                self.search_product()
                return
            elif choice == "Q":
                exit(0)
            else:
                self.print_error("❌ Invalid choice. Please try again.")

    def search_product(self):
        name = input("Enter a Product Name: ").strip()
        if name.upper() == "Q":
            return

        found = [p for p in self.products if p.name.lower() == name.lower()]

        self.clear_screen()
        print("🟡 Category\tProduct\tPrice")

        if not found:
            self.print_error("\nNo products found matching your search.")
        else:
            for product in found:
                print(f"🟣 {product}")

        self.print_command_menu()
        self.handle_user_choice()

    def print_command_menu(self):
        print(
            '\nTo enter a new product - enter: "P" | To search for a product - enter: "S" | To quit - enter: "Q"'
        )

    def print_success(self, message: str):
        print(message)

    def print_error(self, message: str):
        print(message)

    def clear_screen(self):
        print("\033c", end="")
