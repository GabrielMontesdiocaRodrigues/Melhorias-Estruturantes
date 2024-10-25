import os

from pydantic import BaseSettings


class DefaultSettings(BaseSettings):
    URL_SEFAZ_GO: str = os.getenv('URL_SEFAZ_GO',
                                  "http://appasp.sefaz.go.gov.br/Sintegra/Consulta/default.html")

    REDIS_HOST: str = os.getenv("REDIS_HOST",
                                "redishost")


class Environment(DefaultSettings):
    pass


def environment():
    return Environment()
