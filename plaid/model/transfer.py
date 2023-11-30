"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.474.3
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
    from plaid.model.ach_class import ACHClass
    from plaid.model.transfer_authorization_guarantee_decision import TransferAuthorizationGuaranteeDecision
    from plaid.model.transfer_authorization_guarantee_decision_rationale import TransferAuthorizationGuaranteeDecisionRationale
    from plaid.model.transfer_expected_sweep_settlement_schedule_item import TransferExpectedSweepSettlementScheduleItem
    from plaid.model.transfer_failure import TransferFailure
    from plaid.model.transfer_metadata import TransferMetadata
    from plaid.model.transfer_network import TransferNetwork
    from plaid.model.transfer_refund import TransferRefund
    from plaid.model.transfer_status import TransferStatus
    from plaid.model.transfer_sweep_status import TransferSweepStatus
    from plaid.model.transfer_type import TransferType
    from plaid.model.transfer_user_in_response import TransferUserInResponse
    globals()['ACHClass'] = ACHClass
    globals()['TransferAuthorizationGuaranteeDecision'] = TransferAuthorizationGuaranteeDecision
    globals()['TransferAuthorizationGuaranteeDecisionRationale'] = TransferAuthorizationGuaranteeDecisionRationale
    globals()['TransferExpectedSweepSettlementScheduleItem'] = TransferExpectedSweepSettlementScheduleItem
    globals()['TransferFailure'] = TransferFailure
    globals()['TransferMetadata'] = TransferMetadata
    globals()['TransferNetwork'] = TransferNetwork
    globals()['TransferRefund'] = TransferRefund
    globals()['TransferStatus'] = TransferStatus
    globals()['TransferSweepStatus'] = TransferSweepStatus
    globals()['TransferType'] = TransferType
    globals()['TransferUserInResponse'] = TransferUserInResponse


class Transfer(ModelNormal):
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
            'id': (str,),  # noqa: E501
            'authorization_id': (str,),  # noqa: E501
            'funding_account_id': (str, none_type,),  # noqa: E501
            'type': (TransferType,),  # noqa: E501
            'user': (TransferUserInResponse,),  # noqa: E501
            'amount': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'created': (datetime,),  # noqa: E501
            'status': (TransferStatus,),  # noqa: E501
            'network': (TransferNetwork,),  # noqa: E501
            'cancellable': (bool,),  # noqa: E501
            'failure_reason': (TransferFailure,),  # noqa: E501
            'metadata': (TransferMetadata,),  # noqa: E501
            'origination_account_id': (str,),  # noqa: E501
            'guarantee_decision': (TransferAuthorizationGuaranteeDecision,),  # noqa: E501
            'guarantee_decision_rationale': (TransferAuthorizationGuaranteeDecisionRationale,),  # noqa: E501
            'iso_currency_code': (str,),  # noqa: E501
            'standard_return_window': (date, none_type,),  # noqa: E501
            'unauthorized_return_window': (date, none_type,),  # noqa: E501
            'expected_settlement_date': (date, none_type,),  # noqa: E501
            'originator_client_id': (str, none_type,),  # noqa: E501
            'refunds': ([TransferRefund],),  # noqa: E501
            'recurring_transfer_id': (str, none_type,),  # noqa: E501
            'credit_funds_source': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'ach_class': (ACHClass,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'sweep_status': (TransferSweepStatus,),  # noqa: E501
            'expected_sweep_settlement_schedule': ([TransferExpectedSweepSettlementScheduleItem],),  # noqa: E501
            'facilitator_fee': (str,),  # noqa: E501
            'network_trace_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'authorization_id': 'authorization_id',  # noqa: E501
        'funding_account_id': 'funding_account_id',  # noqa: E501
        'type': 'type',  # noqa: E501
        'user': 'user',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'description': 'description',  # noqa: E501
        'created': 'created',  # noqa: E501
        'status': 'status',  # noqa: E501
        'network': 'network',  # noqa: E501
        'cancellable': 'cancellable',  # noqa: E501
        'failure_reason': 'failure_reason',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'origination_account_id': 'origination_account_id',  # noqa: E501
        'guarantee_decision': 'guarantee_decision',  # noqa: E501
        'guarantee_decision_rationale': 'guarantee_decision_rationale',  # noqa: E501
        'iso_currency_code': 'iso_currency_code',  # noqa: E501
        'standard_return_window': 'standard_return_window',  # noqa: E501
        'unauthorized_return_window': 'unauthorized_return_window',  # noqa: E501
        'expected_settlement_date': 'expected_settlement_date',  # noqa: E501
        'originator_client_id': 'originator_client_id',  # noqa: E501
        'refunds': 'refunds',  # noqa: E501
        'recurring_transfer_id': 'recurring_transfer_id',  # noqa: E501
        'credit_funds_source': 'credit_funds_source',  # noqa: E501
        'ach_class': 'ach_class',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'sweep_status': 'sweep_status',  # noqa: E501
        'expected_sweep_settlement_schedule': 'expected_sweep_settlement_schedule',  # noqa: E501
        'facilitator_fee': 'facilitator_fee',  # noqa: E501
        'network_trace_id': 'network_trace_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, authorization_id, funding_account_id, type, user, amount, description, created, status, network, cancellable, failure_reason, metadata, origination_account_id, guarantee_decision, guarantee_decision_rationale, iso_currency_code, standard_return_window, unauthorized_return_window, expected_settlement_date, originator_client_id, refunds, recurring_transfer_id, credit_funds_source, *args, **kwargs):  # noqa: E501
        """Transfer - a model defined in OpenAPI

        Args:
            id (str): Plaid’s unique identifier for a transfer.
            authorization_id (str): Plaid’s unique identifier for a transfer authorization.
            funding_account_id (str, none_type): The id of the associated funding account, available in the Plaid Dashboard. If present, this indicates which of your business checking accounts will be credited or debited.
            type (TransferType):
            user (TransferUserInResponse):
            amount (str): The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\"). When calling `/transfer/authorization/create`, specify the maximum amount to authorize. When calling `/transfer/create`, specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when calling `/transfer/create`, the maximum amount authorized in the `authorization_id` will be sent.
            description (str): The description of the transfer.
            created (datetime): The datetime when this transfer was created. This will be of the form `2006-01-02T15:04:05Z`
            status (TransferStatus):
            network (TransferNetwork):
            cancellable (bool): When `true`, you can still cancel this transfer.
            failure_reason (TransferFailure):
            metadata (TransferMetadata):
            origination_account_id (str): Plaid’s unique identifier for the origination account that was used for this transfer.
            guarantee_decision (TransferAuthorizationGuaranteeDecision):
            guarantee_decision_rationale (TransferAuthorizationGuaranteeDecisionRationale):
            iso_currency_code (str): The currency of the transfer amount, e.g. \"USD\"
            standard_return_window (date, none_type): The date 3 business days from settlement date indicating the following ACH returns can no longer happen: R01, R02, R03, R29. This will be of the form YYYY-MM-DD.
            unauthorized_return_window (date, none_type): The date 61 business days from settlement date indicating the following ACH returns can no longer happen: R05, R07, R10, R11, R51, R33, R37, R38, R51, R52, R53. This will be of the form YYYY-MM-DD.
            expected_settlement_date (date, none_type): The expected date when the full amount of the transfer settles at the consumers’ account, if the transfer is credit; or at the customer's business checking account, if the transfer is debit. Only set for ACH transfers and is null for non-ACH transfers. Only set for ACH transfers. This will be of the form YYYY-MM-DD.
            originator_client_id (str, none_type): The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client as a [Platform customer](https://plaid.com/docs/transfer/application/#originators-vs-platforms).
            refunds ([TransferRefund]): A list of refunds associated with this transfer.
            recurring_transfer_id (str, none_type): The id of the recurring transfer if this transfer belongs to a recurring transfer.
            credit_funds_source (bool, date, datetime, dict, float, int, list, str, none_type):

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
            ach_class (ACHClass): [optional]  # noqa: E501
            account_id (str): The Plaid `account_id` corresponding to the end-user account that will be debited or credited.. [optional]  # noqa: E501
            sweep_status (TransferSweepStatus): [optional]  # noqa: E501
            expected_sweep_settlement_schedule ([TransferExpectedSweepSettlementScheduleItem]): The expected sweep settlement schedule of this transfer, assuming this transfer is not `returned`. Only applies to ACH debit transfers.. [optional]  # noqa: E501
            facilitator_fee (str): The amount to deduct from `transfer.amount` and distribute to the platform’s Ledger balance as a facilitator fee (decimal string with two digits of precision e.g. \"10.00\"). The remainder will go to the end-customer’s Ledger balance. This must be less than or equal to the `transfer.amount`.. [optional]  # noqa: E501
            network_trace_id (str, none_type): The trace identifier for the transfer based on its network. This will only be set after the transfer has posted.  For `ach` or `same-day-ach` transfers, this is the ACH trace number. Currently, the field will remain null for transfers on other rails.. [optional]  # noqa: E501
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

        self.id = id
        self.authorization_id = authorization_id
        self.funding_account_id = funding_account_id
        self.type = type
        self.user = user
        self.amount = amount
        self.description = description
        self.created = created
        self.status = status
        self.network = network
        self.cancellable = cancellable
        self.failure_reason = failure_reason
        self.metadata = metadata
        self.origination_account_id = origination_account_id
        self.guarantee_decision = guarantee_decision
        self.guarantee_decision_rationale = guarantee_decision_rationale
        self.iso_currency_code = iso_currency_code
        self.standard_return_window = standard_return_window
        self.unauthorized_return_window = unauthorized_return_window
        self.expected_settlement_date = expected_settlement_date
        self.originator_client_id = originator_client_id
        self.refunds = refunds
        self.recurring_transfer_id = recurring_transfer_id
        self.credit_funds_source = credit_funds_source
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
    def __init__(self, id, authorization_id, funding_account_id, type, user, amount, description, created, status, network, cancellable, failure_reason, metadata, origination_account_id, guarantee_decision, guarantee_decision_rationale, iso_currency_code, standard_return_window, unauthorized_return_window, expected_settlement_date, originator_client_id, refunds, recurring_transfer_id, credit_funds_source, *args, **kwargs):  # noqa: E501
        """Transfer - a model defined in OpenAPI

        Args:
            id (str): Plaid’s unique identifier for a transfer.
            authorization_id (str): Plaid’s unique identifier for a transfer authorization.
            funding_account_id (str, none_type): The id of the associated funding account, available in the Plaid Dashboard. If present, this indicates which of your business checking accounts will be credited or debited.
            type (TransferType):
            user (TransferUserInResponse):
            amount (str): The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\"). When calling `/transfer/authorization/create`, specify the maximum amount to authorize. When calling `/transfer/create`, specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when calling `/transfer/create`, the maximum amount authorized in the `authorization_id` will be sent.
            description (str): The description of the transfer.
            created (datetime): The datetime when this transfer was created. This will be of the form `2006-01-02T15:04:05Z`
            status (TransferStatus):
            network (TransferNetwork):
            cancellable (bool): When `true`, you can still cancel this transfer.
            failure_reason (TransferFailure):
            metadata (TransferMetadata):
            origination_account_id (str): Plaid’s unique identifier for the origination account that was used for this transfer.
            guarantee_decision (TransferAuthorizationGuaranteeDecision):
            guarantee_decision_rationale (TransferAuthorizationGuaranteeDecisionRationale):
            iso_currency_code (str): The currency of the transfer amount, e.g. \"USD\"
            standard_return_window (date, none_type): The date 3 business days from settlement date indicating the following ACH returns can no longer happen: R01, R02, R03, R29. This will be of the form YYYY-MM-DD.
            unauthorized_return_window (date, none_type): The date 61 business days from settlement date indicating the following ACH returns can no longer happen: R05, R07, R10, R11, R51, R33, R37, R38, R51, R52, R53. This will be of the form YYYY-MM-DD.
            expected_settlement_date (date, none_type): The expected date when the full amount of the transfer settles at the consumers’ account, if the transfer is credit; or at the customer's business checking account, if the transfer is debit. Only set for ACH transfers and is null for non-ACH transfers. Only set for ACH transfers. This will be of the form YYYY-MM-DD.
            originator_client_id (str, none_type): The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client as a [Platform customer](https://plaid.com/docs/transfer/application/#originators-vs-platforms).
            refunds ([TransferRefund]): A list of refunds associated with this transfer.
            recurring_transfer_id (str, none_type): The id of the recurring transfer if this transfer belongs to a recurring transfer.
            credit_funds_source (bool, date, datetime, dict, float, int, list, str, none_type):

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
            ach_class (ACHClass): [optional]  # noqa: E501
            account_id (str): The Plaid `account_id` corresponding to the end-user account that will be debited or credited.. [optional]  # noqa: E501
            sweep_status (TransferSweepStatus): [optional]  # noqa: E501
            expected_sweep_settlement_schedule ([TransferExpectedSweepSettlementScheduleItem]): The expected sweep settlement schedule of this transfer, assuming this transfer is not `returned`. Only applies to ACH debit transfers.. [optional]  # noqa: E501
            facilitator_fee (str): The amount to deduct from `transfer.amount` and distribute to the platform’s Ledger balance as a facilitator fee (decimal string with two digits of precision e.g. \"10.00\"). The remainder will go to the end-customer’s Ledger balance. This must be less than or equal to the `transfer.amount`.. [optional]  # noqa: E501
            network_trace_id (str, none_type): The trace identifier for the transfer based on its network. This will only be set after the transfer has posted.  For `ach` or `same-day-ach` transfers, this is the ACH trace number. Currently, the field will remain null for transfers on other rails.. [optional]  # noqa: E501
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

        self.id = id
        self.authorization_id = authorization_id
        self.funding_account_id = funding_account_id
        self.type = type
        self.user = user
        self.amount = amount
        self.description = description
        self.created = created
        self.status = status
        self.network = network
        self.cancellable = cancellable
        self.failure_reason = failure_reason
        self.metadata = metadata
        self.origination_account_id = origination_account_id
        self.guarantee_decision = guarantee_decision
        self.guarantee_decision_rationale = guarantee_decision_rationale
        self.iso_currency_code = iso_currency_code
        self.standard_return_window = standard_return_window
        self.unauthorized_return_window = unauthorized_return_window
        self.expected_settlement_date = expected_settlement_date
        self.originator_client_id = originator_client_id
        self.refunds = refunds
        self.recurring_transfer_id = recurring_transfer_id
        self.credit_funds_source = credit_funds_source
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
