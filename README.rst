========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        |
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/sys/badge/?style=flat
    :target: https://readthedocs.org/projects/sys
    :alt: Documentation Status

.. |version| image:: https://img.shields.io/pypi/v/sys.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/sys

.. |downloads| image:: https://img.shields.io/pypi/dm/sys.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/sys

.. |wheel| image:: https://img.shields.io/pypi/wheel/sys.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/sys

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/sys.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/sys

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/sys.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/sys


.. end-badges

A test package

* Free software: BSD license

Installation
============

::

    pip install sys

Documentation
=============

https://sys.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
