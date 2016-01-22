# -*- coding: utf-8 -*-
from django.apps import AppConfig


class StudentsAppConfig(AppConfig):
    name = 'students'
    verbose_name = 'База даних студентів'

    def ready(self):
        from students import signals