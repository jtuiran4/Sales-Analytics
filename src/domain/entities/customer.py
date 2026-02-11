from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Customer:
    """Entidad que representa a un cliente."""
    id: Optional[int]
    name: str
    email: str
    phone: str
    region: str
    registration_date: datetime
    segment: Optional[str] = None # VIP, Regular, New

    def __post_init__(self):
        if not self.email or "@" not in self.email:
            raise ValueError("El correo electrónico no es válido.")
        if not self.name.strip():
            raise ValueError("El nombre del cliente no puede estar vacío.")