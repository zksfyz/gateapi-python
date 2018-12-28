# coding: utf-8

"""
    Gate API v4

    APIv4 futures provides all sorts of futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FuturesAccount(object):
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
        'total': 'str',
        'unrealised_pnl': 'str',
        'position_margin': 'str',
        'order_margin': 'str',
        'available': 'str'
    }

    attribute_map = {
        'total': 'total',
        'unrealised_pnl': 'unrealised_pnl',
        'position_margin': 'position_margin',
        'order_margin': 'order_margin',
        'available': 'available'
    }

    def __init__(self, total=None, unrealised_pnl=None, position_margin=None, order_margin=None, available=None):  # noqa: E501
        """FuturesAccount - a model defined in OpenAPI"""  # noqa: E501

        self._total = None
        self._unrealised_pnl = None
        self._position_margin = None
        self._order_margin = None
        self._available = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if unrealised_pnl is not None:
            self.unrealised_pnl = unrealised_pnl
        if position_margin is not None:
            self.position_margin = position_margin
        if order_margin is not None:
            self.order_margin = order_margin
        if available is not None:
            self.available = available

    @property
    def total(self):
        """Gets the total of this FuturesAccount.  # noqa: E501

        total assets, total = position_margin + order_margin + available  # noqa: E501

        :return: The total of this FuturesAccount.  # noqa: E501
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this FuturesAccount.

        total assets, total = position_margin + order_margin + available  # noqa: E501

        :param total: The total of this FuturesAccount.  # noqa: E501
        :type: str
        """

        self._total = total

    @property
    def unrealised_pnl(self):
        """Gets the unrealised_pnl of this FuturesAccount.  # noqa: E501

        unrealized pnl  # noqa: E501

        :return: The unrealised_pnl of this FuturesAccount.  # noqa: E501
        :rtype: str
        """
        return self._unrealised_pnl

    @unrealised_pnl.setter
    def unrealised_pnl(self, unrealised_pnl):
        """Sets the unrealised_pnl of this FuturesAccount.

        unrealized pnl  # noqa: E501

        :param unrealised_pnl: The unrealised_pnl of this FuturesAccount.  # noqa: E501
        :type: str
        """

        self._unrealised_pnl = unrealised_pnl

    @property
    def position_margin(self):
        """Gets the position_margin of this FuturesAccount.  # noqa: E501

        position margin  # noqa: E501

        :return: The position_margin of this FuturesAccount.  # noqa: E501
        :rtype: str
        """
        return self._position_margin

    @position_margin.setter
    def position_margin(self, position_margin):
        """Sets the position_margin of this FuturesAccount.

        position margin  # noqa: E501

        :param position_margin: The position_margin of this FuturesAccount.  # noqa: E501
        :type: str
        """

        self._position_margin = position_margin

    @property
    def order_margin(self):
        """Gets the order_margin of this FuturesAccount.  # noqa: E501

        order margin of unfinished orders  # noqa: E501

        :return: The order_margin of this FuturesAccount.  # noqa: E501
        :rtype: str
        """
        return self._order_margin

    @order_margin.setter
    def order_margin(self, order_margin):
        """Sets the order_margin of this FuturesAccount.

        order margin of unfinished orders  # noqa: E501

        :param order_margin: The order_margin of this FuturesAccount.  # noqa: E501
        :type: str
        """

        self._order_margin = order_margin

    @property
    def available(self):
        """Gets the available of this FuturesAccount.  # noqa: E501

        available balance to transfer out or trade  # noqa: E501

        :return: The available of this FuturesAccount.  # noqa: E501
        :rtype: str
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this FuturesAccount.

        available balance to transfer out or trade  # noqa: E501

        :param available: The available of this FuturesAccount.  # noqa: E501
        :type: str
        """

        self._available = available

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
        if not isinstance(other, FuturesAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
