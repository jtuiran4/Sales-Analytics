from abc import ABC, abstractmethod
import panda as pd
import numpy as np
from typing import Dict, Tuple, List, Optional
from enum import Enum


class DistributorType(Enum):
    """Tipos de distribución estadística para análisis de ventas."""
    NORMAL = "normal"
    UNIFORM = "uniform"
    EXPONENTIAL = "exponential"
    POISSON = "poisson"


class StatisticalService(ABC):
    """
    Servicio de dominio para análisis estadístico avanzado.
    Usa NumPy y SciPy para cálculos estadísticos.
    Define la lógica matemática pura del negocio.
    """

    @abstractmethod
    def descriptive_statistics(self, data: np.ndarray) -> Dict[str, float]:
        """
        Calcula estadísticas descriptivas completas.
        
        Args:
            data: Array de NumPy con datos numéricos
            
        Returns:
            Dict con: mean, median, mode, std, variance, min, max, 
                     q25, q50, q75, skewness, kurtosis
        """
        pass

    @abstractmethod
    def correlation_analysis(self, df: pd.DataFrame, method: str = 'pearson') -> pd.DataFrame:
        """
        Calcula matriz de correlación entre variables.
        
        Args:
            df: DataFrame con variables numéricas
            method: 'pearson', 'spearman', 'kendall'
            
        Returns:
            DataFrame con matriz de correlación
        """
        pass

    @abstractmethod
    def outlier_detection(self, data: np.ndarray, method: str = 'z_score') -> Tuple[np.ndarray, np.ndarray]:
        """
        Detecta valores atípicos (outliers).
        
        Args:
            data: Array con datos numéricos
            threshold: Umbral para detección (default: 3 desv. estándar)
            method: 'zscore', 'iqr', 'isolation_forest'
            
        Returns:
            Tuple (outliers_indices, outliers_values)
        """
        pass

    @abstractmethod
    def normality_test(self, data: np.ndarray, alpha: float = 0.05) -> Dict[str, any]:
        """
        Prueba de normalidad (Shapiro-Wilk, Kolmogorov-Smirnov).
        
        Args:
            data: Array con datos
            alpha: Nivel de significancia
            
        Returns:
            Dict con statistic, p_value, is_normal
        """
        pass

    @abstractmethod
    def hypothesis_testing(self, sample1: np.ndarray, sample2: np.ndarray, test_type: str = 't_test') -> Dict[str, any]:
        """
        Realiza pruebas de hipótesis entre dos muestras.
        
        Args:
            sample1: Primera muestra
            sample2: Segunda muestra
            test_type: 't_test', 'mann_whitney', 'wilcoxon'
            
        Returns:
            Dict con statistic, p_value, reject_null
        """
        pass

    @abstractmethod
    def time_series_decomposition(self, df: pd.DataFrame, freq: str = 'M', model: str = 'additive') -> Dict[str, pd.Series]:
        """
        Descompone series temporales en componentes.
        
        Args:
            df: DataFrame con serie temporal (debe tener índice datetime)
            freq: Frecuencia ('D', 'W', 'M', 'Q', 'Y')
            model: 'additive' o 'multiplicative'
            
        Returns:
            Dict con: trend, seasonal, residual, observed
        """
        pass

    @abstractmethod
    def moving_average(self, data: np.ndarray, window: int = 7, center: bool = False) -> np.ndarray:
        """
        Calcula media móvil (suavizado).
        
        Args:
            data: Array con datos
            window: Tamaño de la ventana
            center: Si True, centra la ventana
            
        Returns:
            Array con media móvil
        """
        pass

    @abstractmethod
    def exponential_smoothing(self, data: np.ndarray, alpha: float = 0.3) -> np.ndarray:
        """
        Suavizado exponencial simple.
        
        Args:
            data: Array con datos
            alpha: Factor de suavizado (0 < alpha < 1)
            
        Returns:
            Array con datos suavizados
        """
        pass

    @abstractmethod
    def linear_regression(self, X: np.ndarray, y: np.ndarray) -> Dict[str, any]:
        """
        Regresión lineal simple o múltiple.
        
        Args:
            X: Variables independientes (features)
            y: Variable dependiente (target)
            
        Returns:
            Dict con: coefficients, intercept, r_squared, predictions
        """
        pass

    @abstractmethod
    def confidence_interval(self, data: np.ndarray, confidence: float = 0.95) -> Tuple[float, float]:
        """
        Calcula intervalo de confianza para la media.
        
        Args:
            data: Array con datos
            confidence: Nivel de confianza (default: 95%)
            
        Returns:
            Tuple (lower_bound, upper_bound)
        """
        pass

    @abstractmethod
    def variance_analysis(self, *groups: np.ndarray) -> Dict[str, any]:
        """
        ANOVA - Análisis de varianza entre grupos.
        
        Args:
            groups: Arrays con datos de cada grupo
            
        Returns:
            Dict con: f_statistic, p_value, reject_null
        """
        pass

    @abstractmethod
    def distribution_fitting(self, data: np.ndarray, dist_type: DistributionType) -> Dict[str, any]:
        """
        Ajusta datos a una distribución estadística.
        
        Args:
            data: Array con datos
            dist_type: Tipo de distribución (Enum)
            
        Returns:
            Dict con parámetros de la distribución y bondad de ajuste
        """
        pass

    @abstractmethod
    def monte_carlo_simulation(self, mean: float, std: float, simulations: int = 10000) -> np.ndarray:
        """
        Simulación Monte Carlo para pronósticos.
        
        Args:
            mean: Media de la distribución
            std: Desviación estándar
            simulations: Número de simulaciones
            
        Returns:
            Array con resultados de simulaciones
        """
        pass

    @abstractmethod
    def bootstrap_sampling(self, data: np.ndarray, n_iterations: int = 1000, sample_size: Optional[int] = None) -> np.ndarray:
        """
        Bootstrap resampling para estimación de estadísticos.
        
        Args:
            data: Array con datos originales
            n_iterations: Número de muestras bootstrap
            sample_size: Tamaño de cada muestra (default: len(data))
            
        Returns:
            Array con estadísticos de cada iteración
        """
        pass

    @abstractmethod
    def clustering_analysis(self, df: pd.DataFrame, n_clusters: int = 3, method: str = 'kmeans') -> pd.DataFrame:
        """
        Análisis de clustering (agrupamiento).
        
        Args:
            df: DataFrame con features para clustering
            n_clusters: Número de clusters
            method: 'kmeans', 'hierarchical', 'dbscan'
            
        Returns:
            DataFrame con cluster asignado a cada observación
        """
        pass

    @abstractmethod
    def principal_component_analysis(self, df: pd.DataFrame, n_components: int = 2) -> Dict[str, any]:
        """
        PCA - Reducción de dimensionalidad.
        
        Args:
            df: DataFrame con variables numéricas
            n_components: Número de componentes principales
            
        Returns:
            Dict con: transformed_data, explained_variance, components
        """
        pass

    @abstractmethod
    def calculate_percentiles(self, data: np.ndarray, percentiles: List[float]) -> Dict[float, float]:
        """
        Calcula percentiles específicos.
        
        Args:
            data: Array con datos
            percentiles: Lista de percentiles a calcular [25, 50, 75, 90, 95, 99]
            
        Returns:
            Dict con percentil: valor
        """
        pass

    @abstractmethod
    def standarize_data(self, data: np.ndarray) -> np.ndarray:
        """
        Estandariza datos (Z-score normalization).
        
        Args:
            data: Array con datos
            
        Returns:
            Array estandarizado (mean=0, std=1)
        """
        pass

    @abstractmethod
    def normalize_data(self, data: np.ndarray, method: str = 'minmax') -> np.ndarray:
        """
        Normaliza datos a un rango específico.
        
        Args:
            data: Array con datos
            method: 'minmax' (0-1) o 'robust' (usa mediana y IQR)
            
        Returns:
            Array normalizado
        """
        pass