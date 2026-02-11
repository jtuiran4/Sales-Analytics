from abc import ABC, abstractmethod
import panda as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from datetime import datetime


class AnalyticsService(ABC):
    """Servicio de dominio para el análisis de datos de ventas. Define la lógica sin dependencias externas"""


    @abstractmethod
    def calculate_sales_metrics(self, df: pd.DataFrame) -> Dict[str, float]:
        """
        Calcula métricas clave de ventas.
        
        Args:
            df: DataFrame con columnas [total_amount, quantity, date]
            
        Returns:
            Dict con métricas: total_sales, avg_sale, total_transactions, etc.
        """
        pass
    
    @abstractmethod
    def analyze_trends(self, df: pd.DataFrame, period: str = 'M') -> pd.DataFrame:
        """
        Analiza tendencias de ventas por período.
        
        Args:
            df: DataFrame con ventas
            period: 'D' (día), 'W' (semana), 'M' (mes), 'Q' (trimestre), 'Y' (año)
            
        Returns:
            DataFrame con ventas agregadas por período.
        """
        pass

    @abstractmethod
    def calculate_growth_rate(self, df: pd.DataFrame, period: str = 'M') -> pd.DataFrame:
        """
        Calcula la tasa de crecimiento de ventas por período.
        
        Args:
            df: DataFrame con ventas y columna 'date'
            period: Período de agrupación
            
        Returns:
            DataFrame con growth_rate y variación porcentual
        """
        pass

    @abstractmethod
    def segment_customers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Segmenta clientes por comportamiento de compra (RFM Analysis).
        
        Args:
            df: DataFrame con ventas [customer_id, date, total_amount]
            
        Returns:
            DataFrame con segmentos: VIP, Regular, At Risk, Lost
        """
        pass

    @abstractmethod
    def calculate_customer_lifetime_value(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calcula el Customer Lifetime Value (CLV).
        
        Args:
            df: DataFrame con ventas por cliente [customer_id, total_amount, date]
            
        Returns:
            DataFrame con CLV por cliente
        """
        pass

    @abstractmethod
    def analyze_product_performance(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Analiza el desempeño de productos.
        
        Args:
            df: DataFrame con ventas [product_id, product_name, total_amount, quantity]
            
        Returns:
            DataFrame con métricas por producto
        """
        pass

    @abstractmethod
    def calculate_abc_analysis(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Realiza análisis ABC de productos (Pareto).
        
        Args:
            df: DataFrame con productos y ventas
            
        Returns:
            DataFrame con clasificación ABC
        """
        pass

    @abstractmethod
    def analyze_seasonality(self, df: pd.DataFrame) -> Dict[str, pd.Series]:
        """
        Analiza la estacionalidad de las ventas.
        
        Args:
            df: DataFrame con ventas y fechas
            
        Returns:
            Dict con análisis por mes, día de semana, hora
        """
        pass

    @abstractmethod
    def calculate_forecasts(self, df: pd.DataFrame, periods: int = 12, method: str = 'moving_average') -> pd.DataFrame:
        """
        Genera pronósticos de ventas.
        
        Args:
            df: DataFrame con series temporales de ventas
            periods: Número de períodos a pronosticar
            method: 'moving_average', 'exponential_smoothing', 'linear_regression'
            
        Returns:
            DataFrame con pronósticos
        """
        pass

    @abstractmethod
    def analyze_regional_performance(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Analiza el desempeño de ventas por región.
        
        Args:
            df: DataFrame con ventas [region, total_amount, quantity]
            
        Returns:
            DataFrame con métricas por región
        """
        pass

    @abstractmethod
    def calculate_conversion_funnel(self, df: pd.DataFrame) -> Dict[str, float]:
        """
        Calcula métricas de conversión del embudo de ventas.
        
        Args:
            df: DataFrame con etapas del funnel
            
        Returns:
            Dict con tasas de conversión
        """
        pass

    @abstractmethod
    def identify_cross_sell_opportunities(self, df: pd.DataFrame, min_support: float = 0.01) -> pd.DataFrame:
        """
        Identifica oportunidades de venta cruzada (Market Basket Analysis).
        
        Args:
            df: DataFrame con transacciones [transaction_id, product_id]
            min_support: Soporte mínimo para asociaciones
            
        Returns:
            DataFrame con productos frecuentemente comprados juntos
        """
        pass

    @abstractmethod
    def calculate_cohort_analysis(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Realiza análisis de cohortes de clientes.
        
        Args:
            df: DataFrame con ventas [customer_id, date, total_amount]
            
        Returns:
            DataFrame con retención por cohorte
        """
        pass
        
    @abstractmethod
    def detect_anomalies(self, df: pd.DataFrame, threshold: float = 3.0) -> pd.DataFrame:
        """
        Detecta anomalías en las ventas usando Z-score.
        
        Args:
            df: DataFrame con series temporales
            threshold: Umbral de desviaciones estándar
            
        Returns:
            DataFrame con anomalías detectadas
        """
        pass

    @abstractmethod
    def calculate_churn_probability(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calcula la probabilidad de abandono de clientes.
        
        Args:
            df: DataFrame con historial de clientes
            
        Returns:
            DataFrame con probabilidad de churn por cliente
        """
        pass