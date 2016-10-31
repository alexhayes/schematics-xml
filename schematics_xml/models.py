# -*- coding: utf-8 -*-
"""
    schematics_xml.models
    ~~~~~~~~~~~~~~~~~~~~~

    Base models that provide to/from XML methods.
"""

import collections
import numbers

import lxml.builder
import lxml.etree
from schematics import Model
from schematics.types import BaseType, ModelType, CompoundType
from schematics.types.base import MultilingualStringType
from schematics.types.compound import PolyModelType
from xmltodict import parse


class XMLModel(Model):
    """
    A model that can convert it's fields to and from XML.
    """
    @property
    def xml_root(self):
        return type(self).__name__.lower()

    def to_xml(self, *, role: str=None, app_data: dict=None, **kwargs) -> str:
        """
        Return a string of XML that represents this model.

        Currently all arguments are passed through to schematics.Model.to_primitive.

        :param role: schematics Model to_primitive role parameter.
        :param app_data: schematics Model to_primitive app_data parameter.
        :param kwargs: schematics Model to_primitive kwargs parameter.
        """
        primitive = self.to_primitive(role=role, app_data=app_data, **kwargs)
        root = self.primitive_to_xml(primitive)
        return lxml.etree.tostring(  # pylint: disable=no-member
            root,
            pretty_print=True,
            xml_declaration=True,
            encoding='ISO-8859-1'
        )

    def primitive_to_xml(self, primitive: dict, parent: 'lxml.etree._Element'=None):
        element_maker = lxml.builder.ElementMaker()

        if parent is None:
            parent = getattr(element_maker, self.xml_root)()

        for key, value in primitive.items():
            self.primitive_value_to_xml(key, parent, value)

        return parent

    def primitive_value_to_xml(self, key, parent, value):
        element_maker = lxml.builder.ElementMaker()

        if isinstance(value, bool):
            parent.append(getattr(element_maker, key)('1' if value else '0'))

        elif isinstance(value, numbers.Number) or isinstance(value, str):
            parent.append(getattr(element_maker, key)(str(value)))

        elif value is None:
            parent.append(getattr(element_maker, key)(''))

        elif isinstance(value, dict):
            _parent = getattr(element_maker, key)()
            parent.append(self.primitive_to_xml(value, _parent))

        elif isinstance(value, collections.abc.Iterable):
            for _value in value:
                self.primitive_value_to_xml(key, parent, _value)

        else:
            raise TypeError('Unsupported data type: %s (%s)' % (value, type(value).__name__))

    @classmethod
    def from_xml(cls, xml: str) -> Model:
        """
        Convert XML into a model.

        :param xml: A string of XML that represents this Model.
        """
        if model_has_field_type(MultilingualStringType, cls):
            raise NotImplementedError("Field type 'MultilingualStringType' is not supported.")
        primitive = parse(xml)
        if len(primitive) != 1:
            raise NotImplementedError
        for _, raw_data in primitive.items():
            return cls(raw_data=raw_data)


def model_has_field_type(needle: BaseType, haystack: Model) -> bool:
    """
    Return True if haystack contains a field of type needle.

    Iterates over all fields (and into field if appropriate) and searches for field type *needle* in model
    *haystack*.

    :param needle: A schematics field class to search for.
    :param haystack: A schematics model to search within.
    """
    for _, field in haystack._field_list:  # pylint: disable=protected-access
        if field_has_type(needle, field):
            return True
    return False


def field_has_type(needle: BaseType, field: BaseType) -> bool:  # pylint: disable=too-many-return-statements, too-many-branches
    """
    Return True if field haystack contains a field of type needle.

    :param needle: A schematics field class to search for.
    :param haystack: An instance of a schematics field within a model.
    """
    if isinstance(field, needle):
        return True

    elif isinstance(field, ModelType):
        if model_has_field_type(needle, field.model_class):
            return True

    elif isinstance(field, PolyModelType):
        if needle in [type(obj) for obj in field.model_classes]:
            return True

        for obj in [obj for obj in field.model_classes if isinstance(obj, ModelType)]:
            if model_has_field_type(needle, obj.model_class):
                return True

    elif isinstance(field, CompoundType):
        if needle == type(field.field):
            return True

        try:
            if needle == field.model_class:
                return True

        except AttributeError:
            pass

        else:
            if model_has_field_type(needle, field.model_class):
                return True

        if field_has_type(needle, field.field):
            return True

    return False
