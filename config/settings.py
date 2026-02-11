from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Configuración de la aplicación"""
    
    # Database
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_NAME: str = "sales_analytics"
    DB_USER: str = "sales_user"
    DB_PASSWORD: str = "sales_pass123"
    
    # Application
    APP_ENV: str = "development"
    DEBUG: bool = True
    
    # Power BI
    POWERBI_EXPORT_PATH: str = "./data/exports/"
    
    class Config:
        env_file = ".env"
        case_sensitive = True
    
    @property
    def database_url(self) -> str:
        """Retorna la URL de conexión a la base de datos"""
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()