# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.22.6
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1beta1SELinuxStrategyOptions(object):
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
        'rule': 'str',
        'se_linux_options': 'V1SELinuxOptions'
    }

    attribute_map = {
        'rule': 'rule',
        'se_linux_options': 'seLinuxOptions'
    }

    def __init__(self, rule=None, se_linux_options=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1SELinuxStrategyOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._rule = None
        self._se_linux_options = None
        self.discriminator = None

        self.rule = rule
        if se_linux_options is not None:
            self.se_linux_options = se_linux_options

    @property
    def rule(self):
        """Gets the rule of this V1beta1SELinuxStrategyOptions.  # noqa: E501

        rule is the strategy that will dictate the allowable labels that may be set.  # noqa: E501

        :return: The rule of this V1beta1SELinuxStrategyOptions.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this V1beta1SELinuxStrategyOptions.

        rule is the strategy that will dictate the allowable labels that may be set.  # noqa: E501

        :param rule: The rule of this V1beta1SELinuxStrategyOptions.  # noqa: E501
        :type rule: str
        """
        if self.local_vars_configuration.client_side_validation and rule is None:  # noqa: E501
            raise ValueError("Invalid value for `rule`, must not be `None`")  # noqa: E501

        self._rule = rule

    @property
    def se_linux_options(self):
        """Gets the se_linux_options of this V1beta1SELinuxStrategyOptions.  # noqa: E501


        :return: The se_linux_options of this V1beta1SELinuxStrategyOptions.  # noqa: E501
        :rtype: V1SELinuxOptions
        """
        return self._se_linux_options

    @se_linux_options.setter
    def se_linux_options(self, se_linux_options):
        """Sets the se_linux_options of this V1beta1SELinuxStrategyOptions.


        :param se_linux_options: The se_linux_options of this V1beta1SELinuxStrategyOptions.  # noqa: E501
        :type se_linux_options: V1SELinuxOptions
        """

        self._se_linux_options = se_linux_options

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1SELinuxStrategyOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1SELinuxStrategyOptions):
            return True

        return self.to_dict() != other.to_dict()
