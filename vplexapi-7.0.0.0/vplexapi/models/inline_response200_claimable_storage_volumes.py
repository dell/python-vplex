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


class InlineResponse200ClaimableStorageVolumes(object):
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
        'storage_volume_path': 'str',
        'storage_volume_name': 'str'
    }

    attribute_map = {
        'storage_volume_path': 'storage_volume_path',
        'storage_volume_name': 'storage_volume_name'
    }

    def __init__(self, storage_volume_path=None, storage_volume_name=None):  # noqa: E501
        """InlineResponse200ClaimableStorageVolumes - a model defined in Swagger"""  # noqa: E501

        self._storage_volume_path = None
        self._storage_volume_name = None
        self.discriminator = None

        if storage_volume_path is not None:
            self.storage_volume_path = storage_volume_path
        if storage_volume_name is not None:
            self.storage_volume_name = storage_volume_name

    @property
    def storage_volume_path(self):
        """Gets the storage_volume_path of this InlineResponse200ClaimableStorageVolumes.  # noqa: E501


        :return: The storage_volume_path of this InlineResponse200ClaimableStorageVolumes.  # noqa: E501
        :rtype: str
        """
        return self._storage_volume_path

    @storage_volume_path.setter
    def storage_volume_path(self, storage_volume_path):
        """Sets the storage_volume_path of this InlineResponse200ClaimableStorageVolumes.


        :param storage_volume_path: The storage_volume_path of this InlineResponse200ClaimableStorageVolumes.  # noqa: E501
        :type: str
        """

        self._storage_volume_path = storage_volume_path

    @property
    def storage_volume_name(self):
        """Gets the storage_volume_name of this InlineResponse200ClaimableStorageVolumes.  # noqa: E501


        :return: The storage_volume_name of this InlineResponse200ClaimableStorageVolumes.  # noqa: E501
        :rtype: str
        """
        return self._storage_volume_name

    @storage_volume_name.setter
    def storage_volume_name(self, storage_volume_name):
        """Sets the storage_volume_name of this InlineResponse200ClaimableStorageVolumes.


        :param storage_volume_name: The storage_volume_name of this InlineResponse200ClaimableStorageVolumes.  # noqa: E501
        :type: str
        """

        self._storage_volume_name = storage_volume_name

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200ClaimableStorageVolumes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other