class Product:
    def __init__(self, product_id: str, color: str):
        self.product_id = product_id
        self.color = color
        self.quantity = 1

    def __eq__(self, other):
        """Equals between Products. If the other is not a Product - raise an error"""
        if type(other) != Product:
            raise TypeError("Argument of __eq__ must be of type Product")
        if self.product_id == other.product_id and self.color == other.color:
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.product_id}, {self.color}"
