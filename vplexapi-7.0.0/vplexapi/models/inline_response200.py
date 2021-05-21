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

from vplexapi.models.inline_response200_claimable_storage_volumes import InlineResponse200ClaimableStorageVolumes  # noqa: F401,E501


class InlineResponse200(object):
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
        'claimable_storage_volumes': 'list[InlineResponse200ClaimableStorageVolumes]',
        'unclaimed_storage_volumes': 'int',
        'storage_array': 'str'
    }

    attribute_map = {
        'claimable_storage_volumes': 'claimable_storage_volumes',
        'unclaimed_storage_volumes': 'unclaimed_storage_volumes',
        'storage_array': 'storage_array'
    }

    def __init__(self, claimable_storage_volumes=None, unclaimed_storage_volumes=None, storage_array=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501

        self._claimable_storage_volumes = None
        self._unclaimed_storage_volumes = None
        self._storage_array = None
        self.discriminator = None

        if claimable_storage_volumes is not None:
            self.claimable_storage_volumes = claimable_storage_volumes
        if unclaimed_storage_volumes is not None:
            self.unclaimed_storage_volumes = unclaimed_storage_volumes
        if storage_array is not None:
            self.storage_array = storage_array

    @property
    def claimable_storage_volumes(self):
        """Gets the claimable_storage_volumes of this InlineResponse200.  # noqa: E501


        :return: The claimable_storage_volumes of this InlineResponse200.  # noqa: E501
        :rtype: list[InlineResponse200ClaimableStorageVolumes]
        """
        return self._claimable_storage_volumes

    @claimable_storage_volumes.setter
    def claimable_storage_volumes(self, claimable_storage_volumes):
        """Sets the claimable_storage_volumes of this InlineResponse200.


        :param claimable_storage_volumes: The claimable_storage_volumes of this InlineResponse200.  # noqa: E501
        :type: list[InlineResponse200ClaimableStorageVolumes]
        """

        self._claimable_storage_volumes = claimable_storage_volumes

    @property
    def unclaimed_storage_volumes(self):
        """Gets the unclaimed_storage_volumes of this InlineResponse200.  # noqa: E501


        :return: The unclaimed_storage_volumes of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._unclaimed_storage_volumes

    @unclaimed_storage_volumes.setter
    def unclaimed_storage_volumes(self, unclaimed_storage_volumes):
        """Sets the unclaimed_storage_volumes of this InlineResponse200.


        :param unclaimed_storage_volumes: The unclaimed_storage_volumes of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._unclaimed_storage_volumes = unclaimed_storage_volumes

    @property
    def storage_array(self):
        """Gets the storage_array of this InlineResponse200.  # noqa: E501


        :return: The storage_array of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._storage_array

    @storage_array.setter
    def storage_array(self, storage_array):
        """Sets the storage_array of this InlineResponse200.


        :param storage_array: The storage_array of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._storage_array = storage_array

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other