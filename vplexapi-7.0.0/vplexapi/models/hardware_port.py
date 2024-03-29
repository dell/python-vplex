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

from vplexapi.models.role import Role  # noqa: F401,E501
from vplexapi.models.status import Status  # noqa: F401,E501


class HardwarePort(object):
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
        'name': 'str',
        'director': 'str',
        'status': 'Status',
        'address': 'str',
        'role': 'Role'
    }

    attribute_map = {
        'name': 'name',
        'director': 'director',
        'status': 'status',
        'address': 'address',
        'role': 'role'
    }

    def __init__(self, name=None, director=None, status=None, address=None, role=None):  # noqa: E501
        """HardwarePort - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._director = None
        self._status = None
        self._address = None
        self._role = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if director is not None:
            self.director = director
        if status is not None:
            self.status = status
        if address is not None:
            self.address = address
        if role is not None:
            self.role = role

    @property
    def name(self):
        """Gets the name of this HardwarePort.  # noqa: E501


        :return: The name of this HardwarePort.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HardwarePort.


        :param name: The name of this HardwarePort.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def director(self):
        """Gets the director of this HardwarePort.  # noqa: E501


        :return: The director of this HardwarePort.  # noqa: E501
        :rtype: str
        """
        return self._director

    @director.setter
    def director(self, director):
        """Sets the director of this HardwarePort.


        :param director: The director of this HardwarePort.  # noqa: E501
        :type: str
        """

        self._director = director

    @property
    def status(self):
        """Gets the status of this HardwarePort.  # noqa: E501


        :return: The status of this HardwarePort.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HardwarePort.


        :param status: The status of this HardwarePort.  # noqa: E501
        :type: Status
        """

        self._status = status

    @property
    def address(self):
        """Gets the address of this HardwarePort.  # noqa: E501


        :return: The address of this HardwarePort.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this HardwarePort.


        :param address: The address of this HardwarePort.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def role(self):
        """Gets the role of this HardwarePort.  # noqa: E501


        :return: The role of this HardwarePort.  # noqa: E501
        :rtype: Role
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this HardwarePort.


        :param role: The role of this HardwarePort.  # noqa: E501
        :type: Role
        """

        self._role = role

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
        if issubclass(HardwarePort, dict):
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
        if not isinstance(other, HardwarePort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
