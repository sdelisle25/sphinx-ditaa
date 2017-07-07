Sphinx contribution Ditaa
#########################

Simple Ditaa builder for sphinx, for python 3. 

Requirements
============

Sphinx Ditaa requires Python_ 3.5, native dependency Ditaa_ and python packages. 

* Python_ >=3.5

* pip3_ pip >=9.0.0

* Sphinx_ >=1.0.7

* Ditaa_  >=0.8

Installation
============

* Install native dependency, installation depends on your OS and/or your distribution, example for Debian:

.. code-block:: shell
   
      sudo apt-get install ditaa
      sudo apt-get install python3
      sudo apt-get install python3-pip

.. code-block:: shell

      sudo pip3 install sphinx


* Install Sphinx contribution:

.. code:: shell

   pip3 install .


Using the Ditaa with Sphinx
===========================

Add `sphinxcontrib.ditaa` to the `extensions` list in `conf.py`:

.. code-block:: python

    extensions = [
       ... other extensions here ...
       'sphinxcontrib.ditaa'
       ]

.. code-block:: python

      ditaa = 'ditaa'    # ditaa command
      ditaa_args = ''    # custom ditaa args

Write ditaa code in `rst` documentation:

::

    .. ditaa::

      +--------+   +-------+    +-------+
      |        | --+ ditaa +--> |       |
      |  Text  |   +-------+    |diagram|
      |Document|   |!magic!|    |       |
      |     {d}|   |       |    |       |
      +---+----+   +-------+    +-------+
          :                         ^
          |       Lots of work      |
          +-------------------------+

    
.. _Python: https://www.python.org/
.. _pip3: https://pypi.python.org/pypi/pip/
.. _Ditaa: http://ditaa.sourceforge.net/
.. _Sphinx: https://pypi.python.org/pypi/Sphinx
