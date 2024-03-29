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


class InitiatorPort(object):
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
        'iscsi_name': 'str',
        'port_wwn': 'str',
        'node_wwn': 'str',
        'type': 'str',
        'iops_limit': 'int',
        'bandwidth_limit': 'str',
        'target_ports': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'iscsi_name': 'iscsi_name',
        'port_wwn': 'port_wwn',
        'node_wwn': 'node_wwn',
        'type': 'type',
        'iops_limit': 'iops_limit',
        'bandwidth_limit': 'bandwidth_limit',
        'target_ports': 'target_ports'
    }

    def __init__(self, name=None, iscsi_name=None, port_wwn=None, node_wwn=None, type=None, iops_limit=None, bandwidth_limit=None, target_ports=None):  # noqa: E501
        """InitiatorPort - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._iscsi_name = None
        self._port_wwn = None
        self._node_wwn = None
        self._type = None
        self._iops_limit = None
        self._bandwidth_limit = None
        self._target_ports = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if iscsi_name is not None:
            self.iscsi_name = iscsi_name
        if port_wwn is not None:
            self.port_wwn = port_wwn
        if node_wwn is not None:
            self.node_wwn = node_wwn
        if type is not None:
            self.type = type
        if iops_limit is not None:
            self.iops_limit = iops_limit
        if bandwidth_limit is not None:
            self.bandwidth_limit = bandwidth_limit
        if target_ports is not None:
            self.target_ports = target_ports

    @property
    def name(self):
        """Gets the name of this InitiatorPort.  # noqa: E501


        :return: The name of this InitiatorPort.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InitiatorPort.


        :param name: The name of this InitiatorPort.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def iscsi_name(self):
        """Gets the iscsi_name of this InitiatorPort.  # noqa: E501


        :return: The iscsi_name of this InitiatorPort.  # noqa: E501
        :rtype: str
        """
        return self._iscsi_name

    @iscsi_name.setter
    def iscsi_name(self, iscsi_name):
        """Sets the iscsi_name of this InitiatorPort.


        :param iscsi_name: The iscsi_name of this InitiatorPort.  # noqa: E501
        :type: str
        """

        self._iscsi_name = iscsi_name

    @property
    def port_wwn(self):
        """Gets the port_wwn of this InitiatorPort.  # noqa: E501


        :return: The port_wwn of this InitiatorPort.  # noqa: E501
        :rtype: str
        """
        return self._port_wwn

    @port_wwn.setter
    def port_wwn(self, port_wwn):
        """Sets the port_wwn of this InitiatorPort.


        :param port_wwn: The port_wwn of this InitiatorPort.  # noqa: E501
        :type: str
        """

        self._port_wwn = port_wwn

    @property
    def node_wwn(self):
        """Gets the node_wwn of this InitiatorPort.  # noqa: E501


        :return: The node_wwn of this InitiatorPort.  # noqa: E501
        :rtype: str
        """
        return self._node_wwn

    @node_wwn.setter
    def node_wwn(self, node_wwn):
        """Sets the node_wwn of this InitiatorPort.


        :param node_wwn: The node_wwn of this InitiatorPort.  # noqa: E501
        :type: str
        """

        self._node_wwn = node_wwn

    @property
    def type(self):
        """Gets the type of this InitiatorPort.  # noqa: E501


        :return: The type of this InitiatorPort.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InitiatorPort.


        :param type: The type of this InitiatorPort.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def iops_limit(self):
        """Gets the iops_limit of this InitiatorPort.  # noqa: E501


        :return: The iops_limit of this InitiatorPort.  # noqa: E501
        :rtype: int
        """
        return self._iops_limit

    @iops_limit.setter
    def iops_limit(self, iops_limit):
        """Sets the iops_limit of this InitiatorPort.


        :param iops_limit: The iops_limit of this InitiatorPort.  # noqa: E501
        :type: int
        """

        self._iops_limit = iops_limit

    @property
    def bandwidth_limit(self):
        """Gets the bandwidth_limit of this InitiatorPort.  # noqa: E501


        :return: The bandwidth_limit of this InitiatorPort.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_limit

    @bandwidth_limit.setter
    def bandwidth_limit(self, bandwidth_limit):
        """Sets the bandwidth_limit of this InitiatorPort.


        :param bandwidth_limit: The bandwidth_limit of this InitiatorPort.  # noqa: E501
        :type: str
        """

        self._bandwidth_limit = bandwidth_limit

    @property
    def target_ports(self):
        """Gets the target_ports of this InitiatorPort.  # noqa: E501


        :return: The target_ports of this InitiatorPort.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_ports

    @target_ports.setter
    def target_ports(self, target_ports):
        """Sets the target_ports of this InitiatorPort.


        :param target_ports: The target_ports of this InitiatorPort.  # noqa: E501
        :type: list[str]
        """

        self._target_ports = target_ports

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
        if issubclass(InitiatorPort, dict):
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
        if not isinstance(other, InitiatorPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
