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


class V1PersistentVolumeClaimStatus(object):
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
        'access_modes': 'list[str]',
        'capacity': 'dict(str, str)',
        'conditions': 'list[V1PersistentVolumeClaimCondition]',
        'phase': 'str'
    }

    attribute_map = {
        'access_modes': 'accessModes',
        'capacity': 'capacity',
        'conditions': 'conditions',
        'phase': 'phase'
    }

    def __init__(self, access_modes=None, capacity=None, conditions=None, phase=None, local_vars_configuration=None):  # noqa: E501
        """V1PersistentVolumeClaimStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._access_modes = None
        self._capacity = None
        self._conditions = None
        self._phase = None
        self.discriminator = None

        if access_modes is not None:
            self.access_modes = access_modes
        if capacity is not None:
            self.capacity = capacity
        if conditions is not None:
            self.conditions = conditions
        if phase is not None:
            self.phase = phase

    @property
    def access_modes(self):
        """Gets the access_modes of this V1PersistentVolumeClaimStatus.  # noqa: E501

        AccessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1  # noqa: E501

        :return: The access_modes of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """Sets the access_modes of this V1PersistentVolumeClaimStatus.

        AccessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1  # noqa: E501

        :param access_modes: The access_modes of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type access_modes: list[str]
        """

        self._access_modes = access_modes

    @property
    def capacity(self):
        """Gets the capacity of this V1PersistentVolumeClaimStatus.  # noqa: E501

        Represents the actual resources of the underlying volume.  # noqa: E501

        :return: The capacity of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this V1PersistentVolumeClaimStatus.

        Represents the actual resources of the underlying volume.  # noqa: E501

        :param capacity: The capacity of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type capacity: dict(str, str)
        """

        self._capacity = capacity

    @property
    def conditions(self):
        """Gets the conditions of this V1PersistentVolumeClaimStatus.  # noqa: E501

        Current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'.  # noqa: E501

        :return: The conditions of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: list[V1PersistentVolumeClaimCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1PersistentVolumeClaimStatus.

        Current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'.  # noqa: E501

        :param conditions: The conditions of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type conditions: list[V1PersistentVolumeClaimCondition]
        """

        self._conditions = conditions

    @property
    def phase(self):
        """Gets the phase of this V1PersistentVolumeClaimStatus.  # noqa: E501

        Phase represents the current phase of PersistentVolumeClaim.  # noqa: E501

        :return: The phase of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this V1PersistentVolumeClaimStatus.

        Phase represents the current phase of PersistentVolumeClaim.  # noqa: E501

        :param phase: The phase of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type phase: str
        """

        self._phase = phase

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
        if not isinstance(other, V1PersistentVolumeClaimStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PersistentVolumeClaimStatus):
            return True

        return self.to_dict() != other.to_dict()
