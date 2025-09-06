# Cash Register Lab

A Python implementation of a cash register system for an e-commerce application.

## Overview

This project creates a `CashRegister` class that simulates basic cash register functionality including adding items, applying discounts, and voiding transactions.

## Features

- **Add Items**: Add products with price and quantity
- **Apply Discounts**: Apply percentage-based discounts to total
- **Void Transactions**: Remove the last transaction
- **Track Items**: Maintain a list of all items added
- **Transaction History**: Keep record of all transactions

## Quick Start

### Setup
1. Clone the repository
2. Open the project in your preferred IDE
3. Run the tests to verify implementation

### Basic Usage

```python
from cash_register import CashRegister

# Create a cash register with 20% discount
register = CashRegister(20)

# Add items
register.add_item("Apple", 1.50, 3)  # 3 apples at $1.50 each
register.add_item("Banana", 0.75)    # 1 banana at $0.75

# Check total
print(f"Total: ${register.total}")   # Total: $5.25

# Apply discount
register.apply_discount()            # Total becomes $4.20

# Void last transaction
register.void_last_transaction()     # Removes bananas, total now $3.60
```
## Testing

Run the test suite to verify functionality:

```bash
python -m pytest cash_register_test.py
```

The tests cover:
- Basic functionality (add items, calculate totals)
- Discount application and validation
- Transaction voiding
- Edge cases and error handling

## Implementation Notes

- Discount must be an integer between 0-100
- Items are tracked individually (quantity=3 creates 3 entries)
- Transactions store item details for voiding capability
- All monetary values maintain proper decimal precision

## Files

- `cash_register.py` - Main implementation
- `cash_register_test.py` - Test suite
- `README.md` - This documentation