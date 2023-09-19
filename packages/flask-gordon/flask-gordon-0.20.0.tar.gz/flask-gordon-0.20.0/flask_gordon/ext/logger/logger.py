"""
Description
===========

Initialize loggers for Celery workers.

Usage
=====

Initializing a Celery application
---------------------------------

Sample :file:`<PACKAGE_NAME>/__init__.py` file:

.. code-block:: python

  #!/usr/bin/env python3

  from flask import Flask
  from flask_gordon.ext import CeleryExt

  app = Flask(__name__)
  celery = CeleryExt().init_app(app)
  celery = LoggerExt().init_app(celery)

Classes
=======

.. autoclass:: CeleryExt
   :members: init_app

"""
from .. import functions


class LoggerExt:
    def __init__(self, app=None):
        """
        Parameters
        ----------
        app:

            A Flask or Celery application.
        """
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Parameters
        ----------
        app:

            A Flask or Celery application.
        """
        # Is this a flask or celery application?
        app_class = functions.get_app_class(app)
        if app_class == "flask":
            return self.init_flask_app(app)

        if app_class == "celery":
            return self.init_celery_app(app)

        raise NotImplementedError("Could not determine if app is Flask or Celery")

    def init_flask_app(self, app):
        return app

    def init_celery_app(self, app):
        # Defaults:
        #   https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-worker_log_format
        #
        # We don't need to toy around with the loggers, so we can just change the settings
        app.conf.update(
            {
                "worker_log_format": "[%(asctime)s] [%(levelname)s] [%(processName)s] %(message)s",
                "worker_task_log_format": "[%(asctime)s] [%(levelname)s] [%(processName)s] [%(task_name)s] [%(task_id)s] %(message)s",
                "worker_redirect_stdouts_level": "DEBUG",
            },
        )
        return app
