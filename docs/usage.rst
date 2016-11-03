=====
Usage
=====

Simply inherit ``XMLModel``.

.. code-block:: python

    from schematics_xml import XMLModel

    class Person(XMLModel):
        name = StringType()

    john = Person(dict(name='John'))

    xml = john.to_xml()

XML now contains;

.. code-block:: xml

    <?xml version='1.0' encoding='UTF-8'?>
    <person>
      <name>John</name>
    </person>

And back the other way;

.. code-block:: python

    john = Person.from_xml(xml)


Root Node
---------

To set the root node simply define class property ``xml_root``, as follows;

.. code-block:: python

    from schematics_xml import XMLModel

    class Animal(XMLModel):
        kind = StringType()

        @property
        def xml_root(self):
            return self.kind

    garfield = Animal(dict(kind='cat'))

    xml = garfield.to_xml()

XML now contains;

.. code-block:: xml

    <?xml version='1.0' encoding='UTF-8'?>
    <cat>
      <kind>cat</kind>
    </cat>


Encoding
--------

By default the encoding returned :py:meth:`.XMLModel.to_xml` is `UTF-8` however
this can be changed either by setting the `xml_encoding` attribute on the model
or by setting the `encoding` kwarg when calling :py:meth:`.XMLModel.to_xml`.

.. code-block:: python

    from schematics_xml import XMLModel

    class Animal(XMLModel):
        xml_encoding = 'UTF-8'
        kind = StringType()

    garfield = Animal(dict(kind='cat'))

    xml = garfield.to_xml()

XML now contains;

.. code-block:: xml

    <?xml version='1.0' encoding='UTF-8'?>
    <cat>
      <animal>cat</animal>
    </cat>
