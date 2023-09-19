"""
Description
===========

Initialize a Celery worker or Celery beat for the Flask application.

A weak reference to the Flask application will be added the Celery application.


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

  # Assert references in both directions:
  assert app is celery.app()
  assert app.extensions["celery"] is celery


Sample Celery shared task
-------------------------

.. code-block:: python

  from celery import shared_task
  from flask import current_app

  def call_example(*args, **kwargs):
      example_task.s(*args, **kwargs).apply_async()

  @shared_task()
  def example_task(*args, **kwargs):
      print(current_app)


Starting a Celery worker
-------------------------

Sample :file:`bin/celery-worker` file:

.. code-block:: bash

 #!/usr/bin/env bash

 exec celery -A <PACKAGE_NAME>.celery worker

Classes
=======

.. autoclass:: CeleryExt
   :members: init_app

"""
import contextlib
import typing as t
import weakref
from datetime import datetime

HAS_CELERY = False
with contextlib.suppress(ImportError):
    from celery import Celery, Task

    HAS_CELERY = True


# https://github.com/celery/celery/issues/4400#issuecomment-393390339
class LocalCelery(Celery):
    def now(self):
        """
        Return the current time and date as a datetime.
        """
        return datetime.now(self.timezone)


class CeleryExt:
    def __init__(self):
        if not HAS_CELERY:
            raise NotImplementedError("CeleryExt requires celery or celery[redis] package")

    def init_app(self, app: "Flask", **kwargs):
        """
        Parameters
        ----------
        app: FlaskApp

            A Flask application.

        kwargs:

            Keyword named arguments.

        Returns
        -------
        object:
            A Celery application
        """

        # pylint: disable=abstract-method
        class FlaskTask(Task):
            def __call__(self, *args: object, **kwargs: t.Dict[str, t.Any]) -> object:
                with app.app_context():
                    return self.run(*args, **kwargs)

        if "task_cls" not in kwargs:
            kwargs["task_cls"] = FlaskTask

        # pylint: disable=attribute-defined-outside-init
        celery_app = LocalCelery(app.name, **kwargs)
        celery_app.set_default()

        # Add a weak reference on celery_app to the Flask application
        celery_app.app = weakref.ref(app)

        app.extensions["celery"] = celery_app

        return celery_app
