from abc import ABC, abstractmethod
from typing import List, Optional
import panda as pd

from ..entities.customer import Customer


class CustomerRepository(ABC):
    """Interfaz para el repositorio de clientes."""

    @abstractmethod
    def get_all(self) -> pd.DataFrame:
        """Obtiene todos los clientes."""
        pass

    @abstractmethod
    def get_by_id(self, customer_id: int) -> Optional[Customer]:
        """Obtiene un cliente por su ID."""
        pass

    @abstractmethod
    def get_by_region(self, region: str) -> pd.DataFrame:
        """Obtiene clientes por región."""
        pass

    @abstractmethod
    def get_by_segment(self, segment: str) -> pd.DataFrame:
        """Obtiene clientes por segmento."""
        pass
    
    @abstractmethod
    def save(self, customer: Customer) -> Customer:
        """Guarda un nuevo cliente."""
        pass

    @abstractmethod
    def update_segment(self, customer_id: int, segment: str) -> bool:
        """Actualiza el segmento de un cliente."""
        pass

    @abstractmethod
    def delete(self, customer_id: int) -> bool:
        """Elimina un cliente por su ID."""
        pass

    @abstractmethod
    def get_customers_with_purchases(self) -> pd.DataFrame:
        """Obtiene clientes con su historial de compras."""
        pass

    @abstractmethod
    def get_top_customers(self, limit: int = 10) -> pd.DataFrame:
        """Obtiene los clientes con más compras."""
        pass