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


class AmpPayload(object):
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
        'provider_name': 'str',
        'provider_type': 'str',
        'ip_address': 'str',
        'port': 'int',
        'user_name': 'str',
        'password': 'str',
        'use_ssl': 'bool'
    }

    attribute_map = {
        'provider_name': 'provider_name',
        'provider_type': 'provider_type',
        'ip_address': 'ip_address',
        'port': 'port',
        'user_name': 'user_name',
        'password': 'password',
        'use_ssl': 'use_ssl'
    }

    def __init__(self, provider_name=None, provider_type=None, ip_address=None, port=None, user_name=None, password=None, use_ssl=None):  # noqa: E501
        """AmpPayload - a model defined in Swagger"""  # noqa: E501

        self._provider_name = None
        self._provider_type = None
        self._ip_address = None
        self._port = None
        self._user_name = None
        self._password = None
        self._use_ssl = None
        self.discriminator = None

        self.provider_name = provider_name
        self.provider_type = provider_type
        self.ip_address = ip_address
        self.port = port
        self.user_name = user_name
        self.password = password
        self.use_ssl = use_ssl

    @property
    def provider_name(self):
        """Gets the provider_name of this AmpPayload.  # noqa: E501


        :return: The provider_name of this AmpPayload.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this AmpPayload.


        :param provider_name: The provider_name of this AmpPayload.  # noqa: E501
        :type: str
        """
        if provider_name is None:
            raise ValueError("Invalid value for `provider_name`, must not be `None`")  # noqa: E501

        self._provider_name = provider_name

    @property
    def provider_type(self):
        """Gets the provider_type of this AmpPayload.  # noqa: E501


        :return: The provider_type of this AmpPayload.  # noqa: E501
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this AmpPayload.


        :param provider_type: The provider_type of this AmpPayload.  # noqa: E501
        :type: str
        """
        if provider_type is None:
            raise ValueError("Invalid value for `provider_type`, must not be `None`")  # noqa: E501

        self._provider_type = provider_type

    @property
    def ip_address(self):
        """Gets the ip_address of this AmpPayload.  # noqa: E501


        :return: The ip_address of this AmpPayload.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this AmpPayload.


        :param ip_address: The ip_address of this AmpPayload.  # noqa: E501
        :type: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def port(self):
        """Gets the port of this AmpPayload.  # noqa: E501


        :return: The port of this AmpPayload.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this AmpPayload.


        :param port: The port of this AmpPayload.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def user_name(self):
        """Gets the user_name of this AmpPayload.  # noqa: E501


        :return: The user_name of this AmpPayload.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AmpPayload.


        :param user_name: The user_name of this AmpPayload.  # noqa: E501
        :type: str
        """
        if user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this AmpPayload.  # noqa: E501


        :return: The password of this AmpPayload.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AmpPayload.


        :param password: The password of this AmpPayload.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def use_ssl(self):
        """Gets the use_ssl of this AmpPayload.  # noqa: E501


        :return: The use_ssl of this AmpPayload.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this AmpPayload.


        :param use_ssl: The use_ssl of this AmpPayload.  # noqa: E501
        :type: bool
        """
        if use_ssl is None:
            raise ValueError("Invalid value for `use_ssl`, must not be `None`")  # noqa: E501

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
        if issubclass(AmpPayload, dict):
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
        if not isinstance(other, AmpPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
