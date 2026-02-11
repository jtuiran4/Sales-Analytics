from abc import ABC, abstractmethod
from typing import List, Optional
import pandas as pd

from ..entities.product import Product


class ProductRepository(ABC):
    """Interfaz para el repositorio de los productos."""

    @abstractmethod
    def get_all(self) -> pd.DataFrame:
        """Obtiene todos los productos."""
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Optional[Product]:
        """Obtiene un producto por su ID."""
        pass

    @abstractmethod
    def get_by_category(self, category: str) -> pd.DataFrame:
        """Obtiene productos por categoría."""
        pass

    @abstractmethod
    def get_low_stock(self, threshold: int = 10) -> pd.DataFrame:
        """Obtiene productos con stock bajo."""
        pass

    @abstractmethod
    def save(self, product: Product) -> Product:
        """Guarda un nuevo producto."""
        pass

    @abstractmethod
    def update_stock(self, product_id: int, quantity: int) -> bool:
        """Actualiza el stock de un producto."""
        pass

    @abstractmethod
    def delete(self, product_id: int) -> bool:
        """Elimina un producto por su ID."""
        pass

    @abstractmethod
    def get_products_with_margin(self) -> pd.DataFrame:
        """Obtiene productos con su margen de beneficio calculado."""
        pass

    @abstractmethod
    def get_best_sellers(self, limit: int = 10) -> pd.DataFrame:
        """Obtiene los productos más vendidos."""
        pass
