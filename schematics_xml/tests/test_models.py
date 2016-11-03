# -*- coding: utf-8 -*-
"""
    schematics_xml.tests.test_models
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for XMLModel
"""
from datetime import date
from datetime import datetime
from decimal import Decimal

import pytest
from schematics import Model
from schematics.types import StringType, IntType, FloatType, DecimalType, ModelType, DictType, LongType, UUIDType, \
    MD5Type, SHA1Type, BooleanType, DateType, DateTimeType, UTCDateTimeType, TimestampType, GeoPointType, \
    MultilingualStringType, ListType, IPv4Type, IPv6Type, URLType, EmailType, UnionType, PolyModelType

from schematics_xml.models import XMLModel, model_has_field_type, ensure_lists_in_model


class TestUUIDType:

    class Person(XMLModel):
        pk = UUIDType()  # pylint: disable=invalid-name

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<person>\n'
        b'  <pk>32c5548e-ddee-4b23-a06e-f387a15bcac9</pk>\n'
        b'</person>\n'
    )

    def test_to_xml(self):
        john = self.Person(dict(pk='32c5548e-ddee-4b23-a06e-f387a15bcac9'))
        actual = john.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        john = self.Person.from_xml(self.xml)
        assert isinstance(john, self.Person)
        assert str(john.pk) == '32c5548e-ddee-4b23-a06e-f387a15bcac9'


class TestStringType:

    class Person(XMLModel):
        name = StringType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<person>\n'
        b'  <name>John</name>\n'
        b'</person>\n'
    )

    def test_to_xml(self):
        john = self.Person(dict(name='John'))
        actual = john.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        john = self.Person.from_xml(self.xml)
        assert isinstance(john, self.Person)
        assert john.name == 'John'


class TestIntType:

    class Person(XMLModel):
        age = IntType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<person>\n'
        b'  <age>18</age>\n'
        b'</person>\n'
    )

    def test_to_xml(self):
        john = self.Person(dict(age=18))
        actual = john.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        john = self.Person.from_xml(self.xml)
        assert isinstance(john, self.Person)
        assert john.age == 18


class TestLongType:

    class Person(XMLModel):
        pk = LongType()  # pylint: disable=invalid-name

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<person>\n'
        b'  <pk>1832932875982759827298</pk>\n'
        b'</person>\n'
    )

    def test_to_xml(self):
        john = self.Person(dict(pk=1832932875982759827298))
        actual = john.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        john = self.Person.from_xml(self.xml)
        assert isinstance(john, self.Person)
        assert john.pk == 1832932875982759827298


class TestFloatType:

    class Person(XMLModel):
        height = FloatType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<person>\n'
        b'  <height>12.2</height>\n'
        b'</person>\n'
    )

    def test_to_xml(self):
        john = self.Person(dict(height=12.2))
        actual = john.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        john = self.Person.from_xml(self.xml)
        assert isinstance(john, self.Person)
        assert john.height == 12.2


class TestDecimalType:

    class Person(XMLModel):
        height = DecimalType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<person>\n'
        b'  <height>12.2</height>\n'
        b'</person>\n'
    )

    def test_to_xml(self):
        john = self.Person(dict(height=12.2))
        actual = john.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        john = self.Person.from_xml(self.xml)
        assert isinstance(john, self.Person)
        assert john.height == Decimal('12.2')


class TestMD5Type:

    class File(XMLModel):
        md5 = MD5Type()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<file>\n'
        b'  <md5>efe2d5fd46824508b8a0082c8279bbae</md5>\n'
        b'</file>\n'
    )

    def test_to_xml(self):
        file = self.File(dict(md5='efe2d5fd46824508b8a0082c8279bbae'))
        actual = file.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        file = self.File.from_xml(self.xml)
        assert isinstance(file, self.File)
        assert file.md5 == 'efe2d5fd46824508b8a0082c8279bbae'


class TestSHA1Type:

    class File(XMLModel):
        sha1 = SHA1Type()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<file>\n'
        b'  <sha1>2eE84Ef6301cCEc5926C4ADBF3E9B51c6c42ade3</sha1>\n'
        b'</file>\n'
    )

    def test_to_xml(self):
        file = self.File(dict(sha1='2eE84Ef6301cCEc5926C4ADBF3E9B51c6c42ade3'))
        actual = file.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        file = self.File.from_xml(self.xml)
        assert isinstance(file, self.File)
        assert file.sha1 == '2eE84Ef6301cCEc5926C4ADBF3E9B51c6c42ade3'


class TestBooleanType:

    class User(XMLModel):
        active = BooleanType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<user>\n'
        b'  <active>1</active>\n'
        b'</user>\n'
    )

    def test_to_xml(self):
        user = self.User(dict(active=True))
        actual = user.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        file = self.User.from_xml(self.xml)
        assert isinstance(file, self.User)
        assert file.active is True


class TestDateType:

    class User(XMLModel):
        birthdate = DateType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<user>\n'
        b'  <birthdate>2016-01-01</birthdate>\n'
        b'</user>\n'
    )

    def test_to_xml(self):
        user = self.User(dict(birthdate=date(2016, 1, 1)))
        actual = user.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        user = self.User.from_xml(self.xml)
        assert isinstance(user, self.User)
        assert user.birthdate == date(2016, 1, 1)


class TestDateTimeType:

    class User(XMLModel):
        created = DateTimeType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<user>\n'
        b'  <created>2016-01-01T08:30:32.000000</created>\n'
        b'</user>\n'
    )

    def test_to_xml(self):
        user = self.User(dict(created=datetime(2016, 1, 1, 8, 30, 32)))
        actual = user.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        user = self.User.from_xml(self.xml)
        assert isinstance(user, self.User)
        assert user.created == datetime(2016, 1, 1, 8, 30, 32)


class TestUTCDateTimeType:

    class User(XMLModel):
        created = UTCDateTimeType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<user>\n'
        b'  <created>2016-01-01T08:30:32.000000Z</created>\n'
        b'</user>\n'
    )

    def test_to_xml(self):
        user = self.User(dict(created=datetime(2016, 1, 1, 8, 30, 32)))
        actual = user.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        user = self.User.from_xml(self.xml)
        assert isinstance(user, self.User)
        assert user.created == datetime(2016, 1, 1, 8, 30, 32)


class TestTimestampType:

    class User(XMLModel):
        created = TimestampType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<user>\n'
        b'  <created>1451637032</created>\n'
        b'</user>\n'
    )

    def test_to_xml(self):
        user = self.User(dict(created=datetime(2016, 1, 1, 8, 30, 32, tzinfo=DateTimeType.UTC)))
        actual = user.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        user = self.User.from_xml(self.xml)

        assert isinstance(user, self.User)
        assert user.created == datetime(2016, 1, 1, 8, 30, 32, tzinfo=DateTimeType.UTC)


class TestGeoPointType:

    class Place(XMLModel):
        point = GeoPointType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<place>\n'
        b'  <point>23</point>\n'
        b'  <point>170</point>\n'
        b'</place>\n'
    )

    def test_to_xml(self):
        place = self.Place(dict(point=(23, 170)))
        actual = place.to_xml()
        assert actual == self.xml

    @pytest.mark.xfail(reason="Schematics should convert string types to numeric.")
    def test_from_xml(self):
        place = self.Place.from_xml(self.xml)
        assert isinstance(place, self.Place)
        assert place.point == (23, 170)


class TestMultilingualStringType:

    class Animal(XMLModel):
        text = MultilingualStringType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<animal>\n'
        b'  <text>serpent</text>\n'
        b'</animal>\n'
    )

    def test_to_xml(self):
        animal = self.Animal(dict(text={
            'en_US': 'snake',
            'fr_FR': 'serpent'
        }))
        actual = animal.to_xml(app_data=dict(locale='fr_FR'))
        assert actual == self.xml

    def test_from_xml(self):
        with pytest.raises(NotImplementedError):
            self.Animal.from_xml(self.xml)
            # MultilingualStringType is not two way

    def test_from_xml_nested_raises(self):
        """
        Test that from_xml raises NotImplementedError for a nested MultilingualStringType
        """
        class Parent(XMLModel):
            child = ModelType(self.Animal)

        xml = (
            b"<?xml version='1.0' encoding='UTF-8'?>\n"
            b'<parent>\n'
            b'  <child>\n'
            b'    <text>serpent</text>\n'
            b'  </child>\n'
            b'</parent>\n'
        )
        with pytest.raises(NotImplementedError):
            Parent.from_xml(xml)


# schematics Compound Types

class TestModelType:
    _person_cls = None

    class Pet(XMLModel):
        name = StringType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<person>\n'
        b'  <pet>\n'
        b'    <name>Garfield</name>\n'
        b'  </pet>\n'
        b'</person>\n'
    )

    @property
    def Person(self):  # pylint: disable=invalid-name
        if not self._person_cls:
            class Person(XMLModel):
                pet = ModelType(self.Pet)
            self._person_cls = Person
        return self._person_cls

    def test_to_xml(self):
        john = self.Person(dict(pet=dict(name='Garfield')))
        actual = john.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        person = self.Person.from_xml(self.xml)
        assert isinstance(person, self.Person)
        assert isinstance(person.pet, self.Pet)
        assert person.pet.name == 'Garfield'


class TestListTypeOfIntType:

    class Person(XMLModel):
        favorite_numbers = ListType(IntType())

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<person>\n'
        b'  <favorite_numbers>1</favorite_numbers>\n'
        b'  <favorite_numbers>2</favorite_numbers>\n'
        b'  <favorite_numbers>3</favorite_numbers>\n'
        b'</person>\n'
    )

    def test_to_xml(self):
        john = self.Person(dict(favorite_numbers=[1, 2, 3]))
        actual = john.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        person = self.Person.from_xml(self.xml)
        assert isinstance(person, self.Person)
        assert person.favorite_numbers == [1, 2, 3]


class TestListTypeOfModelMultipleItemsType:
    _person_cls = None

    class Color(XMLModel):
        name = StringType()

    @property
    def Person(self):  # pylint: disable=invalid-name
        if not self._person_cls:
            class Person(XMLModel):
                favorite_colors = ListType(ModelType(self.Color))
            self._person_cls = Person
        return self._person_cls

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<person>\n'
        b'  <favorite_colors>\n'
        b'    <name>red</name>\n'
        b'  </favorite_colors>\n'
        b'  <favorite_colors>\n'
        b'    <name>green</name>\n'
        b'  </favorite_colors>\n'
        b'  <favorite_colors>\n'
        b'    <name>blue</name>\n'
        b'  </favorite_colors>\n'
        b'</person>\n'
    )

    def test_to_xml(self):
        john = self.Person(dict(favorite_colors=[
            self.Color(dict(name='red')),
            self.Color(dict(name='green')),
            self.Color(dict(name='blue'))
        ]))
        actual = john.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        person = self.Person.from_xml(self.xml)
        assert isinstance(person, self.Person)
        assert len(person.favorite_colors) == 3
        assert person.favorite_colors[0].name == 'red'  # pylint: disable=unsubscriptable-object
        assert person.favorite_colors[1].name == 'green'  # pylint: disable=unsubscriptable-object
        assert person.favorite_colors[2].name == 'blue'  # pylint: disable=unsubscriptable-object


class TestListTypeOfModelSingleItemType:
    _person_cls = None

    class Color(XMLModel):
        name = StringType()

    @property
    def Person(self):  # pylint: disable=invalid-name
        if not self._person_cls:
            class Person(XMLModel):
                favorite_colors = ListType(ModelType(self.Color))
            self._person_cls = Person
        return self._person_cls

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<person>\n'
        b'  <favorite_colors>\n'
        b'    <name>red</name>\n'
        b'  </favorite_colors>\n'
        b'</person>\n'
    )

    def test_to_xml(self):
        john = self.Person(dict(favorite_colors=[
            self.Color(dict(name='red')),
        ]))
        actual = john.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        person = self.Person.from_xml(self.xml)
        assert isinstance(person, self.Person)
        assert len(person.favorite_colors) == 1
        assert person.favorite_colors[0].name == 'red'  # pylint: disable=unsubscriptable-object


class TestDictType:

    class Request(XMLModel):
        payload = DictType(StringType())

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<request>\n'
        b'  <payload>\n'
        b'    <foo>bar</foo>\n'
        b'  </payload>\n'
        b'</request>\n'
    )

    def test_to_xml(self):
        request = self.Request(dict(payload=dict(foo='bar')))
        actual = request.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        request = self.Request.from_xml(self.xml)
        assert request.payload == dict(foo='bar')


class TestPolyModelType:
    _recipe_item_cls = None

    class Eggs(XMLModel):
        yolks = IntType()

    class Sausage(XMLModel):
        meat = StringType()

    @property
    def RecipeItem(self):  # pylint: disable=invalid-name
        if not self._recipe_item_cls:
            class RecipeItem(XMLModel):
                item = PolyModelType([self.Eggs, self.Sausage])
            self._recipe_item_cls = RecipeItem
        return self._recipe_item_cls

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<recipeitem>\n'
        b'  <item>\n'
        b'    <yolks>2</yolks>\n'
        b'  </item>\n'
        b'</recipeitem>\n'
    )

    def test_to_xml(self):
        recipe_type = self.RecipeItem(dict(item=self.Eggs(dict(yolks=2))))
        actual = recipe_type.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        recipe_item = self.RecipeItem.from_xml(self.xml)
        assert isinstance(recipe_item, self.RecipeItem)
        assert isinstance(recipe_item.item, self.Eggs)
        assert recipe_item.item.yolks == 2  # pylint: disable=no-member


# Net tests
class TestIPv4Type:

    class Proxy(XMLModel):
        ip_address = IPv4Type()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<proxy>\n'
        b'  <ip_address>8.8.8.8</ip_address>\n'
        b'</proxy>\n'
    )

    def test_to_xml(self):
        proxy = self.Proxy(dict(ip_address='8.8.8.8'))
        actual = proxy.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        request = self.Proxy.from_xml(self.xml)
        assert request.ip_address == '8.8.8.8'


class TestIPv6Type:

    class Proxy(XMLModel):
        ip_address = IPv6Type()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<proxy>\n'
        b'  <ip_address>2001:db8:85a3::8a2e:370:7334</ip_address>\n'
        b'</proxy>\n'
    )

    def test_to_xml(self):
        proxy = self.Proxy(dict(ip_address='2001:db8:85a3::8a2e:370:7334'))
        actual = proxy.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        request = self.Proxy.from_xml(self.xml)
        assert request.ip_address == '2001:db8:85a3::8a2e:370:7334'


class TestURLType:

    class Site(XMLModel):
        url = URLType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<site>\n'
        b'  <url>https://github.com/alexhayes/schematics-xml</url>\n'
        b'</site>\n'
    )

    def test_to_xml(self):
        site = self.Site(dict(url='https://github.com/alexhayes/schematics-xml'))
        actual = site.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        request = self.Site.from_xml(self.xml)
        assert request.url == 'https://github.com/alexhayes/schematics-xml'


class TestEmailType:

    class User(XMLModel):
        email = EmailType()

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<user>\n'
        b'  <email>user@example.com</email>\n'
        b'</user>\n'
    )

    def test_to_xml(self):
        user = self.User(dict(email='user@example.com'))
        actual = user.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        request = self.User.from_xml(self.xml)
        assert request.email == 'user@example.com'


# UnionType tests

class TestUnionType:

    class Foo(XMLModel):
        union = UnionType([IntType, StringType])

    xml = (
        b"<?xml version='1.0' encoding='UTF-8'?>\n"
        b'<foo>\n'
        b'  <union>2</union>\n'
        b'</foo>\n'
    )

    def test_to_xml(self):
        obj = self.Foo(dict(union=2))
        actual = obj.to_xml()
        assert actual == self.xml

    def test_from_xml(self):
        obj = self.Foo.from_xml(self.xml)
        assert isinstance(obj, self.Foo)
        assert obj.union == 2


class TestHasFieldType:

    class TestModel(Model):
        a = StringType()  # pylint: disable=invalid-name
        b = IntType()  # pylint: disable=invalid-name
        c = FloatType()  # pylint: disable=invalid-name

    def test_shallow(self):
        assert model_has_field_type(StringType, self.TestModel) is True
        assert model_has_field_type(IntType, self.TestModel) is True
        assert model_has_field_type(FloatType, self.TestModel) is True
        assert model_has_field_type(Decimal, self.TestModel) is False

    def test_modeltype(self):
        class Parent(Model):
            child = ModelType(self.TestModel)

        assert model_has_field_type(ModelType, Parent) is True
        assert model_has_field_type(StringType, Parent) is True
        assert model_has_field_type(IntType, Parent) is True
        assert model_has_field_type(FloatType, Parent) is True
        assert model_has_field_type(Decimal, Parent) is False

    def test_listtype(self):
        class Container(Model):
            items = ListType(ModelType(self.TestModel))

        assert model_has_field_type(ListType, Container) is True
        assert model_has_field_type(ModelType, Container) is True
        assert model_has_field_type(StringType, Container) is True
        assert model_has_field_type(IntType, Container) is True
        assert model_has_field_type(FloatType, Container) is True
        assert model_has_field_type(Decimal, Container) is False

        class Container(Model):  # pylint: disable=function-redefined
            items = ListType(IntType())

        assert model_has_field_type(ListType, Container) is True
        assert model_has_field_type(ModelType, Container) is False
        assert model_has_field_type(StringType, Container) is False
        assert model_has_field_type(IntType, Container) is True
        assert model_has_field_type(FloatType, Container) is False
        assert model_has_field_type(Decimal, Container) is False

    def test_listtype_withlisttype(self):
        class Container(Model):
            items = ListType(ListType(ModelType(self.TestModel)))

        assert model_has_field_type(ListType, Container) is True
        assert model_has_field_type(ModelType, Container) is True
        assert model_has_field_type(StringType, Container) is True
        assert model_has_field_type(IntType, Container) is True
        assert model_has_field_type(FloatType, Container) is True
        assert model_has_field_type(Decimal, Container) is False

        class Container(Model):  # pylint: disable=function-redefined
            items = ListType(ListType(IntType()))

        assert model_has_field_type(ListType, Container) is True
        assert model_has_field_type(ModelType, Container) is False
        assert model_has_field_type(StringType, Container) is False
        assert model_has_field_type(IntType, Container) is True
        assert model_has_field_type(FloatType, Container) is False
        assert model_has_field_type(Decimal, Container) is False

    def test_dicttype(self):
        class Container(Model):
            items = DictType(ModelType(self.TestModel))

        assert model_has_field_type(DictType, Container) is True
        assert model_has_field_type(ModelType, Container) is True
        assert model_has_field_type(StringType, Container) is True
        assert model_has_field_type(IntType, Container) is True
        assert model_has_field_type(FloatType, Container) is True
        assert model_has_field_type(Decimal, Container) is False

        class Container(Model):  # pylint: disable=function-redefined
            items = DictType(IntType())

        assert model_has_field_type(DictType, Container) is True
        assert model_has_field_type(ModelType, Container) is False
        assert model_has_field_type(StringType, Container) is False
        assert model_has_field_type(IntType, Container) is True
        assert model_has_field_type(FloatType, Container) is False
        assert model_has_field_type(Decimal, Container) is False

    def test_polymodel_fieldtype(self):
        class Container(Model):
            item = PolyModelType([IntType(), StringType()])

        assert model_has_field_type(PolyModelType, Container) is True
        assert model_has_field_type(DictType, Container) is False
        assert model_has_field_type(ModelType, Container) is False
        assert model_has_field_type(StringType, Container) is True
        assert model_has_field_type(IntType, Container) is True
        assert model_has_field_type(FloatType, Container) is False
        assert model_has_field_type(Decimal, Container) is False

        class Container(Model):  # pylint: disable=function-redefined
            item = PolyModelType([ModelType(self.TestModel), DecimalType()])

        assert model_has_field_type(PolyModelType, Container) is True
        assert model_has_field_type(DictType, Container) is False
        assert model_has_field_type(ModelType, Container) is True
        assert model_has_field_type(StringType, Container) is True
        assert model_has_field_type(IntType, Container) is True
        assert model_has_field_type(FloatType, Container) is True
        assert model_has_field_type(DecimalType, Container) is True
        assert model_has_field_type(EmailType, Container) is False


class TestEnsureLists:
    """
    Tests for :py:func:`.ensure_lists_in_model`.
    """

    def test_model_with_listtype_of_inttype(self):  # pylint: disable=no-self-use,invalid-name
        """
        Ensure a model with a list type can be handled.
        """
        class TestModel(XMLModel):
            numbers = ListType(IntType())

        bad_data = dict(numbers=1)
        actual = ensure_lists_in_model(bad_data, TestModel)
        expected = dict(numbers=[1])
        # Assert bad data can be turned good
        assert actual == expected

        actual = ensure_lists_in_model(expected, TestModel)
        # Assert good data stays good
        assert actual == expected

    def test_model_with_listtype_of_modeltype(self):  # pylint: disable=no-self-use,invalid-name
        """
        Test that a model with a list type of models can correctly be
        """
        class Item(XMLModel):
            number = IntType()

        class TestModel(XMLModel):
            items = ListType(ModelType(Item))

        bad_data = dict(
            items=dict(number=1)
        )
        actual = ensure_lists_in_model(bad_data, TestModel)
        expected = dict(
            items=[
                dict(number=1)
            ]
        )
        # Assert bad data can be turned good
        assert actual == expected

        actual = ensure_lists_in_model(expected, TestModel)
        # Assert good data stays good
        assert actual == expected

    def test_model_with_listtype_of_modeltype_with_listtype_of_modeltype(self):  # pylint: disable=no-self-use,invalid-name
        """
        Test that a model with a list type of models are correctly converted.

        This test also tests the serialized_name functionality of schematics.
        """
        class Item(XMLModel):
            number = IntType()

        class Package(XMLModel):
            items = ListType(ModelType(Item), serialized_name='contents')

        class TestModel(XMLModel):
            packages = ListType(ModelType(Package), serialized_name='pkg')

        bad_data = dict(
            pkg=dict(
                contents=dict(number=1)
            )
        )
        actual = ensure_lists_in_model(bad_data, TestModel)
        expected = dict(
            pkg=[
                dict(
                    contents=[
                        dict(number=1)
                    ]
                )
            ]
        )
        # Assert bad data can be turned good
        assert actual == expected

        actual = ensure_lists_in_model(expected, TestModel)
        # Assert good data stays good
        assert actual == expected

        # Assert data is traversed even if the parent is OK.
        bad_data = dict(
            pkg=[
                dict(
                    contents=dict(number=1)
                )
            ]
        )
        actual = ensure_lists_in_model(bad_data, TestModel)
        assert actual == expected

    def test_model_with_modeltype_with_listtype_of_modeltype(self):  # pylint: disable=no-self-use,invalid-name
        class Item(XMLModel):
            number = IntType()

        class Container(XMLModel):
            items = ListType(ModelType(Item))

        class TestModel(XMLModel):
            container = ModelType(Container)

        bad_data = dict(
            container=dict(
                items=dict(number=1)
            )
        )
        actual = ensure_lists_in_model(bad_data, TestModel)
        expected = dict(
            container=dict(
                items=[
                    dict(number=1)
                ]
            )
        )
        # Assert bad data can be turned good
        assert actual == expected

        actual = ensure_lists_in_model(expected, TestModel)
        # Assert good data stays good
        assert actual == expected

    def test_model_with_dicttype_of_listtype_of_modeltype(self):  # pylint: disable=no-self-use,invalid-name
        class Item(XMLModel):
            number = StringType()

        class TestModel(XMLModel):
            items = DictType(ListType(ModelType(Item)))

        bad_data = dict(
            items=dict(
                bars=dict(number=1)
            )
        )
        actual = ensure_lists_in_model(bad_data, TestModel)
        expected = dict(
            items=dict(
                bars=[
                    dict(number=1)
                ]
            )
        )
        # Assert bad data can be turned good
        assert actual == expected

        actual = ensure_lists_in_model(expected, Model)
        # Assert good data stays good
        assert actual == expected

    def test_model_with_dicttype_of_modeltype_with_listtype(self):  # pylint: disable=no-self-use,invalid-name
        class Item(XMLModel):
            number = IntType()

        class Container(XMLModel):
            items = ListType(ModelType(Item))

        class TestModel(XMLModel):
            containers = DictType(ModelType(Container))

        bad_data = dict(
            containers=dict(
                a=dict(
                    items=dict(number=1)
                )
            )
        )
        actual = ensure_lists_in_model(bad_data, TestModel)
        expected = dict(
            containers=dict(
                a=dict(
                    items=[
                        dict(number=1)
                    ]
                )
            )
        )
        # Assert bad data can be turned good
        assert actual == expected

        actual = ensure_lists_in_model(expected, TestModel)
        # Assert good data stays good
        assert actual == expected

    def test_poly_model_type_raises(self):  # pylint: disable=no-self-use,invalid-name
        """
        PolyModelType is not implemented yet.
        """
        class Package(XMLModel):
            title = StringType()

        class Item(XMLModel):
            number = IntType()

        class TestModel(XMLModel):
            items = ListType(PolyModelType([Item, Package]))

        bad_data = dict(
            items=dict(number=1)
        )
        actual = ensure_lists_in_model(bad_data, TestModel)
        expected = dict(
            items=[
                dict(number=1)
            ]
        )
        # Assert bad data can be turned good
        assert actual == expected

        actual = ensure_lists_in_model(expected, TestModel)
        # Assert good data stays good
        assert actual == expected

        bad_data = dict(
            items=dict(title='Great products')
        )
        actual = ensure_lists_in_model(bad_data, TestModel)
        expected = dict(
            items=[
                dict(title='Great products')
            ]
        )
        # Assert bad data can be turned good
        assert actual == expected

        actual = ensure_lists_in_model(expected, TestModel)
        # Assert good data stays good
        assert actual == expected


class TestEncoding:  # pylint: disable=too-few-public-methods

    xml = (
        b"<?xml version='1.0' encoding='ISO-8859-1'?>\n"
        b'<person>\n'
        b'  <pk>32c5548e-ddee-4b23-a06e-f387a15bcac9</pk>\n'
        b'</person>\n'
    )

    def test_to_xml_accepts_encoding(self):
        class Person(XMLModel):
            pk = UUIDType()  # pylint: disable=invalid-name

        john = Person(dict(pk='32c5548e-ddee-4b23-a06e-f387a15bcac9'))
        actual = john.to_xml(encoding='ISO-8859-1')
        assert actual == self.xml

    def test_to_xml_uses_xml_encoding_model_attr(self):  # pylint: disable=invalid-name
        class Person(XMLModel):
            xml_encoding = 'ISO-8859-1'
            pk = UUIDType()  # pylint: disable=invalid-name

        john = Person(dict(pk='32c5548e-ddee-4b23-a06e-f387a15bcac9'))
        actual = john.to_xml()
        assert actual == self.xml
