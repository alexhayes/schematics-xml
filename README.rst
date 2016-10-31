==============
schematics-xml
==============

Python schematics_ models for converting to and from XML.

.. image:: https://travis-ci.org/alexhayes/schematics-xml.png?branch=master
    :target: https://travis-ci.org/alexhayes/schematics-xml
    :alt: Build Status

.. image:: https://landscape.io/github/alexhayes/schematics-xml/master/landscape.png
    :target: https://landscape.io/github/alexhayes/schematics-xml/
    :alt: Code Health

.. image:: https://codecov.io/github/alexhayes/schematics-xml/coverage.svg?branch=master
    :target: https://codecov.io/github/alexhayes/schematics-xml?branch=master
    :alt: Code Coverage

.. image:: https://readthedocs.org/projects/schematics-xml/badge/
    :target: http://schematics-xml.readthedocs.org/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/schematics-xml.svg
    :target: https://pypi.python.org/pypi/schematics-xml
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/schematics-xml.svg
    :target: https://pypi.python.org/pypi/schematics-xml/
    :alt: Supported Python versions


Install
-------

.. code-block:: bash

    pip install schematics-xml


Example Usage
-------------

Simply inherit XMLModel.

.. code-block:: python

    from schematics_xml import XMLModel

    class Person(XMLModel):
        name = StringType()

    john = Person(dict(name='John'))

    xml = john.to_xml()

XML now contains;

.. code-block:: xml

    <?xml version='1.0' encoding='ISO-8859-1'?>
    <person>
      <name>John</name>
    </person>

And back the other way;

.. code-block:: python

    john = Person.from_xml(xml)


Author
------

Alex Hayes <alex@alution.com>

.. _schematics: https://schematics.readthedocs.io
