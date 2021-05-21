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

from vplexapi.models.port_exports import PortExports  # noqa: F401,E501


class Port(object):
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
        'director': 'str',
        'name': 'str',
        'enabled': 'bool',
        'iscsi_name': 'str',
        'port_wwn': 'str',
        'node_wwn': 'str',
        'export_status': 'str',
        'discovered_initiators': 'list[str]',
        'director_id': 'str',
        'exports': 'list[PortExports]'
    }

    attribute_map = {
        'director': 'director',
        'name': 'name',
        'enabled': 'enabled',
        'iscsi_name': 'iscsi_name',
        'port_wwn': 'port_wwn',
        'node_wwn': 'node_wwn',
        'export_status': 'export_status',
        'discovered_initiators': 'discovered_initiators',
        'director_id': 'director_id',
        'exports': 'exports'
    }

    def __init__(self, director=None, name=None, enabled=None, iscsi_name=None, port_wwn=None, node_wwn=None, export_status=None, discovered_initiators=None, director_id=None, exports=None):  # noqa: E501
        """Port - a model defined in Swagger"""  # noqa: E501

        self._director = None
        self._name = None
        self._enabled = None
        self._iscsi_name = None
        self._port_wwn = None
        self._node_wwn = None
        self._export_status = None
        self._discovered_initiators = None
        self._director_id = None
        self._exports = None
        self.discriminator = None

        if director is not None:
            self.director = director
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if iscsi_name is not None:
            self.iscsi_name = iscsi_name
        if port_wwn is not None:
            self.port_wwn = port_wwn
        if node_wwn is not None:
            self.node_wwn = node_wwn
        if export_status is not None:
            self.export_status = export_status
        if discovered_initiators is not None:
            self.discovered_initiators = discovered_initiators
        if director_id is not None:
            self.director_id = director_id
        if exports is not None:
            self.exports = exports

    @property
    def director(self):
        """Gets the director of this Port.  # noqa: E501


        :return: The director of this Port.  # noqa: E501
        :rtype: str
        """
        return self._director

    @director.setter
    def director(self, director):
        """Sets the director of this Port.


        :param director: The director of this Port.  # noqa: E501
        :type: str
        """

        self._director = director

    @property
    def name(self):
        """Gets the name of this Port.  # noqa: E501


        :return: The name of this Port.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Port.


        :param name: The name of this Port.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this Port.  # noqa: E501


        :return: The enabled of this Port.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Port.


        :param enabled: The enabled of this Port.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def iscsi_name(self):
        """Gets the iscsi_name of this Port.  # noqa: E501


        :return: The iscsi_name of this Port.  # noqa: E501
        :rtype: str
        """
        return self._iscsi_name

    @iscsi_name.setter
    def iscsi_name(self, iscsi_name):
        """Sets the iscsi_name of this Port.


        :param iscsi_name: The iscsi_name of this Port.  # noqa: E501
        :type: str
        """

        self._iscsi_name = iscsi_name

    @property
    def port_wwn(self):
        """Gets the port_wwn of this Port.  # noqa: E501


        :return: The port_wwn of this Port.  # noqa: E501
        :rtype: str
        """
        return self._port_wwn

    @port_wwn.setter
    def port_wwn(self, port_wwn):
        """Sets the port_wwn of this Port.


        :param port_wwn: The port_wwn of this Port.  # noqa: E501
        :type: str
        """

        self._port_wwn = port_wwn

    @property
    def node_wwn(self):
        """Gets the node_wwn of this Port.  # noqa: E501


        :return: The node_wwn of this Port.  # noqa: E501
        :rtype: str
        """
        return self._node_wwn

    @node_wwn.setter
    def node_wwn(self, node_wwn):
        """Sets the node_wwn of this Port.


        :param node_wwn: The node_wwn of this Port.  # noqa: E501
        :type: str
        """

        self._node_wwn = node_wwn

    @property
    def export_status(self):
        """Gets the export_status of this Port.  # noqa: E501


        :return: The export_status of this Port.  # noqa: E501
        :rtype: str
        """
        return self._export_status

    @export_status.setter
    def export_status(self, export_status):
        """Sets the export_status of this Port.


        :param export_status: The export_status of this Port.  # noqa: E501
        :type: str
        """

        self._export_status = export_status

    @property
    def discovered_initiators(self):
        """Gets the discovered_initiators of this Port.  # noqa: E501


        :return: The discovered_initiators of this Port.  # noqa: E501
        :rtype: list[str]
        """
        return self._discovered_initiators

    @discovered_initiators.setter
    def discovered_initiators(self, discovered_initiators):
        """Sets the discovered_initiators of this Port.


        :param discovered_initiators: The discovered_initiators of this Port.  # noqa: E501
        :type: list[str]
        """

        self._discovered_initiators = discovered_initiators

    @property
    def director_id(self):
        """Gets the director_id of this Port.  # noqa: E501


        :return: The director_id of this Port.  # noqa: E501
        :rtype: str
        """
        return self._director_id

    @director_id.setter
    def director_id(self, director_id):
        """Sets the director_id of this Port.


        :param director_id: The director_id of this Port.  # noqa: E501
        :type: str
        """

        self._director_id = director_id

    @property
    def exports(self):
        """Gets the exports of this Port.  # noqa: E501


        :return: The exports of this Port.  # noqa: E501
        :rtype: list[PortExports]
        """
        return self._exports

    @exports.setter
    def exports(self, exports):
        """Sets the exports of this Port.


        :param exports: The exports of this Port.  # noqa: E501
        :type: list[PortExports]
        """

        self._exports = exports

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
        if issubclass(Port, dict):
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
        if not isinstance(other, Port):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other