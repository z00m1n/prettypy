########
prettypy
########

**Python Pretty Printer**

========
Abstract
========

The **prettypy** package is yet another 'pretty printer'.

It is meant to:

* have a **readable and consistent** output.
    - Nested levels are indented. (the indentation string is configurable (4 spaces by default))
    - The sequences and the mapping keys are sorted. (can be disabled)
    - Mapping keys are padded. (so the values are aligned)
    - The data types may be shown. (disabled by default)

* be **simple** to use.
    - Only one class is required.
    - A convinience function is also provided.

* be **extensible**
    - If the provided support for standard types doesn't suit your need, it's easy to modify it.
    - Any object can easaly be supported.

* be able to handle **large data structure**.
    - Sequences, mappings, strings and multi-lines can be truncated as needed.
    - Mapping items can be omitted based on regex.

=====
Usage
=====

There are 2 basic ways to use prettypy: With the **Printer** class or the **dump** function.

------------------
The Printer class:
------------------

.. code-block:: python

    from prettypy import Printer

    p = Printer()
    p.print(some_data_structure)

The **Printer.print** method sends a formatted representation of its argument to a file-like destination (stdout by default). 

------------------
The dump function:
------------------

.. code-block:: python

    from prettypy import dump

    dump(some_data_structure)

The **dump** function uses the **Printer** class to 'dump' its argument on stdout as well as to a file ('prettypy.dump' by default).

==================
Data Types support
==================

There are 2 ways for an object to be "printable" / "dumpable":

-------------------
The Formatter class
-------------------

The **Printer** class needs one **Formatter** for each supported data type (exept for string). 

A set of default **Formatter** is provided by the formatters module for Python's builtin types and should be good enough for most purposes.  

These formatters can be modified or extended at will to support new types or modify the output for existing ones. 

--------------------
The __print__ method
--------------------

Any object can become 'printable' by implementing the **__print__** method which will call the Printer's methods in appropriate ways.

============
Installation
============

.. code-block:: shell 

    $ pip install prettypy
