"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.562.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from plaid.exceptions import ApiAttributeError


def lazy_import():
    from plaid.model.asset_type import AssetType
    globals()['AssetType'] = AssetType


class AssetDetail(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'asset_unique_identifier': (str,),  # noqa: E501
            'asset_account_identifier': (str,),  # noqa: E501
            'asset_as_of_date': (str,),  # noqa: E501
            'asset_description': (str, none_type,),  # noqa: E501
            'asset_available_balance_amount': (float,),  # noqa: E501
            'asset_current_balance_amount': (float,),  # noqa: E501
            'asset_type': (AssetType,),  # noqa: E501
            'asset_type_additional_description': (str, none_type,),  # noqa: E501
            'asset_days_requested_count': (int,),  # noqa: E501
            'asset_ownership_type': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'asset_unique_identifier': 'AssetUniqueIdentifier',  # noqa: E501
        'asset_account_identifier': 'AssetAccountIdentifier',  # noqa: E501
        'asset_as_of_date': 'AssetAsOfDate',  # noqa: E501
        'asset_description': 'AssetDescription',  # noqa: E501
        'asset_available_balance_amount': 'AssetAvailableBalanceAmount',  # noqa: E501
        'asset_current_balance_amount': 'AssetCurrentBalanceAmount',  # noqa: E501
        'asset_type': 'AssetType',  # noqa: E501
        'asset_type_additional_description': 'AssetTypeAdditionalDescription',  # noqa: E501
        'asset_days_requested_count': 'AssetDaysRequestedCount',  # noqa: E501
        'asset_ownership_type': 'AssetOwnershipType',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, asset_unique_identifier, asset_account_identifier, asset_as_of_date, asset_description, asset_available_balance_amount, asset_current_balance_amount, asset_type, asset_type_additional_description, asset_days_requested_count, asset_ownership_type, *args, **kwargs):  # noqa: E501
        """AssetDetail - a model defined in OpenAPI

        Args:
            asset_unique_identifier (str): A vendor created unique Identifier.
            asset_account_identifier (str): A unique alphanumeric string identifying an asset.
            asset_as_of_date (str): Account Report As of Date / Create Date. Format YYYY-MM-DD
            asset_description (str, none_type): A text description that further defines the Asset. This could be used to describe the shares associated with the stocks, bonds or mutual funds, retirement funds or business owned that the borrower has disclosed (named) as an asset.
            asset_available_balance_amount (float): Asset Account Available Balance.
            asset_current_balance_amount (float): A vendor created unique Identifier
            asset_type (AssetType):
            asset_type_additional_description (str, none_type): Additional Asset Decription some examples are Investment Tax-Deferred , Loan, 401K, 403B, Checking, Money Market, Credit Card,ROTH,529,Biller,ROLLOVER,CD,Savings,Investment Taxable, IRA, Mortgage, Line Of Credit.
            asset_days_requested_count (int): The Number of days requested made to the Financial Institution. Example When looking for 3 months of data from the FI, pass in 90 days.
            asset_ownership_type (str, none_type): Ownership type of the asset account.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.asset_unique_identifier = asset_unique_identifier
        self.asset_account_identifier = asset_account_identifier
        self.asset_as_of_date = asset_as_of_date
        self.asset_description = asset_description
        self.asset_available_balance_amount = asset_available_balance_amount
        self.asset_current_balance_amount = asset_current_balance_amount
        self.asset_type = asset_type
        self.asset_type_additional_description = asset_type_additional_description
        self.asset_days_requested_count = asset_days_requested_count
        self.asset_ownership_type = asset_ownership_type
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, asset_unique_identifier, asset_account_identifier, asset_as_of_date, asset_description, asset_available_balance_amount, asset_current_balance_amount, asset_type, asset_type_additional_description, asset_days_requested_count, asset_ownership_type, *args, **kwargs):  # noqa: E501
        """AssetDetail - a model defined in OpenAPI

        Args:
            asset_unique_identifier (str): A vendor created unique Identifier.
            asset_account_identifier (str): A unique alphanumeric string identifying an asset.
            asset_as_of_date (str): Account Report As of Date / Create Date. Format YYYY-MM-DD
            asset_description (str, none_type): A text description that further defines the Asset. This could be used to describe the shares associated with the stocks, bonds or mutual funds, retirement funds or business owned that the borrower has disclosed (named) as an asset.
            asset_available_balance_amount (float): Asset Account Available Balance.
            asset_current_balance_amount (float): A vendor created unique Identifier
            asset_type (AssetType):
            asset_type_additional_description (str, none_type): Additional Asset Decription some examples are Investment Tax-Deferred , Loan, 401K, 403B, Checking, Money Market, Credit Card,ROTH,529,Biller,ROLLOVER,CD,Savings,Investment Taxable, IRA, Mortgage, Line Of Credit.
            asset_days_requested_count (int): The Number of days requested made to the Financial Institution. Example When looking for 3 months of data from the FI, pass in 90 days.
            asset_ownership_type (str, none_type): Ownership type of the asset account.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.asset_unique_identifier = asset_unique_identifier
        self.asset_account_identifier = asset_account_identifier
        self.asset_as_of_date = asset_as_of_date
        self.asset_description = asset_description
        self.asset_available_balance_amount = asset_available_balance_amount
        self.asset_current_balance_amount = asset_current_balance_amount
        self.asset_type = asset_type
        self.asset_type_additional_description = asset_type_additional_description
        self.asset_days_requested_count = asset_days_requested_count
        self.asset_ownership_type = asset_ownership_type
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
