# coding: utf-8

"""
    VPlex REST API

    A defnition for the next-gen VPlex API  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DistributedVirtualVolumePayload(object):
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
        'tier': 'str',
        'thin': 'bool',
        'init': 'bool',
        'device': 'str'
    }

    attribute_map = {
        'tier': 'tier',
        'thin': 'thin',
        'init': 'init',
        'device': 'device'
    }

    def __init__(self, tier=None, thin=None, init=None, device=None):  # noqa: E501
        """DistributedVirtualVolumePayload - a model defined in Swagger"""  # noqa: E501

        self._tier = None
        self._thin = None
        self._init = None
        self._device = None
        self.discriminator = None

        if tier is not None:
            self.tier = tier
        if thin is not None:
            self.thin = thin
        if init is not None:
            self.init = init
        if device is not None:
            self.device = device

    @property
    def tier(self):
        """Gets the tier of this DistributedVirtualVolumePayload.  # noqa: E501


        :return: The tier of this DistributedVirtualVolumePayload.  # noqa: E501
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this DistributedVirtualVolumePayload.


        :param tier: The tier of this DistributedVirtualVolumePayload.  # noqa: E501
        :type: str
        """

        self._tier = tier

    @property
    def thin(self):
        """Gets the thin of this DistributedVirtualVolumePayload.  # noqa: E501


        :return: The thin of this DistributedVirtualVolumePayload.  # noqa: E501
        :rtype: bool
        """
        return self._thin

    @thin.setter
    def thin(self, thin):
        """Sets the thin of this DistributedVirtualVolumePayload.


        :param thin: The thin of this DistributedVirtualVolumePayload.  # noqa: E501
        :type: bool
        """

        self._thin = thin

    @property
    def init(self):
        """Gets the init of this DistributedVirtualVolumePayload.  # noqa: E501


        :return: The init of this DistributedVirtualVolumePayload.  # noqa: E501
        :rtype: bool
        """
        return self._init

    @init.setter
    def init(self, init):
        """Sets the init of this DistributedVirtualVolumePayload.


        :param init: The init of this DistributedVirtualVolumePayload.  # noqa: E501
        :type: bool
        """

        self._init = init

    @property
    def device(self):
        """Gets the device of this DistributedVirtualVolumePayload.  # noqa: E501


        :return: The device of this DistributedVirtualVolumePayload.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this DistributedVirtualVolumePayload.


        :param device: The device of this DistributedVirtualVolumePayload.  # noqa: E501
        :type: str
        """

        self._device = device

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
        if not isinstance(other, DistributedVirtualVolumePayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
