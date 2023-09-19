# coding: utf-8

"""
    Sidra API

    Sidra API  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: info@sidra.dev
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DataQualityApiControllersMetadataModelsEntityDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'item_id': 'str',
        'name': 'str',
        'suite_name': 'str',
        'assets': 'list[DataQualityApiControllersMetadataModelsAssetDto]'
    }

    attribute_map = {
        'id': 'id',
        'item_id': 'itemId',
        'name': 'name',
        'suite_name': 'suiteName',
        'assets': 'assets'
    }

    def __init__(self, id=None, item_id=None, name=None, suite_name=None, assets=None):  # noqa: E501
        """DataQualityApiControllersMetadataModelsEntityDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._item_id = None
        self._name = None
        self._suite_name = None
        self._assets = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if item_id is not None:
            self.item_id = item_id
        if name is not None:
            self.name = name
        if suite_name is not None:
            self.suite_name = suite_name
        if assets is not None:
            self.assets = assets

    @property
    def id(self):
        """Gets the id of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501


        :return: The id of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataQualityApiControllersMetadataModelsEntityDto.


        :param id: The id of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def item_id(self):
        """Gets the item_id of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501


        :return: The item_id of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this DataQualityApiControllersMetadataModelsEntityDto.


        :param item_id: The item_id of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def name(self):
        """Gets the name of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501


        :return: The name of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataQualityApiControllersMetadataModelsEntityDto.


        :param name: The name of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def suite_name(self):
        """Gets the suite_name of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501


        :return: The suite_name of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501
        :rtype: str
        """
        return self._suite_name

    @suite_name.setter
    def suite_name(self, suite_name):
        """Sets the suite_name of this DataQualityApiControllersMetadataModelsEntityDto.


        :param suite_name: The suite_name of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501
        :type: str
        """

        self._suite_name = suite_name

    @property
    def assets(self):
        """Gets the assets of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501


        :return: The assets of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501
        :rtype: list[DataQualityApiControllersMetadataModelsAssetDto]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this DataQualityApiControllersMetadataModelsEntityDto.


        :param assets: The assets of this DataQualityApiControllersMetadataModelsEntityDto.  # noqa: E501
        :type: list[DataQualityApiControllersMetadataModelsAssetDto]
        """

        self._assets = assets

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DataQualityApiControllersMetadataModelsEntityDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DataQualityApiControllersMetadataModelsEntityDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
