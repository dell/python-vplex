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

from vplexapi.models.system_config_branding import SystemConfigBranding  # noqa: F401,E501


class SystemConfig(object):
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
        'branding': 'SystemConfigBranding',
        'product_type': 'str',
        'wan_type': 'str',
        'hardware_type': 'str',
        'limits': 'object'
    }

    attribute_map = {
        'branding': 'branding',
        'product_type': 'product_type',
        'wan_type': 'wan_type',
        'hardware_type': 'hardware_type',
        'limits': 'limits'
    }

    def __init__(self, branding=None, product_type=None, wan_type=None, hardware_type=None, limits=None):  # noqa: E501
        """SystemConfig - a model defined in Swagger"""  # noqa: E501

        self._branding = None
        self._product_type = None
        self._wan_type = None
        self._hardware_type = None
        self._limits = None
        self.discriminator = None

        if branding is not None:
            self.branding = branding
        if product_type is not None:
            self.product_type = product_type
        if wan_type is not None:
            self.wan_type = wan_type
        if hardware_type is not None:
            self.hardware_type = hardware_type
        if limits is not None:
            self.limits = limits

    @property
    def branding(self):
        """Gets the branding of this SystemConfig.  # noqa: E501


        :return: The branding of this SystemConfig.  # noqa: E501
        :rtype: SystemConfigBranding
        """
        return self._branding

    @branding.setter
    def branding(self, branding):
        """Sets the branding of this SystemConfig.


        :param branding: The branding of this SystemConfig.  # noqa: E501
        :type: SystemConfigBranding
        """

        self._branding = branding

    @property
    def product_type(self):
        """Gets the product_type of this SystemConfig.  # noqa: E501


        :return: The product_type of this SystemConfig.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this SystemConfig.


        :param product_type: The product_type of this SystemConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["local", "metro", "unknown"]  # noqa: E501
        if product_type not in allowed_values:
            raise ValueError(
                "Invalid value for `product_type` ({0}), must be one of {1}"  # noqa: E501
                .format(product_type, allowed_values)
            )

        self._product_type = product_type

    @property
    def wan_type(self):
        """Gets the wan_type of this SystemConfig.  # noqa: E501


        :return: The wan_type of this SystemConfig.  # noqa: E501
        :rtype: str
        """
        return self._wan_type

    @wan_type.setter
    def wan_type(self, wan_type):
        """Sets the wan_type of this SystemConfig.


        :param wan_type: The wan_type of this SystemConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["FC", "IP", "unknown"]  # noqa: E501
        if wan_type not in allowed_values:
            raise ValueError(
                "Invalid value for `wan_type` ({0}), must be one of {1}"  # noqa: E501
                .format(wan_type, allowed_values)
            )

        self._wan_type = wan_type

    @property
    def hardware_type(self):
        """Gets the hardware_type of this SystemConfig.  # noqa: E501


        :return: The hardware_type of this SystemConfig.  # noqa: E501
        :rtype: str
        """
        return self._hardware_type

    @hardware_type.setter
    def hardware_type(self, hardware_type):
        """Sets the hardware_type of this SystemConfig.


        :param hardware_type: The hardware_type of this SystemConfig.  # noqa: E501
        :type: str
        """

        self._hardware_type = hardware_type

    @property
    def limits(self):
        """Gets the limits of this SystemConfig.  # noqa: E501


        :return: The limits of this SystemConfig.  # noqa: E501
        :rtype: object
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this SystemConfig.


        :param limits: The limits of this SystemConfig.  # noqa: E501
        :type: object
        """

        self._limits = limits

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
        if not isinstance(other, SystemConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other