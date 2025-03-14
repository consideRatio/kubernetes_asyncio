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


class V1TopologySpreadConstraint(object):
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
        'label_selector': 'V1LabelSelector',
        'max_skew': 'int',
        'topology_key': 'str',
        'when_unsatisfiable': 'str'
    }

    attribute_map = {
        'label_selector': 'labelSelector',
        'max_skew': 'maxSkew',
        'topology_key': 'topologyKey',
        'when_unsatisfiable': 'whenUnsatisfiable'
    }

    def __init__(self, label_selector=None, max_skew=None, topology_key=None, when_unsatisfiable=None, local_vars_configuration=None):  # noqa: E501
        """V1TopologySpreadConstraint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._label_selector = None
        self._max_skew = None
        self._topology_key = None
        self._when_unsatisfiable = None
        self.discriminator = None

        if label_selector is not None:
            self.label_selector = label_selector
        self.max_skew = max_skew
        self.topology_key = topology_key
        self.when_unsatisfiable = when_unsatisfiable

    @property
    def label_selector(self):
        """Gets the label_selector of this V1TopologySpreadConstraint.  # noqa: E501


        :return: The label_selector of this V1TopologySpreadConstraint.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._label_selector

    @label_selector.setter
    def label_selector(self, label_selector):
        """Sets the label_selector of this V1TopologySpreadConstraint.


        :param label_selector: The label_selector of this V1TopologySpreadConstraint.  # noqa: E501
        :type label_selector: V1LabelSelector
        """

        self._label_selector = label_selector

    @property
    def max_skew(self):
        """Gets the max_skew of this V1TopologySpreadConstraint.  # noqa: E501

        MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 1/1/0: | zone1 | zone2 | zone3 | |   P   |   P   |       | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 1/1/1; scheduling it onto zone1(zone2) would make the ActualSkew(2-0) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It's a required field. Default value is 1 and 0 is not allowed.  # noqa: E501

        :return: The max_skew of this V1TopologySpreadConstraint.  # noqa: E501
        :rtype: int
        """
        return self._max_skew

    @max_skew.setter
    def max_skew(self, max_skew):
        """Sets the max_skew of this V1TopologySpreadConstraint.

        MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 1/1/0: | zone1 | zone2 | zone3 | |   P   |   P   |       | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 1/1/1; scheduling it onto zone1(zone2) would make the ActualSkew(2-0) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It's a required field. Default value is 1 and 0 is not allowed.  # noqa: E501

        :param max_skew: The max_skew of this V1TopologySpreadConstraint.  # noqa: E501
        :type max_skew: int
        """
        if self.local_vars_configuration.client_side_validation and max_skew is None:  # noqa: E501
            raise ValueError("Invalid value for `max_skew`, must not be `None`")  # noqa: E501

        self._max_skew = max_skew

    @property
    def topology_key(self):
        """Gets the topology_key of this V1TopologySpreadConstraint.  # noqa: E501

        TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a \"bucket\", and try to put balanced number of pods into each bucket. It's a required field.  # noqa: E501

        :return: The topology_key of this V1TopologySpreadConstraint.  # noqa: E501
        :rtype: str
        """
        return self._topology_key

    @topology_key.setter
    def topology_key(self, topology_key):
        """Sets the topology_key of this V1TopologySpreadConstraint.

        TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a \"bucket\", and try to put balanced number of pods into each bucket. It's a required field.  # noqa: E501

        :param topology_key: The topology_key of this V1TopologySpreadConstraint.  # noqa: E501
        :type topology_key: str
        """
        if self.local_vars_configuration.client_side_validation and topology_key is None:  # noqa: E501
            raise ValueError("Invalid value for `topology_key`, must not be `None`")  # noqa: E501

        self._topology_key = topology_key

    @property
    def when_unsatisfiable(self):
        """Gets the when_unsatisfiable of this V1TopologySpreadConstraint.  # noqa: E501

        WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location,   but giving higher precedence to topologies that would help reduce the   skew. A constraint is considered \"Unsatisfiable\" for an incoming pod if and only if every possible node assigment for that pod would violate \"MaxSkew\" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.  # noqa: E501

        :return: The when_unsatisfiable of this V1TopologySpreadConstraint.  # noqa: E501
        :rtype: str
        """
        return self._when_unsatisfiable

    @when_unsatisfiable.setter
    def when_unsatisfiable(self, when_unsatisfiable):
        """Sets the when_unsatisfiable of this V1TopologySpreadConstraint.

        WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location,   but giving higher precedence to topologies that would help reduce the   skew. A constraint is considered \"Unsatisfiable\" for an incoming pod if and only if every possible node assigment for that pod would violate \"MaxSkew\" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.  # noqa: E501

        :param when_unsatisfiable: The when_unsatisfiable of this V1TopologySpreadConstraint.  # noqa: E501
        :type when_unsatisfiable: str
        """
        if self.local_vars_configuration.client_side_validation and when_unsatisfiable is None:  # noqa: E501
            raise ValueError("Invalid value for `when_unsatisfiable`, must not be `None`")  # noqa: E501

        self._when_unsatisfiable = when_unsatisfiable

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
        if not isinstance(other, V1TopologySpreadConstraint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1TopologySpreadConstraint):
            return True

        return self.to_dict() != other.to_dict()
