=============
faker-file-qt
=============
PyQT UI for `faker-file`_.

.. image:: https://img.shields.io/pypi/v/faker-file-qt.svg
   :target: https://pypi.python.org/pypi/faker-file-qt
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/faker-file-qt.svg
    :target: https://pypi.python.org/pypi/faker-file-qt/
    :alt: Supported Python versions

.. image:: https://github.com/barseghyanartur/faker-file-qt/workflows/test/badge.svg?branch=main
   :target: https://github.com/barseghyanartur/faker-file-qt/actions
   :alt: Build Status

.. image:: https://readthedocs.org/projects/faker-file-qt/badge/?version=latest
    :target: http://faker-file-qt.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/barseghyanartur/faker-file-qt/#License
   :alt: MIT

.. image:: https://coveralls.io/repos/github/barseghyanartur/faker-file-qt/badge.svg?branch=main&service=github
    :target: https://coveralls.io/github/barseghyanartur/faker-file-qt?branch=main
    :alt: Coverage

.. Internal references

.. _Read the Docs: http://faker-file-qt.readthedocs.io/

.. Related projects

.. _faker-file: https://github.com/barseghyanartur/faker-file/
.. _faker-file-api: https://github.com/barseghyanartur/faker-file-api
.. _faker-file-ui: https://github.com/barseghyanartur/faker-file-ui
.. _faker-file-wasm: https://github.com/barseghyanartur/faker-file-wasm

.. Demos

.. _REST API demo: https://faker-file-api.onrender.com/docs/
.. _UI frontend demo: https://faker-file-ui.vercel.app/
.. _WASM frontend demo: https://faker-file-wasm.vercel.app/

.. External references

.. _Apache Tika: https://tika.apache.org/
.. _Django: https://www.djangoproject.com/
.. _Faker: https://faker.readthedocs.io/
.. _Jinja2: https://jinja.palletsprojects.com/
.. _Pillow: https://pypi.org/project/Pillow/
.. _PyTorch: https://pytorch.org/
.. _WeasyPrint: https://pypi.org/project/weasyprint/
.. _azure-storage-blob: https://pypi.org/project/azure-storage-blob/
.. _boto3: https://pypi.org/project/boto3/
.. _edge-tts: https://pypi.org/project/edge-tts/
.. _factory_boy: https://factoryboy.readthedocs.io/
.. _gTTS: https://gtts.readthedocs.io/
.. _google-cloud-storage: https://pypi.org/project/google-cloud-storage/
.. _imgkit: https://pypi.org/project/imgkit/
.. _nlpaug: https://nlpaug.readthedocs.io/
.. _numpy: https://numpy.org/
.. _odfpy: https://pypi.org/project/odfpy/
.. _openpyxl: https://openpyxl.readthedocs.io/
.. _pandas: https://pandas.pydata.org/
.. _pdf2image: https://pypi.org/project/pdf2image/
.. _paramiko: http://paramiko.org/
.. _pathy: https://pypi.org/project/pathy/
.. _pdfkit: https://pypi.org/project/pdfkit/
.. _poppler: https://poppler.freedesktop.org/
.. _python-docx: https://python-docx.readthedocs.io/
.. _python-pptx: https://python-pptx.readthedocs.io/
.. _PyQT5: https://pypi.org/project/PyQt5/
.. _QDarkStyle: https://pypi.org/project/QDarkStyle/
.. _reportlab: https://pypi.org/project/reportlab/
.. _tablib: https://tablib.readthedocs.io/
.. _tika: https://pypi.org/project/tika/
.. _transformers: https://pypi.org/project/transformers/
.. _wkhtmltopdf: https://wkhtmltopdf.org/
.. _xml2epub: https://pypi.org/project/xml2epub/

Prerequisites
=============
- `faker-file`_ (``faker-file[common]``)
- `QDarkStyle`_
- `PyQT5`_

Documentation
=============
- Documentation is available on `Read the Docs`_.

Installation
============
Latest stable version from PyPI
-------------------------------
.. code-block:: sh

    pipx install faker-file-qt

Or development version from GitHub
----------------------------------

.. code-block:: sh

    pipx install https://github.com/barseghyanartur/faker-file-qt/archive/main.tar.gz

Install locally in development mode
-----------------------------------
.. code-block:: sh

    pip install -e .[dev]

Running
=======
.. code-block:: sh

    faker-file-qt

Testing
=======
Simply type:

.. code-block:: sh

    pytest -vrx

Or use tox:

.. code-block:: sh

    tox

Related projects
================
Check the demo(s):

- `REST API demo`_ (based on `faker-file-api`_ REST API)
- `UI frontend demo`_ (based on `faker-file-ui`_ UI frontend)
- `WASM frontend demo`_ (based on `faker-file-wasm`_ WASM frontend)

Writing documentation
=====================

Keep the following hierarchy.

.. code-block:: text

    =====
    title
    =====

    header
    ======

    sub-header
    ----------

    sub-sub-header
    ~~~~~~~~~~~~~~

    sub-sub-sub-header
    ^^^^^^^^^^^^^^^^^^

    sub-sub-sub-sub-header
    ++++++++++++++++++++++

    sub-sub-sub-sub-sub-header
    **************************

License
=======
MIT

Support
=======
For security issues contact me at the e-mail given in the `Author`_ section.

For overall issues, go to `GitHub <https://github.com/barseghyanartur/faker-file-qt/issues>`_.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
