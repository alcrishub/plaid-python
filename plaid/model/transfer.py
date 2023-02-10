"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
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
)

def lazy_import():
    from plaid.model.ach_class import ACHClass
    from plaid.model.transfer_authorization_guarantee_decision import TransferAuthorizationGuaranteeDecision
    from plaid.model.transfer_authorization_guarantee_decision_rationale import TransferAuthorizationGuaranteeDecisionRationale
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
            'funding_account_id': (str,),  # noqa: E501
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
            'ach_class': (ACHClass,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'sweep_status': (TransferSweepStatus,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
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
        'ach_class': 'ach_class',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'sweep_status': 'sweep_status',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, funding_account_id, type, user, amount, description, created, status, network, cancellable, failure_reason, metadata, origination_account_id, guarantee_decision, guarantee_decision_rationale, iso_currency_code, standard_return_window, unauthorized_return_window, expected_settlement_date, originator_client_id, refunds, recurring_transfer_id, *args, **kwargs):  # noqa: E501
        """Transfer - a model defined in OpenAPI

        Args:
            id (str): Plaid’s unique identifier for a transfer.
            funding_account_id (str): The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited.
            type (TransferType):
            user (TransferUserInResponse):
            amount (str): The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\").
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
            expected_settlement_date (date, none_type): An estimation of the settlement date which can be useful when the transfer is `pending`. Only set for ACH transfers and is `null` for non-ACH transfers. This will be of the form YYYY-MM-DD.
            originator_client_id (str, none_type): The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client as a third-party sender (TPS).
            refunds ([TransferRefund]): A list of refunds associated with this transfer.
            recurring_transfer_id (str, none_type): The id of the recurring transfer if this transfer belongs to a recurring transfer.

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
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
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
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
