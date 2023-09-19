# coding: utf-8

"""
    Event Ingestion API

    Event Ingestion API client for DataKitchen’s DataOps Observability  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@datakitchen.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TestgenItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'test_suite': 'str',
        'columns': 'list[str]',
        'table': 'str',
        'version': 'float',
        'test_parameters': 'list[TestgenItemTestParameters]'
    }

    attribute_map = {
        'test_suite': 'test_suite',
        'columns': 'columns',
        'table': 'table',
        'version': 'version',
        'test_parameters': 'test_parameters'
    }

    def __init__(self, test_suite=None, columns=None, table=None, version=None, test_parameters=None):  # noqa: E501
        """TestgenItem - a model defined in Swagger"""  # noqa: E501
        self._test_suite = None
        self._columns = None
        self._table = None
        self._version = None
        self._test_parameters = None
        self.discriminator = None
        self.test_suite = test_suite
        if columns is not None:
            self.columns = columns
        self.table = table
        self.version = version
        if test_parameters is not None:
            self.test_parameters = test_parameters

    @property
    def test_suite(self):
        """Gets the test_suite of this TestgenItem.  # noqa: E501

        Required. The name of the test suite the test is a member of.  # noqa: E501

        :return: The test_suite of this TestgenItem.  # noqa: E501
        :rtype: str
        """
        return self._test_suite

    @test_suite.setter
    def test_suite(self, test_suite):
        """Sets the test_suite of this TestgenItem.

        Required. The name of the test suite the test is a member of.  # noqa: E501

        :param test_suite: The test_suite of this TestgenItem.  # noqa: E501
        :type: str
        """
        if test_suite is None:
            raise ValueError("Invalid value for `test_suite`, must not be `None`")  # noqa: E501

        self._test_suite = test_suite

    @property
    def columns(self):
        """Gets the columns of this TestgenItem.  # noqa: E501

        Optional. The name(s) of the table column(s) the test was conducted on.  # noqa: E501

        :return: The columns of this TestgenItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this TestgenItem.

        Optional. The name(s) of the table column(s) the test was conducted on.  # noqa: E501

        :param columns: The columns of this TestgenItem.  # noqa: E501
        :type: list[str]
        """

        self._columns = columns

    @property
    def table(self):
        """Gets the table of this TestgenItem.  # noqa: E501

        Required. Name of the table the test was conducted on.  # noqa: E501

        :return: The table of this TestgenItem.  # noqa: E501
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this TestgenItem.

        Required. Name of the table the test was conducted on.  # noqa: E501

        :param table: The table of this TestgenItem.  # noqa: E501
        :type: str
        """
        if table is None:
            raise ValueError("Invalid value for `table`, must not be `None`")  # noqa: E501

        self._table = table

    @property
    def version(self):
        """Gets the version of this TestgenItem.  # noqa: E501

        Required. The integration schema version.  # noqa: E501

        :return: The version of this TestgenItem.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TestgenItem.

        Required. The integration schema version.  # noqa: E501

        :param version: The version of this TestgenItem.  # noqa: E501
        :type: float
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def test_parameters(self):
        """Gets the test_parameters of this TestgenItem.  # noqa: E501

        Optional. An arbitrary list of test parameter descriptions. Defaults to an empty list.  # noqa: E501

        :return: The test_parameters of this TestgenItem.  # noqa: E501
        :rtype: list[TestgenItemTestParameters]
        """
        return self._test_parameters

    @test_parameters.setter
    def test_parameters(self, test_parameters):
        """Sets the test_parameters of this TestgenItem.

        Optional. An arbitrary list of test parameter descriptions. Defaults to an empty list.  # noqa: E501

        :param test_parameters: The test_parameters of this TestgenItem.  # noqa: E501
        :type: list[TestgenItemTestParameters]
        """

        self._test_parameters = test_parameters

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TestgenItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TestgenItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
