# coding: utf-8

"""
    VPlex REST API

    A definition for the next-gen VPlex API  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from vplexapi.models.bulk_response_tasks import BulkResponseTasks  # noqa: F401,E501


class BulkResponse(object):
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
        'status': 'str',
        'tasks': 'list[BulkResponseTasks]'
    }

    attribute_map = {
        'status': 'status',
        'tasks': 'tasks'
    }

    def __init__(self, status=None, tasks=None):  # noqa: E501
        """BulkResponse - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._tasks = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if tasks is not None:
            self.tasks = tasks

    @property
    def status(self):
        """Gets the status of this BulkResponse.  # noqa: E501


        :return: The status of this BulkResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BulkResponse.


        :param status: The status of this BulkResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tasks(self):
        """Gets the tasks of this BulkResponse.  # noqa: E501


        :return: The tasks of this BulkResponse.  # noqa: E501
        :rtype: list[BulkResponseTasks]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this BulkResponse.


        :param tasks: The tasks of this BulkResponse.  # noqa: E501
        :type: list[BulkResponseTasks]
        """

        self._tasks = tasks

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
        if issubclass(BulkResponse, dict):
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
        if not isinstance(other, BulkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
