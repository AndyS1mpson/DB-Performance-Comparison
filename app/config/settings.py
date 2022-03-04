from typing import Any, Mapping, Optional

from pydantic import BaseConfig, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    DOCKER_POSTGRES_USER: str
    DOCKER_POSTGRES_PASSWORD: str = ""
    DOCKER_POSTGRES_DB: str
    DOCKER_POSTGRES_HOST: str
    DOCKER_POSTGRES_PORT: int = 5432

    # LOCAL_POSTGRES_USER: str
    # LOCAL_POSTGRES_PASSWORD: str = ""
    # LOCAL_POSTGRES_DB: str
    # LOCAL_POSTGRES_HOST: str
    # LOCAL_POSTGRES_PORT: int = 5432

    

    DOCKER_POSTGRES_URL: str = ""
    #LOCAL_POSTGRES_URL: str = ""


    @validator("DOCKER_POSTGRES_URL", pre=True)
    def assemble_docker_postgres_db_url(
        cls, v: Optional[str], values: Mapping[str, Any]
    ) -> Any:
        if v and isinstance(v, str):
            return v
        
        return str(
            PostgresDsn.build(
                scheme="postgresql",
                user=values["DOCKER_POSTGRES_USER"],
                password=values["DOCKER_POSTGRES_PASSWORD"],
                host=values["DOCKER_POSTGRES_HOST"],
                port=str(values["DOCKER_POSTGRES_PORT"]),
                path=f'/{values["DOCKER_POSTGRES_DB"]}',
            )
        )

    # @validator("LOCAL_POSTGRES_URL", pre=True)
    # def assemble_local_postgres_db_url(
    #     cls, v: Optional[str], values: Mapping[str, Any]
    # ) -> Any:
    #     if v and isinstance(v, str):
    #         return v
        
    #     return str(
    #         PostgresDsn.build(
    #             scheme="postgresql",
    #             user=values["LOCAL_POSTGRES_USER"],
    #             password=values["LOCAL_POSTGRES_PASSWORD"],
    #             host=values["LOCAL_POSTGRES_HOST"],
    #             port=str(values["LOCAL_POSTGRES_PORT"]),
    #             path=f'/{values["LOCAL_POSTGRES_DB"]}',
    #         )
    #     )

settings = Settings()

