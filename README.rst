Sphinx contribution Ditaa
#########################

Simple Ditaa builder for sphinx, for python 3. 

Installation
------------

.. code:: shell

    pip3 install .


Install [ditaa command](http://ditaa.sourceforge.net/)

Using the Ditaa with Sphinx
---------------------------

Add `sphinxcontrib.ditaa` to the `extensions` list in `conf.py`:

.. code:: python

    extensions = [
       ... other extensions here ...
       'sphinxcontrib.ditaa'
       ]

# ditaa command. should be install ditaa
ditaa = 'ditaa'    # ditaa command
# ditaa_args = ''  # custom ditaa args


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
