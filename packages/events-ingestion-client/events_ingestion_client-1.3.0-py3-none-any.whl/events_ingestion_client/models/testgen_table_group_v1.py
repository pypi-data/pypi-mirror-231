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

class TestgenTableGroupV1(object):
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
        'sample_percentage': 'str',
        'project_code': 'str',
        'sample_minimum_count': 'int',
        'group_id': 'str',
        'uses_sampling': 'bool'
    }

    attribute_map = {
        'sample_percentage': 'sample_percentage',
        'project_code': 'project_code',
        'sample_minimum_count': 'sample_minimum_count',
        'group_id': 'group_id',
        'uses_sampling': 'uses_sampling'
    }

    def __init__(self, sample_percentage=None, project_code=None, sample_minimum_count=None, group_id=None, uses_sampling=False):  # noqa: E501
        """TestgenTableGroupV1 - a model defined in Swagger"""  # noqa: E501
        self._sample_percentage = None
        self._project_code = None
        self._sample_minimum_count = None
        self._group_id = None
        self._uses_sampling = None
        self.discriminator = None
        if sample_percentage is not None:
            self.sample_percentage = sample_percentage
        self.project_code = project_code
        if sample_minimum_count is not None:
            self.sample_minimum_count = sample_minimum_count
        self.group_id = group_id
        if uses_sampling is not None:
            self.uses_sampling = uses_sampling

    @property
    def sample_percentage(self):
        """Gets the sample_percentage of this TestgenTableGroupV1.  # noqa: E501

        Optional. Requires use_sampling. Percentage of sampling.  # noqa: E501

        :return: The sample_percentage of this TestgenTableGroupV1.  # noqa: E501
        :rtype: str
        """
        return self._sample_percentage

    @sample_percentage.setter
    def sample_percentage(self, sample_percentage):
        """Sets the sample_percentage of this TestgenTableGroupV1.

        Optional. Requires use_sampling. Percentage of sampling.  # noqa: E501

        :param sample_percentage: The sample_percentage of this TestgenTableGroupV1.  # noqa: E501
        :type: str
        """

        self._sample_percentage = sample_percentage

    @property
    def project_code(self):
        """Gets the project_code of this TestgenTableGroupV1.  # noqa: E501

        Required. The project code associated with the table group.  # noqa: E501

        :return: The project_code of this TestgenTableGroupV1.  # noqa: E501
        :rtype: str
        """
        return self._project_code

    @project_code.setter
    def project_code(self, project_code):
        """Sets the project_code of this TestgenTableGroupV1.

        Required. The project code associated with the table group.  # noqa: E501

        :param project_code: The project_code of this TestgenTableGroupV1.  # noqa: E501
        :type: str
        """
        if project_code is None:
            raise ValueError("Invalid value for `project_code`, must not be `None`")  # noqa: E501

        self._project_code = project_code

    @property
    def sample_minimum_count(self):
        """Gets the sample_minimum_count of this TestgenTableGroupV1.  # noqa: E501

        Optional. Requires use_sampling. Minimum number of samples.  # noqa: E501

        :return: The sample_minimum_count of this TestgenTableGroupV1.  # noqa: E501
        :rtype: int
        """
        return self._sample_minimum_count

    @sample_minimum_count.setter
    def sample_minimum_count(self, sample_minimum_count):
        """Sets the sample_minimum_count of this TestgenTableGroupV1.

        Optional. Requires use_sampling. Minimum number of samples.  # noqa: E501

        :param sample_minimum_count: The sample_minimum_count of this TestgenTableGroupV1.  # noqa: E501
        :type: int
        """

        self._sample_minimum_count = sample_minimum_count

    @property
    def group_id(self):
        """Gets the group_id of this TestgenTableGroupV1.  # noqa: E501

        Required. The ID of the table group.  # noqa: E501

        :return: The group_id of this TestgenTableGroupV1.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this TestgenTableGroupV1.

        Required. The ID of the table group.  # noqa: E501

        :param group_id: The group_id of this TestgenTableGroupV1.  # noqa: E501
        :type: str
        """
        if group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")  # noqa: E501

        self._group_id = group_id

    @property
    def uses_sampling(self):
        """Gets the uses_sampling of this TestgenTableGroupV1.  # noqa: E501

        Optional. Event comes from a Table Group that uses a sampling of data. Defaults to false.  # noqa: E501

        :return: The uses_sampling of this TestgenTableGroupV1.  # noqa: E501
        :rtype: bool
        """
        return self._uses_sampling

    @uses_sampling.setter
    def uses_sampling(self, uses_sampling):
        """Sets the uses_sampling of this TestgenTableGroupV1.

        Optional. Event comes from a Table Group that uses a sampling of data. Defaults to false.  # noqa: E501

        :param uses_sampling: The uses_sampling of this TestgenTableGroupV1.  # noqa: E501
        :type: bool
        """

        self._uses_sampling = uses_sampling

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
        if issubclass(TestgenTableGroupV1, dict):
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
        if not isinstance(other, TestgenTableGroupV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
