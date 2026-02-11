from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class Sale:
    """Entidad que representa una venta."""
    id: Optional[int]
    date: datetime
    product_id: int
    customer_id: int
    quantity: int
    unit_price: Decimal
    total_amount: Decimal
    region: str
    category: str

    def __post_init__(self):
        """Validaciones de negocio."""
        if self.quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if self.unit_price < 0:
            raise ValueError("El precio unitario no puede ser negativo.")
        if self.total_amount != self.unit_price * self.quantity:
            raise ValueError("El monto total debe ser igual al precio unitario por la cantidad.")
        
    def calculate_discount(self, discount_percentage: Decimal) -> Decimal:
        """Calcula el descuento aplicado a la venta."""
        return self.total_amount * (1 - Decimal(str(discount_percentage / 100)))