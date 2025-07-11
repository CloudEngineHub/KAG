# coding: utf-8

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


class SubGraph(object):
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
        "class_name": "str",
        "result_nodes": "list[DataNode]",
        "result_edges": "list[DataEdge]",
    }

    attribute_map = {
        "class_name": "className",
        "result_nodes": "resultNodes",
        "result_edges": "resultEdges",
    }

    def __init__(
        self,
        class_name=None,
        result_nodes=None,
        result_edges=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """SubGraph - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._class_name = None
        self._result_nodes = None
        self._result_edges = None
        self.discriminator = None

        self.class_name = class_name
        self.result_nodes = result_nodes
        self.result_edges = result_edges

    @property
    def class_name(self):
        """Gets the class_name of this SubGraph.  # noqa: E501


        :return: The class_name of this SubGraph.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this SubGraph.


        :param class_name: The class_name of this SubGraph.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and class_name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `class_name`, must not be `None`"
            )  # noqa: E501

        self._class_name = class_name

    @property
    def result_nodes(self):
        """Gets the result_nodes of this SubGraph.  # noqa: E501


        :return: The result_nodes of this SubGraph.  # noqa: E501
        :rtype: list[DataNode]
        """
        return self._result_nodes

    @result_nodes.setter
    def result_nodes(self, result_nodes):
        """Sets the result_nodes of this SubGraph.


        :param result_nodes: The result_nodes of this SubGraph.  # noqa: E501
        :type: list[DataNode]
        """
        if (
            self.local_vars_configuration.client_side_validation
            and result_nodes is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `result_nodes`, must not be `None`"
            )  # noqa: E501

        self._result_nodes = result_nodes

    @property
    def result_edges(self):
        """Gets the result_edges of this SubGraph.  # noqa: E501


        :return: The result_edges of this SubGraph.  # noqa: E501
        :rtype: list[DataEdge]
        """
        return self._result_edges

    @result_edges.setter
    def result_edges(self, result_edges):
        """Sets the result_edges of this SubGraph.


        :param result_edges: The result_edges of this SubGraph.  # noqa: E501
        :type: list[DataEdge]
        """
        if (
            self.local_vars_configuration.client_side_validation
            and result_edges is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `result_edges`, must not be `None`"
            )  # noqa: E501

        self._result_edges = result_edges

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
        if not isinstance(other, SubGraph):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubGraph):
            return True

        return self.to_dict() != other.to_dict()
