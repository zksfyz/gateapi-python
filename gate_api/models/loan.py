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


class Loan(object):
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
        'create_time': 'str',
        'expire_time': 'str',
        'status': 'str',
        'side': 'str',
        'currency': 'str',
        'rate': 'str',
        'amount': 'str',
        'days': 'int',
        'auto_renew': 'bool',
        'currency_pair': 'str',
        'left': 'str',
        'repaid': 'str',
        'paid_interest': 'str',
        'unpaid_interest': 'str',
        'fee_rate': 'str',
        'orig_id': 'str',
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'expire_time': 'expire_time',
        'status': 'status',
        'side': 'side',
        'currency': 'currency',
        'rate': 'rate',
        'amount': 'amount',
        'days': 'days',
        'auto_renew': 'auto_renew',
        'currency_pair': 'currency_pair',
        'left': 'left',
        'repaid': 'repaid',
        'paid_interest': 'paid_interest',
        'unpaid_interest': 'unpaid_interest',
        'fee_rate': 'fee_rate',
        'orig_id': 'orig_id',
    }

    def __init__(
        self,
        id=None,
        create_time=None,
        expire_time=None,
        status=None,
        side=None,
        currency=None,
        rate=None,
        amount=None,
        days=None,
        auto_renew=False,
        currency_pair=None,
        left=None,
        repaid=None,
        paid_interest=None,
        unpaid_interest=None,
        fee_rate=None,
        orig_id=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, str, str, str, str, int, bool, str, str, str, str, str, str, str, Configuration) -> None
        """Loan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._expire_time = None
        self._status = None
        self._side = None
        self._currency = None
        self._rate = None
        self._amount = None
        self._days = None
        self._auto_renew = None
        self._currency_pair = None
        self._left = None
        self._repaid = None
        self._paid_interest = None
        self._unpaid_interest = None
        self._fee_rate = None
        self._orig_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if expire_time is not None:
            self.expire_time = expire_time
        if status is not None:
            self.status = status
        self.side = side
        self.currency = currency
        if rate is not None:
            self.rate = rate
        self.amount = amount
        self.days = days
        if auto_renew is not None:
            self.auto_renew = auto_renew
        if currency_pair is not None:
            self.currency_pair = currency_pair
        if left is not None:
            self.left = left
        if repaid is not None:
            self.repaid = repaid
        if paid_interest is not None:
            self.paid_interest = paid_interest
        if unpaid_interest is not None:
            self.unpaid_interest = unpaid_interest
        if fee_rate is not None:
            self.fee_rate = fee_rate
        if orig_id is not None:
            self.orig_id = orig_id

    @property
    def id(self):
        """Gets the id of this Loan.  # noqa: E501

        Loan ID  # noqa: E501

        :return: The id of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Loan.

        Loan ID  # noqa: E501

        :param id: The id of this Loan.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this Loan.  # noqa: E501

        Creation time  # noqa: E501

        :return: The create_time of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Loan.

        Creation time  # noqa: E501

        :param create_time: The create_time of this Loan.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def expire_time(self):
        """Gets the expire_time of this Loan.  # noqa: E501

        Repay time of the loan. No value will be returned for lending loan  # noqa: E501

        :return: The expire_time of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this Loan.

        Repay time of the loan. No value will be returned for lending loan  # noqa: E501

        :param expire_time: The expire_time of this Loan.  # noqa: E501
        :type: str
        """

        self._expire_time = expire_time

    @property
    def status(self):
        """Gets the status of this Loan.  # noqa: E501

        Loan status  open - not fully loaned loaned - all loaned out for lending loan; loaned in for borrowing side finished - loan is finished, either being all repaid or cancelled by the lender auto_repaid - automatically repaid by the system  # noqa: E501

        :return: The status of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Loan.

        Loan status  open - not fully loaned loaned - all loaned out for lending loan; loaned in for borrowing side finished - loan is finished, either being all repaid or cancelled by the lender auto_repaid - automatically repaid by the system  # noqa: E501

        :param status: The status of this Loan.  # noqa: E501
        :type: str
        """
        allowed_values = ["open", "loaned", "finished", "auto_repaid"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(status, allowed_values)  # noqa: E501
            )

        self._status = status

    @property
    def side(self):
        """Gets the side of this Loan.  # noqa: E501

        Loan side  # noqa: E501

        :return: The side of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this Loan.

        Loan side  # noqa: E501

        :param side: The side of this Loan.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and side is None:  # noqa: E501
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501
        allowed_values = ["lend", "borrow"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and side not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `side` ({0}), must be one of {1}".format(side, allowed_values)  # noqa: E501
            )

        self._side = side

    @property
    def currency(self):
        """Gets the currency of this Loan.  # noqa: E501

        Loan currency  # noqa: E501

        :return: The currency of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Loan.

        Loan currency  # noqa: E501

        :param currency: The currency of this Loan.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def rate(self):
        """Gets the rate of this Loan.  # noqa: E501

        Loan rate. Only rates in [0.0002, 0.002] are supported.  Not required in lending. Market rate calculated from recent rates will be used if not set  # noqa: E501

        :return: The rate of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this Loan.

        Loan rate. Only rates in [0.0002, 0.002] are supported.  Not required in lending. Market rate calculated from recent rates will be used if not set  # noqa: E501

        :param rate: The rate of this Loan.  # noqa: E501
        :type: str
        """

        self._rate = rate

    @property
    def amount(self):
        """Gets the amount of this Loan.  # noqa: E501

        Loan amount  # noqa: E501

        :return: The amount of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Loan.

        Loan amount  # noqa: E501

        :param amount: The amount of this Loan.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def days(self):
        """Gets the days of this Loan.  # noqa: E501

        Loan days  # noqa: E501

        :return: The days of this Loan.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this Loan.

        Loan days  # noqa: E501

        :param days: The days of this Loan.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and days is None:  # noqa: E501
            raise ValueError("Invalid value for `days`, must not be `None`")  # noqa: E501

        self._days = days

    @property
    def auto_renew(self):
        """Gets the auto_renew of this Loan.  # noqa: E501

        Auto renew the loan on expiration  # noqa: E501

        :return: The auto_renew of this Loan.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this Loan.

        Auto renew the loan on expiration  # noqa: E501

        :param auto_renew: The auto_renew of this Loan.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def currency_pair(self):
        """Gets the currency_pair of this Loan.  # noqa: E501

        Currency pair. Required for borrowing side  # noqa: E501

        :return: The currency_pair of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, currency_pair):
        """Sets the currency_pair of this Loan.

        Currency pair. Required for borrowing side  # noqa: E501

        :param currency_pair: The currency_pair of this Loan.  # noqa: E501
        :type: str
        """

        self._currency_pair = currency_pair

    @property
    def left(self):
        """Gets the left of this Loan.  # noqa: E501

        Amount not lending out  # noqa: E501

        :return: The left of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this Loan.

        Amount not lending out  # noqa: E501

        :param left: The left of this Loan.  # noqa: E501
        :type: str
        """

        self._left = left

    @property
    def repaid(self):
        """Gets the repaid of this Loan.  # noqa: E501

        Repaid amount  # noqa: E501

        :return: The repaid of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._repaid

    @repaid.setter
    def repaid(self, repaid):
        """Sets the repaid of this Loan.

        Repaid amount  # noqa: E501

        :param repaid: The repaid of this Loan.  # noqa: E501
        :type: str
        """

        self._repaid = repaid

    @property
    def paid_interest(self):
        """Gets the paid_interest of this Loan.  # noqa: E501

        Repaid interest  # noqa: E501

        :return: The paid_interest of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._paid_interest

    @paid_interest.setter
    def paid_interest(self, paid_interest):
        """Sets the paid_interest of this Loan.

        Repaid interest  # noqa: E501

        :param paid_interest: The paid_interest of this Loan.  # noqa: E501
        :type: str
        """

        self._paid_interest = paid_interest

    @property
    def unpaid_interest(self):
        """Gets the unpaid_interest of this Loan.  # noqa: E501

        Interest not repaid  # noqa: E501

        :return: The unpaid_interest of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._unpaid_interest

    @unpaid_interest.setter
    def unpaid_interest(self, unpaid_interest):
        """Sets the unpaid_interest of this Loan.

        Interest not repaid  # noqa: E501

        :param unpaid_interest: The unpaid_interest of this Loan.  # noqa: E501
        :type: str
        """

        self._unpaid_interest = unpaid_interest

    @property
    def fee_rate(self):
        """Gets the fee_rate of this Loan.  # noqa: E501

        Loan fee rate  # noqa: E501

        :return: The fee_rate of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._fee_rate

    @fee_rate.setter
    def fee_rate(self, fee_rate):
        """Sets the fee_rate of this Loan.

        Loan fee rate  # noqa: E501

        :param fee_rate: The fee_rate of this Loan.  # noqa: E501
        :type: str
        """

        self._fee_rate = fee_rate

    @property
    def orig_id(self):
        """Gets the orig_id of this Loan.  # noqa: E501

        Original loan ID if the loan is auto-renewed. Equal to `id` if not  # noqa: E501

        :return: The orig_id of this Loan.  # noqa: E501
        :rtype: str
        """
        return self._orig_id

    @orig_id.setter
    def orig_id(self, orig_id):
        """Sets the orig_id of this Loan.

        Original loan ID if the loan is auto-renewed. Equal to `id` if not  # noqa: E501

        :param orig_id: The orig_id of this Loan.  # noqa: E501
        :type: str
        """

        self._orig_id = orig_id

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
        if not isinstance(other, Loan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Loan):
            return True

        return self.to_dict() != other.to_dict()
