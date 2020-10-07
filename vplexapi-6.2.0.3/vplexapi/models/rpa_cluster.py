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


class RPACluster(object):
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
        'vplex_cluster': 'str',
        'rp_health_indications': 'list[str]',
        'rp_health_status': 'str',
        'rpa_host': 'str'
    }

    attribute_map = {
        'name': 'name',
        'vplex_cluster': 'vplex_cluster',
        'rp_health_indications': 'rp_health_indications',
        'rp_health_status': 'rp_health_status',
        'rpa_host': 'rpa_host'
    }

    def __init__(self, name=None, vplex_cluster=None, rp_health_indications=None, rp_health_status=None, rpa_host=None):  # noqa: E501
        """RPACluster - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._vplex_cluster = None
        self._rp_health_indications = None
        self._rp_health_status = None
        self._rpa_host = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if vplex_cluster is not None:
            self.vplex_cluster = vplex_cluster
        if rp_health_indications is not None:
            self.rp_health_indications = rp_health_indications
        if rp_health_status is not None:
            self.rp_health_status = rp_health_status
        if rpa_host is not None:
            self.rpa_host = rpa_host

    @property
    def name(self):
        """Gets the name of this RPACluster.  # noqa: E501


        :return: The name of this RPACluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RPACluster.


        :param name: The name of this RPACluster.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def vplex_cluster(self):
        """Gets the vplex_cluster of this RPACluster.  # noqa: E501


        :return: The vplex_cluster of this RPACluster.  # noqa: E501
        :rtype: str
        """
        return self._vplex_cluster

    @vplex_cluster.setter
    def vplex_cluster(self, vplex_cluster):
        """Sets the vplex_cluster of this RPACluster.


        :param vplex_cluster: The vplex_cluster of this RPACluster.  # noqa: E501
        :type: str
        """

        self._vplex_cluster = vplex_cluster

    @property
    def rp_health_indications(self):
        """Gets the rp_health_indications of this RPACluster.  # noqa: E501


        :return: The rp_health_indications of this RPACluster.  # noqa: E501
        :rtype: list[str]
        """
        return self._rp_health_indications

    @rp_health_indications.setter
    def rp_health_indications(self, rp_health_indications):
        """Sets the rp_health_indications of this RPACluster.


        :param rp_health_indications: The rp_health_indications of this RPACluster.  # noqa: E501
        :type: list[str]
        """

        self._rp_health_indications = rp_health_indications

    @property
    def rp_health_status(self):
        """Gets the rp_health_status of this RPACluster.  # noqa: E501


        :return: The rp_health_status of this RPACluster.  # noqa: E501
        :rtype: str
        """
        return self._rp_health_status

    @rp_health_status.setter
    def rp_health_status(self, rp_health_status):
        """Sets the rp_health_status of this RPACluster.


        :param rp_health_status: The rp_health_status of this RPACluster.  # noqa: E501
        :type: str
        """

        self._rp_health_status = rp_health_status

    @property
    def rpa_host(self):
        """Gets the rpa_host of this RPACluster.  # noqa: E501


        :return: The rpa_host of this RPACluster.  # noqa: E501
        :rtype: str
        """
        return self._rpa_host

    @rpa_host.setter
    def rpa_host(self, rpa_host):
        """Sets the rpa_host of this RPACluster.


        :param rpa_host: The rpa_host of this RPACluster.  # noqa: E501
        :type: str
        """

        self._rpa_host = rpa_host

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
        if not isinstance(other, RPACluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
