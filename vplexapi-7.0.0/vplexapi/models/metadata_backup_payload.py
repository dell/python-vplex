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


class MetadataBackupPayload(object):
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
        'backup_volumes': 'list[str]',
        'hours': 'int',
        'minutes': 'int'
    }

    attribute_map = {
        'backup_volumes': 'backup_volumes',
        'hours': 'hours',
        'minutes': 'minutes'
    }

    def __init__(self, backup_volumes=None, hours=None, minutes=None):  # noqa: E501
        """MetadataBackupPayload - a model defined in Swagger"""  # noqa: E501

        self._backup_volumes = None
        self._hours = None
        self._minutes = None
        self.discriminator = None

        if backup_volumes is not None:
            self.backup_volumes = backup_volumes
        self.hours = hours
        self.minutes = minutes

    @property
    def backup_volumes(self):
        """Gets the backup_volumes of this MetadataBackupPayload.  # noqa: E501


        :return: The backup_volumes of this MetadataBackupPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._backup_volumes

    @backup_volumes.setter
    def backup_volumes(self, backup_volumes):
        """Sets the backup_volumes of this MetadataBackupPayload.


        :param backup_volumes: The backup_volumes of this MetadataBackupPayload.  # noqa: E501
        :type: list[str]
        """

        self._backup_volumes = backup_volumes

    @property
    def hours(self):
        """Gets the hours of this MetadataBackupPayload.  # noqa: E501


        :return: The hours of this MetadataBackupPayload.  # noqa: E501
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this MetadataBackupPayload.


        :param hours: The hours of this MetadataBackupPayload.  # noqa: E501
        :type: int
        """
        if hours is None:
            raise ValueError("Invalid value for `hours`, must not be `None`")  # noqa: E501

        self._hours = hours

    @property
    def minutes(self):
        """Gets the minutes of this MetadataBackupPayload.  # noqa: E501


        :return: The minutes of this MetadataBackupPayload.  # noqa: E501
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this MetadataBackupPayload.


        :param minutes: The minutes of this MetadataBackupPayload.  # noqa: E501
        :type: int
        """
        if minutes is None:
            raise ValueError("Invalid value for `minutes`, must not be `None`")  # noqa: E501

        self._minutes = minutes

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
        if issubclass(MetadataBackupPayload, dict):
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
        if not isinstance(other, MetadataBackupPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
