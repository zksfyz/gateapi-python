# coding: utf-8

"""
    Gate API v4

    APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class CurrencyPair(object):
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
        'id': 'str',
        'base': 'str',
        'quote': 'str',
        'fee': 'str',
        'min_base_amount': 'str',
        'min_quote_amount': 'str',
        'amount_precision': 'int',
        'precision': 'int',
        'trade_status': 'str',
        'etf_net_value': 'str',
        'etf_pre_net_value': 'str',
        'etf_pre_timestamp': 'int',
        'etf_leverage': 'str',
    }

    attribute_map = {
        'id': 'id',
        'base': 'base',
        'quote': 'quote',
        'fee': 'fee',
        'min_base_amount': 'min_base_amount',
        'min_quote_amount': 'min_quote_amount',
        'amount_precision': 'amount_precision',
        'precision': 'precision',
        'trade_status': 'trade_status',
        'etf_net_value': 'etf_net_value',
        'etf_pre_net_value': 'etf_pre_net_value',
        'etf_pre_timestamp': 'etf_pre_timestamp',
        'etf_leverage': 'etf_leverage',
    }

    def __init__(
        self,
        id=None,
        base=None,
        quote=None,
        fee=None,
        min_base_amount=None,
        min_quote_amount=None,
        amount_precision=None,
        precision=None,
        trade_status=None,
        etf_net_value=None,
        etf_pre_net_value=None,
        etf_pre_timestamp=None,
        etf_leverage=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, str, str, int, int, str, str, str, int, str, Configuration) -> None
        """CurrencyPair - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._base = None
        self._quote = None
        self._fee = None
        self._min_base_amount = None
        self._min_quote_amount = None
        self._amount_precision = None
        self._precision = None
        self._trade_status = None
        self._etf_net_value = None
        self._etf_pre_net_value = None
        self._etf_pre_timestamp = None
        self._etf_leverage = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if base is not None:
            self.base = base
        if quote is not None:
            self.quote = quote
        if fee is not None:
            self.fee = fee
        if min_base_amount is not None:
            self.min_base_amount = min_base_amount
        if min_quote_amount is not None:
            self.min_quote_amount = min_quote_amount
        if amount_precision is not None:
            self.amount_precision = amount_precision
        if precision is not None:
            self.precision = precision
        if trade_status is not None:
            self.trade_status = trade_status
        if etf_net_value is not None:
            self.etf_net_value = etf_net_value
        if etf_pre_net_value is not None:
            self.etf_pre_net_value = etf_pre_net_value
        if etf_pre_timestamp is not None:
            self.etf_pre_timestamp = etf_pre_timestamp
        if etf_leverage is not None:
            self.etf_leverage = etf_leverage

    @property
    def id(self):
        """Gets the id of this CurrencyPair.  # noqa: E501

        Currency pair  # noqa: E501

        :return: The id of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CurrencyPair.

        Currency pair  # noqa: E501

        :param id: The id of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def base(self):
        """Gets the base of this CurrencyPair.  # noqa: E501

        Base currency  # noqa: E501

        :return: The base of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this CurrencyPair.

        Base currency  # noqa: E501

        :param base: The base of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._base = base

    @property
    def quote(self):
        """Gets the quote of this CurrencyPair.  # noqa: E501

        Quote currency  # noqa: E501

        :return: The quote of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this CurrencyPair.

        Quote currency  # noqa: E501

        :param quote: The quote of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._quote = quote

    @property
    def fee(self):
        """Gets the fee of this CurrencyPair.  # noqa: E501

        Trading fee  # noqa: E501

        :return: The fee of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this CurrencyPair.

        Trading fee  # noqa: E501

        :param fee: The fee of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._fee = fee

    @property
    def min_base_amount(self):
        """Gets the min_base_amount of this CurrencyPair.  # noqa: E501

        Minimum amount of base currency to trade, `null` means no limit  # noqa: E501

        :return: The min_base_amount of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._min_base_amount

    @min_base_amount.setter
    def min_base_amount(self, min_base_amount):
        """Sets the min_base_amount of this CurrencyPair.

        Minimum amount of base currency to trade, `null` means no limit  # noqa: E501

        :param min_base_amount: The min_base_amount of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._min_base_amount = min_base_amount

    @property
    def min_quote_amount(self):
        """Gets the min_quote_amount of this CurrencyPair.  # noqa: E501

        Minimum amount of quote currency to trade, `null` means no limit  # noqa: E501

        :return: The min_quote_amount of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._min_quote_amount

    @min_quote_amount.setter
    def min_quote_amount(self, min_quote_amount):
        """Sets the min_quote_amount of this CurrencyPair.

        Minimum amount of quote currency to trade, `null` means no limit  # noqa: E501

        :param min_quote_amount: The min_quote_amount of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._min_quote_amount = min_quote_amount

    @property
    def amount_precision(self):
        """Gets the amount_precision of this CurrencyPair.  # noqa: E501

        Amount scale  # noqa: E501

        :return: The amount_precision of this CurrencyPair.  # noqa: E501
        :rtype: int
        """
        return self._amount_precision

    @amount_precision.setter
    def amount_precision(self, amount_precision):
        """Sets the amount_precision of this CurrencyPair.

        Amount scale  # noqa: E501

        :param amount_precision: The amount_precision of this CurrencyPair.  # noqa: E501
        :type: int
        """

        self._amount_precision = amount_precision

    @property
    def precision(self):
        """Gets the precision of this CurrencyPair.  # noqa: E501

        Price scale  # noqa: E501

        :return: The precision of this CurrencyPair.  # noqa: E501
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this CurrencyPair.

        Price scale  # noqa: E501

        :param precision: The precision of this CurrencyPair.  # noqa: E501
        :type: int
        """

        self._precision = precision

    @property
    def trade_status(self):
        """Gets the trade_status of this CurrencyPair.  # noqa: E501

        How currency pair can be traded  - untradable: cannot be bought or sold - buyable: can be bought - sellable: can be sold - tradable: can be bought or sold  # noqa: E501

        :return: The trade_status of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._trade_status

    @trade_status.setter
    def trade_status(self, trade_status):
        """Sets the trade_status of this CurrencyPair.

        How currency pair can be traded  - untradable: cannot be bought or sold - buyable: can be bought - sellable: can be sold - tradable: can be bought or sold  # noqa: E501

        :param trade_status: The trade_status of this CurrencyPair.  # noqa: E501
        :type: str
        """
        allowed_values = ["untradable", "buyable", "sellable", "tradable"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and trade_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `trade_status` ({0}), must be one of {1}".format(  # noqa: E501
                    trade_status, allowed_values
                )
            )

        self._trade_status = trade_status

    @property
    def etf_net_value(self):
        """Gets the etf_net_value of this CurrencyPair.  # noqa: E501

        ETF net value  # noqa: E501

        :return: The etf_net_value of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._etf_net_value

    @etf_net_value.setter
    def etf_net_value(self, etf_net_value):
        """Sets the etf_net_value of this CurrencyPair.

        ETF net value  # noqa: E501

        :param etf_net_value: The etf_net_value of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._etf_net_value = etf_net_value

    @property
    def etf_pre_net_value(self):
        """Gets the etf_pre_net_value of this CurrencyPair.  # noqa: E501

        ETF previous net value at re-balancing time  # noqa: E501

        :return: The etf_pre_net_value of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._etf_pre_net_value

    @etf_pre_net_value.setter
    def etf_pre_net_value(self, etf_pre_net_value):
        """Sets the etf_pre_net_value of this CurrencyPair.

        ETF previous net value at re-balancing time  # noqa: E501

        :param etf_pre_net_value: The etf_pre_net_value of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._etf_pre_net_value = etf_pre_net_value

    @property
    def etf_pre_timestamp(self):
        """Gets the etf_pre_timestamp of this CurrencyPair.  # noqa: E501

        ETF previous re-balancing time  # noqa: E501

        :return: The etf_pre_timestamp of this CurrencyPair.  # noqa: E501
        :rtype: int
        """
        return self._etf_pre_timestamp

    @etf_pre_timestamp.setter
    def etf_pre_timestamp(self, etf_pre_timestamp):
        """Sets the etf_pre_timestamp of this CurrencyPair.

        ETF previous re-balancing time  # noqa: E501

        :param etf_pre_timestamp: The etf_pre_timestamp of this CurrencyPair.  # noqa: E501
        :type: int
        """

        self._etf_pre_timestamp = etf_pre_timestamp

    @property
    def etf_leverage(self):
        """Gets the etf_leverage of this CurrencyPair.  # noqa: E501

        ETF current leverage  # noqa: E501

        :return: The etf_leverage of this CurrencyPair.  # noqa: E501
        :rtype: str
        """
        return self._etf_leverage

    @etf_leverage.setter
    def etf_leverage(self, etf_leverage):
        """Sets the etf_leverage of this CurrencyPair.

        ETF current leverage  # noqa: E501

        :param etf_leverage: The etf_leverage of this CurrencyPair.  # noqa: E501
        :type: str
        """

        self._etf_leverage = etf_leverage

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, CurrencyPair):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrencyPair):
            return True

        return self.to_dict() != other.to_dict()
