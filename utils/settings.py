# External modules
from dotenv import find_dotenv
from pydantic import BaseSettings, Field


class GlobalSettings(BaseSettings):

    SITE: str = Field(..., env='SITE')
    EMAIL: str = Field(..., env='EMAIL')
    PASSWORD: str = Field(..., env='PASSWORD')
    FALLOW_PEOPLE: int = Field(..., env='FALLOW_PEOPLE')
    DELETE_MESSAGE: int = Field(..., env='DELETE_MESSAGE')
    UNFALLOW_PEOPLE: int = Field(..., env='UNFALLOW_PEOPLE')

    class Config:

        env_file: str = find_dotenv('.env')


settings = GlobalSettings()
