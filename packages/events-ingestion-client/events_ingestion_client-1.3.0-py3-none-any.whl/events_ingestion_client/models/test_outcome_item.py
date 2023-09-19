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

class TestOutcomeItem(object):
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
        'dimensions': 'list[str]',
        'metric_value': 'float',
        'max_threshold': 'float',
        'start_time': 'datetime',
        'min_threshold': 'float',
        'integrations': 'AllOfTestOutcomeItemIntegrations',
        'result': 'str',
        'metric_description': 'str',
        'key': 'str',
        'name': 'str',
        'end_time': 'datetime',
        'metadata': 'object',
        'description': 'str',
        'metric_name': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'metric_value': 'metric_value',
        'max_threshold': 'max_threshold',
        'start_time': 'start_time',
        'min_threshold': 'min_threshold',
        'integrations': 'integrations',
        'result': 'result',
        'metric_description': 'metric_description',
        'key': 'key',
        'name': 'name',
        'end_time': 'end_time',
        'metadata': 'metadata',
        'description': 'description',
        'metric_name': 'metric_name',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, dimensions=None, metric_value=None, max_threshold=None, start_time=None, min_threshold=None, integrations=None, result=None, metric_description=None, key=None, name=None, end_time=None, metadata=None, description=None, metric_name=None, status=None, type=None):  # noqa: E501
        """TestOutcomeItem - a model defined in Swagger"""  # noqa: E501
        self._dimensions = None
        self._metric_value = None
        self._max_threshold = None
        self._start_time = None
        self._min_threshold = None
        self._integrations = None
        self._result = None
        self._metric_description = None
        self._key = None
        self._name = None
        self._end_time = None
        self._metadata = None
        self._description = None
        self._metric_name = None
        self._status = None
        self._type = None
        self.discriminator = None
        if dimensions is not None:
            self.dimensions = dimensions
        if metric_value is not None:
            self.metric_value = metric_value
        if max_threshold is not None:
            self.max_threshold = max_threshold
        if start_time is not None:
            self.start_time = start_time
        if min_threshold is not None:
            self.min_threshold = min_threshold
        if integrations is not None:
            self.integrations = integrations
        if result is not None:
            self.result = result
        if metric_description is not None:
            self.metric_description = metric_description
        if key is not None:
            self.key = key
        self.name = name
        if end_time is not None:
            self.end_time = end_time
        if metadata is not None:
            self.metadata = metadata
        if description is not None:
            self.description = description
        if metric_name is not None:
            self.metric_name = metric_name
        self.status = status
        if type is not None:
            self.type = type

    @property
    def dimensions(self):
        """Gets the dimensions of this TestOutcomeItem.  # noqa: E501

        Optional. Represents a list of data quality aspects the test is meant to address.  # noqa: E501

        :return: The dimensions of this TestOutcomeItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this TestOutcomeItem.

        Optional. Represents a list of data quality aspects the test is meant to address.  # noqa: E501

        :param dimensions: The dimensions of this TestOutcomeItem.  # noqa: E501
        :type: list[str]
        """

        self._dimensions = dimensions

    @property
    def metric_value(self):
        """Gets the metric_value of this TestOutcomeItem.  # noqa: E501

        Optional. A numerical test outcome.  # noqa: E501

        :return: The metric_value of this TestOutcomeItem.  # noqa: E501
        :rtype: float
        """
        return self._metric_value

    @metric_value.setter
    def metric_value(self, metric_value):
        """Sets the metric_value of this TestOutcomeItem.

        Optional. A numerical test outcome.  # noqa: E501

        :param metric_value: The metric_value of this TestOutcomeItem.  # noqa: E501
        :type: float
        """

        self._metric_value = metric_value

    @property
    def max_threshold(self):
        """Gets the max_threshold of this TestOutcomeItem.  # noqa: E501

        Optional. The maximum acceptable value for the test metric_value.  # noqa: E501

        :return: The max_threshold of this TestOutcomeItem.  # noqa: E501
        :rtype: float
        """
        return self._max_threshold

    @max_threshold.setter
    def max_threshold(self, max_threshold):
        """Sets the max_threshold of this TestOutcomeItem.

        Optional. The maximum acceptable value for the test metric_value.  # noqa: E501

        :param max_threshold: The max_threshold of this TestOutcomeItem.  # noqa: E501
        :type: float
        """

        self._max_threshold = max_threshold

    @property
    def start_time(self):
        """Gets the start_time of this TestOutcomeItem.  # noqa: E501

        An ISO timestamp of when the test execution started.  # noqa: E501

        :return: The start_time of this TestOutcomeItem.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TestOutcomeItem.

        An ISO timestamp of when the test execution started.  # noqa: E501

        :param start_time: The start_time of this TestOutcomeItem.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def min_threshold(self):
        """Gets the min_threshold of this TestOutcomeItem.  # noqa: E501

        Optional. The minimum acceptable value for the test metric_value  # noqa: E501

        :return: The min_threshold of this TestOutcomeItem.  # noqa: E501
        :rtype: float
        """
        return self._min_threshold

    @min_threshold.setter
    def min_threshold(self, min_threshold):
        """Sets the min_threshold of this TestOutcomeItem.

        Optional. The minimum acceptable value for the test metric_value  # noqa: E501

        :param min_threshold: The min_threshold of this TestOutcomeItem.  # noqa: E501
        :type: float
        """

        self._min_threshold = min_threshold

    @property
    def integrations(self):
        """Gets the integrations of this TestOutcomeItem.  # noqa: E501

        Optional. Test data specific to DataKitchen Inc. software integrations.  # noqa: E501

        :return: The integrations of this TestOutcomeItem.  # noqa: E501
        :rtype: AllOfTestOutcomeItemIntegrations
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """Sets the integrations of this TestOutcomeItem.

        Optional. Test data specific to DataKitchen Inc. software integrations.  # noqa: E501

        :param integrations: The integrations of this TestOutcomeItem.  # noqa: E501
        :type: AllOfTestOutcomeItemIntegrations
        """

        self._integrations = integrations

    @property
    def result(self):
        """Gets the result of this TestOutcomeItem.  # noqa: E501

        Optional. A string representing the tests' result.  # noqa: E501

        :return: The result of this TestOutcomeItem.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this TestOutcomeItem.

        Optional. A string representing the tests' result.  # noqa: E501

        :param result: The result of this TestOutcomeItem.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def metric_description(self):
        """Gets the metric_description of this TestOutcomeItem.  # noqa: E501

        Optional. A description of the unit under measure.  # noqa: E501

        :return: The metric_description of this TestOutcomeItem.  # noqa: E501
        :rtype: str
        """
        return self._metric_description

    @metric_description.setter
    def metric_description(self, metric_description):
        """Sets the metric_description of this TestOutcomeItem.

        Optional. A description of the unit under measure.  # noqa: E501

        :param metric_description: The metric_description of this TestOutcomeItem.  # noqa: E501
        :type: str
        """

        self._metric_description = metric_description

    @property
    def key(self):
        """Gets the key of this TestOutcomeItem.  # noqa: E501

        Optional. A correlation key. Tests with the same key are assumed to be related.  # noqa: E501

        :return: The key of this TestOutcomeItem.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TestOutcomeItem.

        Optional. A correlation key. Tests with the same key are assumed to be related.  # noqa: E501

        :param key: The key of this TestOutcomeItem.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this TestOutcomeItem.  # noqa: E501

        The name of the test.  # noqa: E501

        :return: The name of this TestOutcomeItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestOutcomeItem.

        The name of the test.  # noqa: E501

        :param name: The name of this TestOutcomeItem.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def end_time(self):
        """Gets the end_time of this TestOutcomeItem.  # noqa: E501

        An ISO timestamp of when the test execution ended.  # noqa: E501

        :return: The end_time of this TestOutcomeItem.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TestOutcomeItem.

        An ISO timestamp of when the test execution ended.  # noqa: E501

        :param end_time: The end_time of this TestOutcomeItem.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def metadata(self):
        """Gets the metadata of this TestOutcomeItem.  # noqa: E501

        Optional. Additional key-value information for the event. Provided by the user as needed.  # noqa: E501

        :return: The metadata of this TestOutcomeItem.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this TestOutcomeItem.

        Optional. Additional key-value information for the event. Provided by the user as needed.  # noqa: E501

        :param metadata: The metadata of this TestOutcomeItem.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def description(self):
        """Gets the description of this TestOutcomeItem.  # noqa: E501

        Optional. A description of the test outcomes.  # noqa: E501

        :return: The description of this TestOutcomeItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TestOutcomeItem.

        Optional. A description of the test outcomes.  # noqa: E501

        :param description: The description of this TestOutcomeItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def metric_name(self):
        """Gets the metric_name of this TestOutcomeItem.  # noqa: E501

        Optional. The name of the metric, or its unit of measure.  # noqa: E501

        :return: The metric_name of this TestOutcomeItem.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this TestOutcomeItem.

        Optional. The name of the metric, or its unit of measure.  # noqa: E501

        :param metric_name: The metric_name of this TestOutcomeItem.  # noqa: E501
        :type: str
        """

        self._metric_name = metric_name

    @property
    def status(self):
        """Gets the status of this TestOutcomeItem.  # noqa: E501

        Required. The test status to be applied. Can set the status for both tests in runs and tests in tasks.  # noqa: E501

        :return: The status of this TestOutcomeItem.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TestOutcomeItem.

        Required. The test status to be applied. Can set the status for both tests in runs and tests in tasks.  # noqa: E501

        :param status: The status of this TestOutcomeItem.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["PASSED", "FAILED", "WARNING"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def type(self):
        """Gets the type of this TestOutcomeItem.  # noqa: E501

        Optional. Represents type or archetype of a test.  # noqa: E501

        :return: The type of this TestOutcomeItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TestOutcomeItem.

        Optional. Represents type or archetype of a test.  # noqa: E501

        :param type: The type of this TestOutcomeItem.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(TestOutcomeItem, dict):
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
        if not isinstance(other, TestOutcomeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
