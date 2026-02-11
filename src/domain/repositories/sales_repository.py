from abc import ABC, abstractmethod
from typing import List, Optional
import pandas as pd
from datetime import datetime

from ..entities.sale import Sale

class SalesRepository(ABC):
    """Interfaz para el repositorio de ventas."""

    @abstractmethod
    def get_all(self) -> pd.DataFrame:
        """Obtiene todas las ventas."""
        pass
    
    @abstractmethod
    def get_by_id(self, sale_id: int) -> Optional[Sale]:
        """Obtiene una venta por su ID."""
        pass

    @abstractmethod
    def get_by_date_range(self, start_date: datetime, end_date: datetime) -> pd.DataFrame:
        """Obtiene ventas dentro de un rango de fechas."""
        pass

    @abstractmethod
    def get_by_region(self,region: str) -> pd.DataFrame:
        """Obtiene ventas por región."""
        pass

    @abstractmethod
    def get_by_category(self, category: str) -> dp.DataFrame:
        """Obtiene ventas por categoría de producto."""
        pass

    @abstractmethod
    def save(self, sale: Sale ) -> Sale:
        """Guarda una nueva venta."""
        pass

    @abstractmethod
    def save_bulk(self, sales: List[Sale]) -> int:
        """Guarda múltiples ventas."""
        pass

    @abstractmethod
    def delete(self, sale_id: int) -> bool:
        """Elimina una venta por su ID."""
        pass

    @abstractmethod
    def save_dataframe(self, df: pd.DataFrame, if_exists: str = 'append') -> int:
        """Guarda un DataFrame de ventas."""
        pass

    @abstractmethod
    def get_aggregated_by_period(self, period: str = 'M') -> pd.DataFrame:
        """Obtiene ventas agregadas por período (diario, mensual, anual)."""
        pass

    @abstractmethod
    def get_top_products(self, limit: int = 10, start_date: datetime = None, end_date: datetime = None) -> pd.DataFrame:
        """Obtiene los productos más vendidos."""
        pass
