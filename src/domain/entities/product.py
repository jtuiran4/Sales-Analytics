from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class Product:
    """Entidad que representa a un producto."""
    id: Optional[int]
    name : str
    category: str
    price: Decimal
    cost: Decimal
    stock: int

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("El precio debe ser positivo.")
        if self.cost < 0:
            raise ValueError("El costo no puede ser negativo.")
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        
    def calculate_margin(self) -> Decimal:
        """Calcula el margen de beneficio del producto."""
        if self.price == 0:
            return ((self.price - self.cost) / self.price) * 100
        
    def is_in_stock(self, quantity: int) -> bool:
        """Verifica si el producto está en stock."""
        return self.stock >= quantity