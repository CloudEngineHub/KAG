# coding: utf-8
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

"""
    knext

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from knext.common.rest.configuration import Configuration


class StreamData(object):
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
        "answer": "str",
        "reference": "list[RefDocSet]",
        "think": "str",
        "metrics": "Metrics",
        "subgraph": "list[SubGraph]",
    }

    attribute_map = {
        "answer": "answer",
        "reference": "reference",
        "think": "think",
        "metrics": "metrics",
        "subgraph": "subgraph",
    }

    def __init__(
        self,
        answer=None,
        reference=None,
        think=None,
        metrics=None,
        subgraph=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """StreamData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._answer = None
        self._reference = None
        self._think = None
        self._metrics = None
        self._subgraph = None
        self.discriminator = None

        self.answer = answer
        self.reference = reference
        self.think = think
        self.metrics = metrics
        self.subgraph = subgraph

    @property
    def answer(self):
        """Gets the answer of this StreamData.  # noqa: E501


        :return: The answer of this StreamData.  # noqa: E501
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this StreamData.


        :param answer: The answer of this StreamData.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and answer is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `answer`, must not be `None`"
            )  # noqa: E501

        self._answer = answer

    @property
    def reference(self):
        """Gets the reference of this StreamData.  # noqa: E501


        :return: The reference of this StreamData.  # noqa: E501
        :rtype: list[RefDocSet]
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this StreamData.


        :param reference: The reference of this StreamData.  # noqa: E501
        :type: list[RefDocSet]
        """
        if (
            self.local_vars_configuration.client_side_validation and reference is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `reference`, must not be `None`"
            )  # noqa: E501

        self._reference = reference

    @property
    def think(self):
        """Gets the think of this StreamData.  # noqa: E501


        :return: The think of this StreamData.  # noqa: E501
        :rtype: str
        """
        return self._think

    @think.setter
    def think(self, think):
        """Sets the think of this StreamData.


        :param think: The think of this StreamData.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and think is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `think`, must not be `None`"
            )  # noqa: E501

        self._think = think

    @property
    def metrics(self):
        """Gets the metrics of this StreamData.  # noqa: E501


        :return: The metrics of this StreamData.  # noqa: E501
        :rtype: Metrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this StreamData.


        :param metrics: The metrics of this StreamData.  # noqa: E501
        :type: Metrics
        """
        if (
            self.local_vars_configuration.client_side_validation and metrics is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `metrics`, must not be `None`"
            )  # noqa: E501

        self._metrics = metrics

    @property
    def subgraph(self):
        """Gets the subgraph of this StreamData.  # noqa: E501


        :return: The subgraph of this StreamData.  # noqa: E501
        :rtype: list[SubGraph]
        """
        return self._subgraph

    @subgraph.setter
    def subgraph(self, subgraph):
        """Sets the subgraph of this StreamData.


        :param subgraph: The subgraph of this StreamData.  # noqa: E501
        :type: list[SubGraph]
        """
        if (
            self.local_vars_configuration.client_side_validation and subgraph is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `subgraph`, must not be `None`"
            )  # noqa: E501

        self._subgraph = subgraph

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
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
        if not isinstance(other, StreamData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StreamData):
            return True

        return self.to_dict() != other.to_dict()
