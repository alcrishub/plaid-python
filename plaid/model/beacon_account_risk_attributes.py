"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.555.0
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



class BeaconAccountRiskAttributes(ModelNormal):
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
        return {
            'days_since_first_plaid_connection': (int, none_type,),  # noqa: E501
            'is_account_closed': (bool, none_type,),  # noqa: E501
            'is_account_frozen_or_restricted': (bool, none_type,),  # noqa: E501
            'total_plaid_connections_count': (int, none_type,),  # noqa: E501
            'plaid_connections_count_7d': (int, none_type,),  # noqa: E501
            'plaid_connections_count_30d': (int, none_type,),  # noqa: E501
            'failed_plaid_non_oauth_authentication_attempts_count_3d': (int, none_type,),  # noqa: E501
            'plaid_non_oauth_authentication_attempts_count_3d': (int, none_type,),  # noqa: E501
            'failed_plaid_non_oauth_authentication_attempts_count_7d': (int, none_type,),  # noqa: E501
            'plaid_non_oauth_authentication_attempts_count_7d': (int, none_type,),  # noqa: E501
            'failed_plaid_non_oauth_authentication_attempts_count_30d': (int, none_type,),  # noqa: E501
            'plaid_non_oauth_authentication_attempts_count_30d': (int, none_type,),  # noqa: E501
            'distinct_ip_addresses_count_3d': (int, none_type,),  # noqa: E501
            'distinct_ip_addresses_count_7d': (int, none_type,),  # noqa: E501
            'distinct_ip_addresses_count_30d': (int, none_type,),  # noqa: E501
            'distinct_ip_addresses_count_90d': (int, none_type,),  # noqa: E501
            'distinct_user_agents_count_3d': (int, none_type,),  # noqa: E501
            'distinct_user_agents_count_7d': (int, none_type,),  # noqa: E501
            'distinct_user_agents_count_30d': (int, none_type,),  # noqa: E501
            'distinct_user_agents_count_90d': (int, none_type,),  # noqa: E501
            'address_change_count_28d': (int, none_type,),  # noqa: E501
            'email_change_count_28d': (int, none_type,),  # noqa: E501
            'phone_change_count_28d': (int, none_type,),  # noqa: E501
            'address_change_count_90d': (int, none_type,),  # noqa: E501
            'email_change_count_90d': (int, none_type,),  # noqa: E501
            'phone_change_count_90d': (int, none_type,),  # noqa: E501
            'days_since_account_opening': (int, none_type,),  # noqa: E501
            'days_since_first_observed_transaction': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'days_since_first_plaid_connection': 'days_since_first_plaid_connection',  # noqa: E501
        'is_account_closed': 'is_account_closed',  # noqa: E501
        'is_account_frozen_or_restricted': 'is_account_frozen_or_restricted',  # noqa: E501
        'total_plaid_connections_count': 'total_plaid_connections_count',  # noqa: E501
        'plaid_connections_count_7d': 'plaid_connections_count_7d',  # noqa: E501
        'plaid_connections_count_30d': 'plaid_connections_count_30d',  # noqa: E501
        'failed_plaid_non_oauth_authentication_attempts_count_3d': 'failed_plaid_non_oauth_authentication_attempts_count_3d',  # noqa: E501
        'plaid_non_oauth_authentication_attempts_count_3d': 'plaid_non_oauth_authentication_attempts_count_3d',  # noqa: E501
        'failed_plaid_non_oauth_authentication_attempts_count_7d': 'failed_plaid_non_oauth_authentication_attempts_count_7d',  # noqa: E501
        'plaid_non_oauth_authentication_attempts_count_7d': 'plaid_non_oauth_authentication_attempts_count_7d',  # noqa: E501
        'failed_plaid_non_oauth_authentication_attempts_count_30d': 'failed_plaid_non_oauth_authentication_attempts_count_30d',  # noqa: E501
        'plaid_non_oauth_authentication_attempts_count_30d': 'plaid_non_oauth_authentication_attempts_count_30d',  # noqa: E501
        'distinct_ip_addresses_count_3d': 'distinct_ip_addresses_count_3d',  # noqa: E501
        'distinct_ip_addresses_count_7d': 'distinct_ip_addresses_count_7d',  # noqa: E501
        'distinct_ip_addresses_count_30d': 'distinct_ip_addresses_count_30d',  # noqa: E501
        'distinct_ip_addresses_count_90d': 'distinct_ip_addresses_count_90d',  # noqa: E501
        'distinct_user_agents_count_3d': 'distinct_user_agents_count_3d',  # noqa: E501
        'distinct_user_agents_count_7d': 'distinct_user_agents_count_7d',  # noqa: E501
        'distinct_user_agents_count_30d': 'distinct_user_agents_count_30d',  # noqa: E501
        'distinct_user_agents_count_90d': 'distinct_user_agents_count_90d',  # noqa: E501
        'address_change_count_28d': 'address_change_count_28d',  # noqa: E501
        'email_change_count_28d': 'email_change_count_28d',  # noqa: E501
        'phone_change_count_28d': 'phone_change_count_28d',  # noqa: E501
        'address_change_count_90d': 'address_change_count_90d',  # noqa: E501
        'email_change_count_90d': 'email_change_count_90d',  # noqa: E501
        'phone_change_count_90d': 'phone_change_count_90d',  # noqa: E501
        'days_since_account_opening': 'days_since_account_opening',  # noqa: E501
        'days_since_first_observed_transaction': 'days_since_first_observed_transaction',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, days_since_first_plaid_connection, is_account_closed, is_account_frozen_or_restricted, total_plaid_connections_count, plaid_connections_count_7d, plaid_connections_count_30d, failed_plaid_non_oauth_authentication_attempts_count_3d, plaid_non_oauth_authentication_attempts_count_3d, failed_plaid_non_oauth_authentication_attempts_count_7d, plaid_non_oauth_authentication_attempts_count_7d, failed_plaid_non_oauth_authentication_attempts_count_30d, plaid_non_oauth_authentication_attempts_count_30d, distinct_ip_addresses_count_3d, distinct_ip_addresses_count_7d, distinct_ip_addresses_count_30d, distinct_ip_addresses_count_90d, distinct_user_agents_count_3d, distinct_user_agents_count_7d, distinct_user_agents_count_30d, distinct_user_agents_count_90d, address_change_count_28d, email_change_count_28d, phone_change_count_28d, address_change_count_90d, email_change_count_90d, phone_change_count_90d, days_since_account_opening, days_since_first_observed_transaction, *args, **kwargs):  # noqa: E501
        """BeaconAccountRiskAttributes - a model defined in OpenAPI

        Args:
            days_since_first_plaid_connection (int, none_type): The number of days since the first time the Item was connected to an application via Plaid
            is_account_closed (bool, none_type): Indicates if the account has been closed by the financial institution or the consumer, or is at risk of being closed
            is_account_frozen_or_restricted (bool, none_type): Indicates whether the account has withdrawals and transfers disabled or if access to the account is restricted. This could be due to a freeze by the credit issuer, legal restrictions (e.g., sanctions), or regulatory requirements limiting monthly withdrawals, among other reasons
            total_plaid_connections_count (int, none_type): The total number of times the item has been connected to applications via Plaid
            plaid_connections_count_7d (int, none_type): The number of times the Item has been connected to applications via Plaid over the past 7 days
            plaid_connections_count_30d (int, none_type): The number of times the Item has been connected to applications via Plaid over the past 30 days
            failed_plaid_non_oauth_authentication_attempts_count_3d (int, none_type): The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 3 days
            plaid_non_oauth_authentication_attempts_count_3d (int, none_type): The number of non-OAuth authentication attempts via Plaid for this bank account over the past 3 days
            failed_plaid_non_oauth_authentication_attempts_count_7d (int, none_type): The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 7 days
            plaid_non_oauth_authentication_attempts_count_7d (int, none_type): The number of non-OAuth authentication attempts via Plaid for this bank account over the past 7 days
            failed_plaid_non_oauth_authentication_attempts_count_30d (int, none_type): The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 30 days
            plaid_non_oauth_authentication_attempts_count_30d (int, none_type): The number of non-OAuth authentication attempts via Plaid for this bank account over the past 30 days
            distinct_ip_addresses_count_3d (int, none_type): The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 3 days
            distinct_ip_addresses_count_7d (int, none_type): The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 7 days
            distinct_ip_addresses_count_30d (int, none_type): The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 30 days
            distinct_ip_addresses_count_90d (int, none_type): The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 90 days
            distinct_user_agents_count_3d (int, none_type): The number of distinct user agents linked to the same bank account during Plaid authentication in the last 3 days
            distinct_user_agents_count_7d (int, none_type): The number of distinct user agents linked to the same bank account during Plaid authentication in the last 7 days
            distinct_user_agents_count_30d (int, none_type): The number of distinct user agents linked to the same bank account during Plaid authentication in the last 30 days
            distinct_user_agents_count_90d (int, none_type): The number of distinct user agents linked to the same bank account during Plaid authentication in the last 90 days
            address_change_count_28d (int, none_type): The number of times the account's addresses on file have changed over the past 28 days
            email_change_count_28d (int, none_type): The number of times the account's email addresses on file have changed over the past 28 days
            phone_change_count_28d (int, none_type): The number of times the account's phone numbers on file have changed over the past 28 days
            address_change_count_90d (int, none_type): The number of times the account's addresses on file have changed over the past 90 days
            email_change_count_90d (int, none_type): The number of times the account's email addresses on file have changed over the past 90 days
            phone_change_count_90d (int, none_type): The number of times the account's phone numbers on file have changed over the past 90 days
            days_since_account_opening (int, none_type): The number of days since the bank account was opened, as reported by the financial institution
            days_since_first_observed_transaction (int, none_type): The number of days since the oldest transaction available to Plaid for this account. This measure, combined with Plaid connection history, can be used to infer the age of the account

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

        self.days_since_first_plaid_connection = days_since_first_plaid_connection
        self.is_account_closed = is_account_closed
        self.is_account_frozen_or_restricted = is_account_frozen_or_restricted
        self.total_plaid_connections_count = total_plaid_connections_count
        self.plaid_connections_count_7d = plaid_connections_count_7d
        self.plaid_connections_count_30d = plaid_connections_count_30d
        self.failed_plaid_non_oauth_authentication_attempts_count_3d = failed_plaid_non_oauth_authentication_attempts_count_3d
        self.plaid_non_oauth_authentication_attempts_count_3d = plaid_non_oauth_authentication_attempts_count_3d
        self.failed_plaid_non_oauth_authentication_attempts_count_7d = failed_plaid_non_oauth_authentication_attempts_count_7d
        self.plaid_non_oauth_authentication_attempts_count_7d = plaid_non_oauth_authentication_attempts_count_7d
        self.failed_plaid_non_oauth_authentication_attempts_count_30d = failed_plaid_non_oauth_authentication_attempts_count_30d
        self.plaid_non_oauth_authentication_attempts_count_30d = plaid_non_oauth_authentication_attempts_count_30d
        self.distinct_ip_addresses_count_3d = distinct_ip_addresses_count_3d
        self.distinct_ip_addresses_count_7d = distinct_ip_addresses_count_7d
        self.distinct_ip_addresses_count_30d = distinct_ip_addresses_count_30d
        self.distinct_ip_addresses_count_90d = distinct_ip_addresses_count_90d
        self.distinct_user_agents_count_3d = distinct_user_agents_count_3d
        self.distinct_user_agents_count_7d = distinct_user_agents_count_7d
        self.distinct_user_agents_count_30d = distinct_user_agents_count_30d
        self.distinct_user_agents_count_90d = distinct_user_agents_count_90d
        self.address_change_count_28d = address_change_count_28d
        self.email_change_count_28d = email_change_count_28d
        self.phone_change_count_28d = phone_change_count_28d
        self.address_change_count_90d = address_change_count_90d
        self.email_change_count_90d = email_change_count_90d
        self.phone_change_count_90d = phone_change_count_90d
        self.days_since_account_opening = days_since_account_opening
        self.days_since_first_observed_transaction = days_since_first_observed_transaction
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
    def __init__(self, days_since_first_plaid_connection, is_account_closed, is_account_frozen_or_restricted, total_plaid_connections_count, plaid_connections_count_7d, plaid_connections_count_30d, failed_plaid_non_oauth_authentication_attempts_count_3d, plaid_non_oauth_authentication_attempts_count_3d, failed_plaid_non_oauth_authentication_attempts_count_7d, plaid_non_oauth_authentication_attempts_count_7d, failed_plaid_non_oauth_authentication_attempts_count_30d, plaid_non_oauth_authentication_attempts_count_30d, distinct_ip_addresses_count_3d, distinct_ip_addresses_count_7d, distinct_ip_addresses_count_30d, distinct_ip_addresses_count_90d, distinct_user_agents_count_3d, distinct_user_agents_count_7d, distinct_user_agents_count_30d, distinct_user_agents_count_90d, address_change_count_28d, email_change_count_28d, phone_change_count_28d, address_change_count_90d, email_change_count_90d, phone_change_count_90d, days_since_account_opening, days_since_first_observed_transaction, *args, **kwargs):  # noqa: E501
        """BeaconAccountRiskAttributes - a model defined in OpenAPI

        Args:
            days_since_first_plaid_connection (int, none_type): The number of days since the first time the Item was connected to an application via Plaid
            is_account_closed (bool, none_type): Indicates if the account has been closed by the financial institution or the consumer, or is at risk of being closed
            is_account_frozen_or_restricted (bool, none_type): Indicates whether the account has withdrawals and transfers disabled or if access to the account is restricted. This could be due to a freeze by the credit issuer, legal restrictions (e.g., sanctions), or regulatory requirements limiting monthly withdrawals, among other reasons
            total_plaid_connections_count (int, none_type): The total number of times the item has been connected to applications via Plaid
            plaid_connections_count_7d (int, none_type): The number of times the Item has been connected to applications via Plaid over the past 7 days
            plaid_connections_count_30d (int, none_type): The number of times the Item has been connected to applications via Plaid over the past 30 days
            failed_plaid_non_oauth_authentication_attempts_count_3d (int, none_type): The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 3 days
            plaid_non_oauth_authentication_attempts_count_3d (int, none_type): The number of non-OAuth authentication attempts via Plaid for this bank account over the past 3 days
            failed_plaid_non_oauth_authentication_attempts_count_7d (int, none_type): The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 7 days
            plaid_non_oauth_authentication_attempts_count_7d (int, none_type): The number of non-OAuth authentication attempts via Plaid for this bank account over the past 7 days
            failed_plaid_non_oauth_authentication_attempts_count_30d (int, none_type): The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 30 days
            plaid_non_oauth_authentication_attempts_count_30d (int, none_type): The number of non-OAuth authentication attempts via Plaid for this bank account over the past 30 days
            distinct_ip_addresses_count_3d (int, none_type): The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 3 days
            distinct_ip_addresses_count_7d (int, none_type): The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 7 days
            distinct_ip_addresses_count_30d (int, none_type): The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 30 days
            distinct_ip_addresses_count_90d (int, none_type): The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 90 days
            distinct_user_agents_count_3d (int, none_type): The number of distinct user agents linked to the same bank account during Plaid authentication in the last 3 days
            distinct_user_agents_count_7d (int, none_type): The number of distinct user agents linked to the same bank account during Plaid authentication in the last 7 days
            distinct_user_agents_count_30d (int, none_type): The number of distinct user agents linked to the same bank account during Plaid authentication in the last 30 days
            distinct_user_agents_count_90d (int, none_type): The number of distinct user agents linked to the same bank account during Plaid authentication in the last 90 days
            address_change_count_28d (int, none_type): The number of times the account's addresses on file have changed over the past 28 days
            email_change_count_28d (int, none_type): The number of times the account's email addresses on file have changed over the past 28 days
            phone_change_count_28d (int, none_type): The number of times the account's phone numbers on file have changed over the past 28 days
            address_change_count_90d (int, none_type): The number of times the account's addresses on file have changed over the past 90 days
            email_change_count_90d (int, none_type): The number of times the account's email addresses on file have changed over the past 90 days
            phone_change_count_90d (int, none_type): The number of times the account's phone numbers on file have changed over the past 90 days
            days_since_account_opening (int, none_type): The number of days since the bank account was opened, as reported by the financial institution
            days_since_first_observed_transaction (int, none_type): The number of days since the oldest transaction available to Plaid for this account. This measure, combined with Plaid connection history, can be used to infer the age of the account

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

        self.days_since_first_plaid_connection = days_since_first_plaid_connection
        self.is_account_closed = is_account_closed
        self.is_account_frozen_or_restricted = is_account_frozen_or_restricted
        self.total_plaid_connections_count = total_plaid_connections_count
        self.plaid_connections_count_7d = plaid_connections_count_7d
        self.plaid_connections_count_30d = plaid_connections_count_30d
        self.failed_plaid_non_oauth_authentication_attempts_count_3d = failed_plaid_non_oauth_authentication_attempts_count_3d
        self.plaid_non_oauth_authentication_attempts_count_3d = plaid_non_oauth_authentication_attempts_count_3d
        self.failed_plaid_non_oauth_authentication_attempts_count_7d = failed_plaid_non_oauth_authentication_attempts_count_7d
        self.plaid_non_oauth_authentication_attempts_count_7d = plaid_non_oauth_authentication_attempts_count_7d
        self.failed_plaid_non_oauth_authentication_attempts_count_30d = failed_plaid_non_oauth_authentication_attempts_count_30d
        self.plaid_non_oauth_authentication_attempts_count_30d = plaid_non_oauth_authentication_attempts_count_30d
        self.distinct_ip_addresses_count_3d = distinct_ip_addresses_count_3d
        self.distinct_ip_addresses_count_7d = distinct_ip_addresses_count_7d
        self.distinct_ip_addresses_count_30d = distinct_ip_addresses_count_30d
        self.distinct_ip_addresses_count_90d = distinct_ip_addresses_count_90d
        self.distinct_user_agents_count_3d = distinct_user_agents_count_3d
        self.distinct_user_agents_count_7d = distinct_user_agents_count_7d
        self.distinct_user_agents_count_30d = distinct_user_agents_count_30d
        self.distinct_user_agents_count_90d = distinct_user_agents_count_90d
        self.address_change_count_28d = address_change_count_28d
        self.email_change_count_28d = email_change_count_28d
        self.phone_change_count_28d = phone_change_count_28d
        self.address_change_count_90d = address_change_count_90d
        self.email_change_count_90d = email_change_count_90d
        self.phone_change_count_90d = phone_change_count_90d
        self.days_since_account_opening = days_since_account_opening
        self.days_since_first_observed_transaction = days_since_first_observed_transaction
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
