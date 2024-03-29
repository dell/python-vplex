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


class DistributedVirtualVolumeExpandPayload(object):
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
        'skip_init': 'bool'
    }

    attribute_map = {
        'skip_init': 'skip_init'
    }

    def __init__(self, skip_init=None):  # noqa: E501
        """DistributedVirtualVolumeExpandPayload - a model defined in Swagger"""  # noqa: E501

        self._skip_init = None
        self.discriminator = None

        if skip_init is not None:
            self.skip_init = skip_init

    @property
    def skip_init(self):
        """Gets the skip_init of this DistributedVirtualVolumeExpandPayload.  # noqa: E501

        If skip_init is true the blocks of the expanded space will NOT be initialized to ensure single-disk semantics. This option should only be used under very specific circumstances, such as part of the recovery procedure after restoring metadata from backup.  # noqa: E501

        :return: The skip_init of this DistributedVirtualVolumeExpandPayload.  # noqa: E501
        :rtype: bool
        """
        return self._skip_init

    @skip_init.setter
    def skip_init(self, skip_init):
        """Sets the skip_init of this DistributedVirtualVolumeExpandPayload.

        If skip_init is true the blocks of the expanded space will NOT be initialized to ensure single-disk semantics. This option should only be used under very specific circumstances, such as part of the recovery procedure after restoring metadata from backup.  # noqa: E501

        :param skip_init: The skip_init of this DistributedVirtualVolumeExpandPayload.  # noqa: E501
        :type: bool
        """

        self._skip_init = skip_init

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
        if issubclass(DistributedVirtualVolumeExpandPayload, dict):
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
        if not isinstance(other, DistributedVirtualVolumeExpandPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
