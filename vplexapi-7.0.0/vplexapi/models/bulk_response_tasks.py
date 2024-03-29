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


class BulkResponseTasks(object):
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
        'object': 'str',
        'reason': 'object',
        'additional_properties': 'object'
    }

    attribute_map = {
        'status': 'status',
        'object': 'object',
        'reason': 'reason',
        'additional_properties': 'additionalProperties'
    }

    def __init__(self, status=None, object=None, reason=None, additional_properties=None):  # noqa: E501
        """BulkResponseTasks - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._object = None
        self._reason = None
        self._additional_properties = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if object is not None:
            self.object = object
        if reason is not None:
            self.reason = reason
        if additional_properties is not None:
            self.additional_properties = additional_properties

    @property
    def status(self):
        """Gets the status of this BulkResponseTasks.  # noqa: E501


        :return: The status of this BulkResponseTasks.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BulkResponseTasks.


        :param status: The status of this BulkResponseTasks.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def object(self):
        """Gets the object of this BulkResponseTasks.  # noqa: E501


        :return: The object of this BulkResponseTasks.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this BulkResponseTasks.


        :param object: The object of this BulkResponseTasks.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def reason(self):
        """Gets the reason of this BulkResponseTasks.  # noqa: E501


        :return: The reason of this BulkResponseTasks.  # noqa: E501
        :rtype: object
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this BulkResponseTasks.


        :param reason: The reason of this BulkResponseTasks.  # noqa: E501
        :type: object
        """

        self._reason = reason

    @property
    def additional_properties(self):
        """Gets the additional_properties of this BulkResponseTasks.  # noqa: E501


        :return: The additional_properties of this BulkResponseTasks.  # noqa: E501
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """Sets the additional_properties of this BulkResponseTasks.


        :param additional_properties: The additional_properties of this BulkResponseTasks.  # noqa: E501
        :type: object
        """

        self._additional_properties = additional_properties

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
        if issubclass(BulkResponseTasks, dict):
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
        if not isinstance(other, BulkResponseTasks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
