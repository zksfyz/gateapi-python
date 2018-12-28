# coding: utf-8

# flake8: noqa
"""
    Gate API v4

    APIv4 futures provides all sorts of futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from gate_client.models.contract import Contract
from gate_client.models.funding_rate_record import FundingRateRecord
from gate_client.models.futures_account import FuturesAccount
from gate_client.models.futures_candlestick import FuturesCandlestick
from gate_client.models.futures_error_response import FuturesErrorResponse
from gate_client.models.futures_order import FuturesOrder
from gate_client.models.futures_order_book import FuturesOrderBook
from gate_client.models.futures_order_book_item import FuturesOrderBookItem
from gate_client.models.futures_ticker import FuturesTicker
from gate_client.models.futures_trade import FuturesTrade
from gate_client.models.insurance_record import InsuranceRecord
from gate_client.models.my_futures_trade import MyFuturesTrade
from gate_client.models.position import Position
