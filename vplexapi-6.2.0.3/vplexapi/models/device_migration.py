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


class DeviceMigration(object):
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
        'source': 'str',
        'target': 'str',
        'from_cluster': 'str',
        'to_cluster': 'str',
        'start_time': 'str',
        'status': 'str',
        'percentage_done': 'int',
        'transfer_size': 'int',
        'type': 'str',
        'source_exported': 'bool',
        'target_exported': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'source': 'source',
        'target': 'target',
        'from_cluster': 'from_cluster',
        'to_cluster': 'to_cluster',
        'start_time': 'start_time',
        'status': 'status',
        'percentage_done': 'percentage_done',
        'transfer_size': 'transfer_size',
        'type': 'type',
        'source_exported': 'source_exported',
        'target_exported': 'target_exported'
    }

    def __init__(self, name=None, source=None, target=None, from_cluster=None, to_cluster=None, start_time=None, status=None, percentage_done=None, transfer_size=None, type=None, source_exported=None, target_exported=None):  # noqa: E501
        """DeviceMigration - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._source = None
        self._target = None
        self._from_cluster = None
        self._to_cluster = None
        self._start_time = None
        self._status = None
        self._percentage_done = None
        self._transfer_size = None
        self._type = None
        self._source_exported = None
        self._target_exported = None
        self.discriminator = None

        self.name = name
        if source is not None:
            self.source = source
        if target is not None:
            self.target = target
        if from_cluster is not None:
            self.from_cluster = from_cluster
        if to_cluster is not None:
            self.to_cluster = to_cluster
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if percentage_done is not None:
            self.percentage_done = percentage_done
        if transfer_size is not None:
            self.transfer_size = transfer_size
        if type is not None:
            self.type = type
        if source_exported is not None:
            self.source_exported = source_exported
        if target_exported is not None:
            self.target_exported = target_exported

    @property
    def name(self):
        """Gets the name of this DeviceMigration.  # noqa: E501


        :return: The name of this DeviceMigration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceMigration.


        :param name: The name of this DeviceMigration.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def source(self):
        """Gets the source of this DeviceMigration.  # noqa: E501


        :return: The source of this DeviceMigration.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DeviceMigration.


        :param source: The source of this DeviceMigration.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def target(self):
        """Gets the target of this DeviceMigration.  # noqa: E501


        :return: The target of this DeviceMigration.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this DeviceMigration.


        :param target: The target of this DeviceMigration.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def from_cluster(self):
        """Gets the from_cluster of this DeviceMigration.  # noqa: E501


        :return: The from_cluster of this DeviceMigration.  # noqa: E501
        :rtype: str
        """
        return self._from_cluster

    @from_cluster.setter
    def from_cluster(self, from_cluster):
        """Sets the from_cluster of this DeviceMigration.


        :param from_cluster: The from_cluster of this DeviceMigration.  # noqa: E501
        :type: str
        """

        self._from_cluster = from_cluster

    @property
    def to_cluster(self):
        """Gets the to_cluster of this DeviceMigration.  # noqa: E501


        :return: The to_cluster of this DeviceMigration.  # noqa: E501
        :rtype: str
        """
        return self._to_cluster

    @to_cluster.setter
    def to_cluster(self, to_cluster):
        """Sets the to_cluster of this DeviceMigration.


        :param to_cluster: The to_cluster of this DeviceMigration.  # noqa: E501
        :type: str
        """

        self._to_cluster = to_cluster

    @property
    def start_time(self):
        """Gets the start_time of this DeviceMigration.  # noqa: E501


        :return: The start_time of this DeviceMigration.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DeviceMigration.


        :param start_time: The start_time of this DeviceMigration.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this DeviceMigration.  # noqa: E501


        :return: The status of this DeviceMigration.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeviceMigration.


        :param status: The status of this DeviceMigration.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def percentage_done(self):
        """Gets the percentage_done of this DeviceMigration.  # noqa: E501


        :return: The percentage_done of this DeviceMigration.  # noqa: E501
        :rtype: int
        """
        return self._percentage_done

    @percentage_done.setter
    def percentage_done(self, percentage_done):
        """Sets the percentage_done of this DeviceMigration.


        :param percentage_done: The percentage_done of this DeviceMigration.  # noqa: E501
        :type: int
        """

        self._percentage_done = percentage_done

    @property
    def transfer_size(self):
        """Gets the transfer_size of this DeviceMigration.  # noqa: E501


        :return: The transfer_size of this DeviceMigration.  # noqa: E501
        :rtype: int
        """
        return self._transfer_size

    @transfer_size.setter
    def transfer_size(self, transfer_size):
        """Sets the transfer_size of this DeviceMigration.


        :param transfer_size: The transfer_size of this DeviceMigration.  # noqa: E501
        :type: int
        """

        self._transfer_size = transfer_size

    @property
    def type(self):
        """Gets the type of this DeviceMigration.  # noqa: E501


        :return: The type of this DeviceMigration.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceMigration.


        :param type: The type of this DeviceMigration.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def source_exported(self):
        """Gets the source_exported of this DeviceMigration.  # noqa: E501


        :return: The source_exported of this DeviceMigration.  # noqa: E501
        :rtype: bool
        """
        return self._source_exported

    @source_exported.setter
    def source_exported(self, source_exported):
        """Sets the source_exported of this DeviceMigration.


        :param source_exported: The source_exported of this DeviceMigration.  # noqa: E501
        :type: bool
        """

        self._source_exported = source_exported

    @property
    def target_exported(self):
        """Gets the target_exported of this DeviceMigration.  # noqa: E501


        :return: The target_exported of this DeviceMigration.  # noqa: E501
        :rtype: bool
        """
        return self._target_exported

    @target_exported.setter
    def target_exported(self, target_exported):
        """Sets the target_exported of this DeviceMigration.


        :param target_exported: The target_exported of this DeviceMigration.  # noqa: E501
        :type: bool
        """

        self._target_exported = target_exported

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
        if not isinstance(other, DeviceMigration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
