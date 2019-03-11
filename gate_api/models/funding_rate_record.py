# coding: utf-8

"""
    Gate API v4

    APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    OpenAPI spec version: 4.5.1
    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FundingRateRecord(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        't': 'int',
        'r': 'str'
    }

    attribute_map = {
        't': 't',
        'r': 'r'
    }

    def __init__(self, t=None, r=None):  # noqa: E501
        """FundingRateRecord - a model defined in OpenAPI"""  # noqa: E501

        self._t = None
        self._r = None
        self.discriminator = None

        if t is not None:
            self.t = t
        if r is not None:
            self.r = r

    @property
    def t(self):
        """Gets the t of this FundingRateRecord.  # noqa: E501

        Unix timestamp in seconds  # noqa: E501

        :return: The t of this FundingRateRecord.  # noqa: E501
        :rtype: int
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this FundingRateRecord.

        Unix timestamp in seconds  # noqa: E501

        :param t: The t of this FundingRateRecord.  # noqa: E501
        :type: int
        """

        self._t = t

    @property
    def r(self):
        """Gets the r of this FundingRateRecord.  # noqa: E501

        Funding rate  # noqa: E501

        :return: The r of this FundingRateRecord.  # noqa: E501
        :rtype: str
        """
        return self._r

    @r.setter
    def r(self, r):
        """Sets the r of this FundingRateRecord.

        Funding rate  # noqa: E501

        :param r: The r of this FundingRateRecord.  # noqa: E501
        :type: str
        """

        self._r = r

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, FundingRateRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
