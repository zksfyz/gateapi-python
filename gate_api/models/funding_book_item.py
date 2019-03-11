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


class FundingBookItem(object):
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
        'rate': 'str',
        'amount': 'str',
        'days': 'int'
    }

    attribute_map = {
        'rate': 'rate',
        'amount': 'amount',
        'days': 'days'
    }

    def __init__(self, rate=None, amount=None, days=None):  # noqa: E501
        """FundingBookItem - a model defined in OpenAPI"""  # noqa: E501

        self._rate = None
        self._amount = None
        self._days = None
        self.discriminator = None

        if rate is not None:
            self.rate = rate
        if amount is not None:
            self.amount = amount
        if days is not None:
            self.days = days

    @property
    def rate(self):
        """Gets the rate of this FundingBookItem.  # noqa: E501

        Loan rate  # noqa: E501

        :return: The rate of this FundingBookItem.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this FundingBookItem.

        Loan rate  # noqa: E501

        :param rate: The rate of this FundingBookItem.  # noqa: E501
        :type: str
        """

        self._rate = rate

    @property
    def amount(self):
        """Gets the amount of this FundingBookItem.  # noqa: E501

        Borrowable amount  # noqa: E501

        :return: The amount of this FundingBookItem.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FundingBookItem.

        Borrowable amount  # noqa: E501

        :param amount: The amount of this FundingBookItem.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def days(self):
        """Gets the days of this FundingBookItem.  # noqa: E501

        How long the loan should be repaid  # noqa: E501

        :return: The days of this FundingBookItem.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this FundingBookItem.

        How long the loan should be repaid  # noqa: E501

        :param days: The days of this FundingBookItem.  # noqa: E501
        :type: int
        """

        self._days = days

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
        if not isinstance(other, FundingBookItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
