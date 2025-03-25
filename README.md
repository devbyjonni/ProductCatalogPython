# ProductCatalogPython

##  Overview
ProductCatalogPython is a **Python 3 console application**, converted from the original C# and Swift versions. It allows users to manage a product catalog through a simple terminal interface, supporting product entry, search, and listing.

---

##  Features
- Add products with:
  - **Category** (e.g., Electronics, Clothing, etc.)
  - **Product Name** (custom input)
  - **Price** (positive decimal only)
- **Sorted Output**: Displays products sorted by price (ascending)
- **Search**: Find products by name
- **Error Handling**: Validates user input
- **Command Flow**:
  - `P` to add a product
  - `S` to search products
  - `Q` to quit

---

##  How to Run

1. Open Terminal and navigate to the project root.
2. Run the app using:
   ```bash
   python3 -m src.main
   ```

---

##  Testing

Unit tests are written using Python’s built-in `unittest` module with `unittest.mock` for input simulation.

---

### Run all tests:
```bash
python3 -m unittest discover tests
```

---

### Run a single test file:
```bash
python3 -m unittest tests/test_catalog_controller.py
```

---

## Author
Developed by **Jonni Åkesson** as part of a learning journey converting from **C# ➡️ Swift ➡️ Python** 🚀
```

---
