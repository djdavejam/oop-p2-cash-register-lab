class CashRegister:
    """
    A cash register class that manages items, totals, discounts, and transactions.
    
    Attributes:
        discount (int): Percentage discount (0-100)
        total (float): Current total amount
        items (list): List of all items added
        previous_transactions (list): List of transaction dictionaries
    """
    
    def __init__(self, discount=0):
        """
        Initialize the cash register.
        
        Args:
            discount (int): Optional discount percentage (default: 0)
        """
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):
        """Get the current discount percentage."""
        return self._discount
    
    @discount.setter
    def discount(self, value):
        """
        Set the discount percentage with validation.
        
        Args:
            value: Discount percentage to set
        """
        if not isinstance(value, int):
            print("Not valid discount")
            self._discount = 0
        elif value < 0 or value > 100:
            print("Not valid discount")
            self._discount = 0
        else:
            self._discount = value
    
    def add_item(self, item, price, quantity=1):
        """
        Add an item to the cash register.
        
        Args:
            item (str): Name of the item
            price (float): Price per unit
            quantity (int): Number of items (default: 1)
        """
        # Add to total
        item_total = price * quantity
        self.total += item_total
        
        # Add items to the items list (one entry per item)
        for _ in range(quantity):
            self.items.append(item)
        
        # Add transaction record
        transaction = {
            'item': item,
            'price': price,
            'quantity': quantity,
            'total': item_total
        }
        self.previous_transactions.append(transaction)
    
    def apply_discount(self):
        """
        Apply the discount to the current total.
        Prints appropriate message based on discount availability.
        """
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            # Calculate discount amount and new total
            discount_multiplier = (100 - self.discount) / 100
            self.total = self.total * discount_multiplier
            print(f"After the discount, the total comes to ${self.total:.0f}.")
    
    def void_last_transaction(self):
        """
        Void the last transaction by removing its items and adjusting the total.
        """
        if self.previous_transactions:
            # Get the last transaction
            last_transaction = self.previous_transactions.pop()
            
            # Subtract the transaction total from the overall total
            self.total -= last_transaction['total']
            
            # Remove items from the items list
            item_name = last_transaction['item']
            quantity = last_transaction['quantity']
            
            # Remove the correct number of items from the end of the list
            for _ in range(quantity):
                if item_name in self.items:
                    # Remove from the end to maintain proper order
                    for i in range(len(self.items) - 1, -1, -1):
                        if self.items[i] == item_name:
                            self.items.pop(i)
                            break