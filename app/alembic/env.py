from __future__ import with_statement

import os
import sys

from db.base import Base
from db.session import docker_pg_engine, local_pg_engine, remote_pg_engine

from alembic import context

parent_dir = os.path.abspath(os.getcwd())
sys.path.append(parent_dir)
config = context.config


class Migrator:
    def __init__(self, engine, target_metadata):
        self.engine = engine
        self.target_metadata = target_metadata

    def migrate(self):
        connectable = config.attributes.get("connection", None)
        if connectable is None:
            connectable = self.engine.connect()
        context.configure(
            connection=connectable,
            target_metadata=self.target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            self.prepare_migration_context()
            context.run_migrations()

    def prepare_migration_context(self):
        pass


class PostgresMigrator(Migrator):
    pass

def run_migrations_online() -> None:
    if config.config_ini_section == "postgres":
        migrator = PostgresMigrator(docker_pg_engine, Base.metadata)

    migrator.migrate()


run_migrations_online()
