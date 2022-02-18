from dynaconf import Dynaconf
import os

settings = Dynaconf(
    settings_files=['settings.local.yaml', 'settings.dev.yaml', 'settings.prod.yaml'],
    environments=True
)
