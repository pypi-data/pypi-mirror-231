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

class TestOutcomeItemIntegrations(object):
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
        'testgen': 'AllOfTestOutcomeItemIntegrationsTestgen'
    }

    attribute_map = {
        'testgen': 'testgen'
    }

    def __init__(self, testgen=None):  # noqa: E501
        """TestOutcomeItemIntegrations - a model defined in Swagger"""  # noqa: E501
        self._testgen = None
        self.discriminator = None
        self.testgen = testgen

    @property
    def testgen(self):
        """Gets the testgen of this TestOutcomeItemIntegrations.  # noqa: E501

        Required. Component data specific to DataKitchen Inc. Testgen integration.  # noqa: E501

        :return: The testgen of this TestOutcomeItemIntegrations.  # noqa: E501
        :rtype: AllOfTestOutcomeItemIntegrationsTestgen
        """
        return self._testgen

    @testgen.setter
    def testgen(self, testgen):
        """Sets the testgen of this TestOutcomeItemIntegrations.

        Required. Component data specific to DataKitchen Inc. Testgen integration.  # noqa: E501

        :param testgen: The testgen of this TestOutcomeItemIntegrations.  # noqa: E501
        :type: AllOfTestOutcomeItemIntegrationsTestgen
        """
        if testgen is None:
            raise ValueError("Invalid value for `testgen`, must not be `None`")  # noqa: E501

        self._testgen = testgen

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
        if issubclass(TestOutcomeItemIntegrations, dict):
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
        if not isinstance(other, TestOutcomeItemIntegrations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
