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

from vplexapi.models.operational_status import OperationalStatus  # noqa: F401,E501
from vplexapi.models.role import Role  # noqa: F401,E501
from vplexapi.models.status import Status  # noqa: F401,E501


class DirectorPort(object):
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
        'address': 'str',
        'status': 'Status',
        'operational_status': 'OperationalStatus',
        'role': 'Role',
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'address': 'address',
        'status': 'status',
        'operational_status': 'operational_status',
        'role': 'role',
        'enabled': 'enabled'
    }

    def __init__(self, name=None, address=None, status=None, operational_status=None, role=None, enabled=None):  # noqa: E501
        """DirectorPort - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._address = None
        self._status = None
        self._operational_status = None
        self._role = None
        self._enabled = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if status is not None:
            self.status = status
        if operational_status is not None:
            self.operational_status = operational_status
        if role is not None:
            self.role = role
        if enabled is not None:
            self.enabled = enabled

    @property
    def name(self):
        """Gets the name of this DirectorPort.  # noqa: E501


        :return: The name of this DirectorPort.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DirectorPort.


        :param name: The name of this DirectorPort.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this DirectorPort.  # noqa: E501


        :return: The address of this DirectorPort.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this DirectorPort.


        :param address: The address of this DirectorPort.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def status(self):
        """Gets the status of this DirectorPort.  # noqa: E501


        :return: The status of this DirectorPort.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DirectorPort.


        :param status: The status of this DirectorPort.  # noqa: E501
        :type: Status
        """

        self._status = status

    @property
    def operational_status(self):
        """Gets the operational_status of this DirectorPort.  # noqa: E501


        :return: The operational_status of this DirectorPort.  # noqa: E501
        :rtype: OperationalStatus
        """
        return self._operational_status

    @operational_status.setter
    def operational_status(self, operational_status):
        """Sets the operational_status of this DirectorPort.


        :param operational_status: The operational_status of this DirectorPort.  # noqa: E501
        :type: OperationalStatus
        """

        self._operational_status = operational_status

    @property
    def role(self):
        """Gets the role of this DirectorPort.  # noqa: E501


        :return: The role of this DirectorPort.  # noqa: E501
        :rtype: Role
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this DirectorPort.


        :param role: The role of this DirectorPort.  # noqa: E501
        :type: Role
        """

        self._role = role

    @property
    def enabled(self):
        """Gets the enabled of this DirectorPort.  # noqa: E501


        :return: The enabled of this DirectorPort.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DirectorPort.


        :param enabled: The enabled of this DirectorPort.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if not isinstance(other, DirectorPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other