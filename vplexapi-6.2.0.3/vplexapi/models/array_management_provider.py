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


class ArrayManagementProvider(object):
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
        'managed_arrays': 'list[str]',
        'name': 'str',
        'ip_address': 'str',
        'user_name': 'str',
        'port': 'str',
        'connectivity': 'str',
        'provider_type': 'str',
        'use_ssl': 'bool'
    }

    attribute_map = {
        'managed_arrays': 'managed_arrays',
        'name': 'name',
        'ip_address': 'ip_address',
        'user_name': 'user_name',
        'port': 'port',
        'connectivity': 'connectivity',
        'provider_type': 'provider_type',
        'use_ssl': 'use_ssl'
    }

    def __init__(self, managed_arrays=None, name=None, ip_address=None, user_name=None, port=None, connectivity=None, provider_type=None, use_ssl=None):  # noqa: E501
        """ArrayManagementProvider - a model defined in Swagger"""  # noqa: E501

        self._managed_arrays = None
        self._name = None
        self._ip_address = None
        self._user_name = None
        self._port = None
        self._connectivity = None
        self._provider_type = None
        self._use_ssl = None
        self.discriminator = None

        if managed_arrays is not None:
            self.managed_arrays = managed_arrays
        if name is not None:
            self.name = name
        if ip_address is not None:
            self.ip_address = ip_address
        if user_name is not None:
            self.user_name = user_name
        if port is not None:
            self.port = port
        if connectivity is not None:
            self.connectivity = connectivity
        if provider_type is not None:
            self.provider_type = provider_type
        if use_ssl is not None:
            self.use_ssl = use_ssl

    @property
    def managed_arrays(self):
        """Gets the managed_arrays of this ArrayManagementProvider.  # noqa: E501


        :return: The managed_arrays of this ArrayManagementProvider.  # noqa: E501
        :rtype: list[str]
        """
        return self._managed_arrays

    @managed_arrays.setter
    def managed_arrays(self, managed_arrays):
        """Sets the managed_arrays of this ArrayManagementProvider.


        :param managed_arrays: The managed_arrays of this ArrayManagementProvider.  # noqa: E501
        :type: list[str]
        """

        self._managed_arrays = managed_arrays

    @property
    def name(self):
        """Gets the name of this ArrayManagementProvider.  # noqa: E501


        :return: The name of this ArrayManagementProvider.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArrayManagementProvider.


        :param name: The name of this ArrayManagementProvider.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ip_address(self):
        """Gets the ip_address of this ArrayManagementProvider.  # noqa: E501


        :return: The ip_address of this ArrayManagementProvider.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ArrayManagementProvider.


        :param ip_address: The ip_address of this ArrayManagementProvider.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def user_name(self):
        """Gets the user_name of this ArrayManagementProvider.  # noqa: E501


        :return: The user_name of this ArrayManagementProvider.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ArrayManagementProvider.


        :param user_name: The user_name of this ArrayManagementProvider.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def port(self):
        """Gets the port of this ArrayManagementProvider.  # noqa: E501


        :return: The port of this ArrayManagementProvider.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ArrayManagementProvider.


        :param port: The port of this ArrayManagementProvider.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def connectivity(self):
        """Gets the connectivity of this ArrayManagementProvider.  # noqa: E501


        :return: The connectivity of this ArrayManagementProvider.  # noqa: E501
        :rtype: str
        """
        return self._connectivity

    @connectivity.setter
    def connectivity(self, connectivity):
        """Sets the connectivity of this ArrayManagementProvider.


        :param connectivity: The connectivity of this ArrayManagementProvider.  # noqa: E501
        :type: str
        """
        allowed_values = ["connected", "unreachable"]  # noqa: E501
        if connectivity not in allowed_values:
            raise ValueError(
                "Invalid value for `connectivity` ({0}), must be one of {1}"  # noqa: E501
                .format(connectivity, allowed_values)
            )

        self._connectivity = connectivity

    @property
    def provider_type(self):
        """Gets the provider_type of this ArrayManagementProvider.  # noqa: E501


        :return: The provider_type of this ArrayManagementProvider.  # noqa: E501
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this ArrayManagementProvider.


        :param provider_type: The provider_type of this ArrayManagementProvider.  # noqa: E501
        :type: str
        """
        allowed_values = ["SMI-S", "REST"]  # noqa: E501
        if provider_type not in allowed_values:
            raise ValueError(
                "Invalid value for `provider_type` ({0}), must be one of {1}"  # noqa: E501
                .format(provider_type, allowed_values)
            )

        self._provider_type = provider_type

    @property
    def use_ssl(self):
        """Gets the use_ssl of this ArrayManagementProvider.  # noqa: E501


        :return: The use_ssl of this ArrayManagementProvider.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this ArrayManagementProvider.


        :param use_ssl: The use_ssl of this ArrayManagementProvider.  # noqa: E501
        :type: bool
        """

        self._use_ssl = use_ssl

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
        if not isinstance(other, ArrayManagementProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
