import os
import time

from django.apps import AppConfig


class ApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'application'

    # def ready(self):
    #     from jobs import updater
    #     updater.start()


# from django.apps import AppConfig


# class MainConfig(AppConfig):
#     name = 'main'

#     def ready(self):
#     	from jobs import updater
#     	updater.start()

