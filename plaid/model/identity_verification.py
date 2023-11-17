"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.470.1
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
    from plaid.model.client_user_id import ClientUserID
    from plaid.model.documentary_verification import DocumentaryVerification
    from plaid.model.identity_verification_status import IdentityVerificationStatus
    from plaid.model.identity_verification_step_summary import IdentityVerificationStepSummary
    from plaid.model.identity_verification_template_reference import IdentityVerificationTemplateReference
    from plaid.model.identity_verification_user_data import IdentityVerificationUserData
    from plaid.model.kyc_check_details import KYCCheckDetails
    from plaid.model.risk_check_details import RiskCheckDetails
    from plaid.model.selfie_check import SelfieCheck
    globals()['ClientUserID'] = ClientUserID
    globals()['DocumentaryVerification'] = DocumentaryVerification
    globals()['IdentityVerificationStatus'] = IdentityVerificationStatus
    globals()['IdentityVerificationStepSummary'] = IdentityVerificationStepSummary
    globals()['IdentityVerificationTemplateReference'] = IdentityVerificationTemplateReference
    globals()['IdentityVerificationUserData'] = IdentityVerificationUserData
    globals()['KYCCheckDetails'] = KYCCheckDetails
    globals()['RiskCheckDetails'] = RiskCheckDetails
    globals()['SelfieCheck'] = SelfieCheck


class IdentityVerification(ModelNormal):
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
            'client_user_id': (ClientUserID,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'completed_at': (datetime, none_type,),  # noqa: E501
            'previous_attempt_id': (str, none_type,),  # noqa: E501
            'shareable_url': (str, none_type,),  # noqa: E501
            'template': (IdentityVerificationTemplateReference,),  # noqa: E501
            'user': (IdentityVerificationUserData,),  # noqa: E501
            'status': (IdentityVerificationStatus,),  # noqa: E501
            'steps': (IdentityVerificationStepSummary,),  # noqa: E501
            'documentary_verification': (DocumentaryVerification,),  # noqa: E501
            'selfie_check': (SelfieCheck,),  # noqa: E501
            'kyc_check': (KYCCheckDetails,),  # noqa: E501
            'risk_check': (RiskCheckDetails,),  # noqa: E501
            'watchlist_screening_id': (str, none_type,),  # noqa: E501
            'redacted_at': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'client_user_id': 'client_user_id',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'completed_at': 'completed_at',  # noqa: E501
        'previous_attempt_id': 'previous_attempt_id',  # noqa: E501
        'shareable_url': 'shareable_url',  # noqa: E501
        'template': 'template',  # noqa: E501
        'user': 'user',  # noqa: E501
        'status': 'status',  # noqa: E501
        'steps': 'steps',  # noqa: E501
        'documentary_verification': 'documentary_verification',  # noqa: E501
        'selfie_check': 'selfie_check',  # noqa: E501
        'kyc_check': 'kyc_check',  # noqa: E501
        'risk_check': 'risk_check',  # noqa: E501
        'watchlist_screening_id': 'watchlist_screening_id',  # noqa: E501
        'redacted_at': 'redacted_at',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, client_user_id, created_at, completed_at, previous_attempt_id, shareable_url, template, user, status, steps, documentary_verification, selfie_check, kyc_check, risk_check, watchlist_screening_id, redacted_at, *args, **kwargs):  # noqa: E501
        """IdentityVerification - a model defined in OpenAPI

        Args:
            id (str): ID of the associated Identity Verification attempt.
            client_user_id (ClientUserID):
            created_at (datetime): An ISO8601 formatted timestamp.
            completed_at (datetime, none_type): An ISO8601 formatted timestamp.
            previous_attempt_id (str, none_type): The ID for the Identity Verification preceding this session. This field will only be filled if the current Identity Verification is a retry of a previous attempt.
            shareable_url (str, none_type): A shareable URL that can be sent directly to the user to complete verification
            template (IdentityVerificationTemplateReference):
            user (IdentityVerificationUserData):
            status (IdentityVerificationStatus):
            steps (IdentityVerificationStepSummary):
            documentary_verification (DocumentaryVerification):
            selfie_check (SelfieCheck):
            kyc_check (KYCCheckDetails):
            risk_check (RiskCheckDetails):
            watchlist_screening_id (str, none_type): ID of the associated screening.
            redacted_at (datetime, none_type): An ISO8601 formatted timestamp.

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

        self.id = id
        self.client_user_id = client_user_id
        self.created_at = created_at
        self.completed_at = completed_at
        self.previous_attempt_id = previous_attempt_id
        self.shareable_url = shareable_url
        self.template = template
        self.user = user
        self.status = status
        self.steps = steps
        self.documentary_verification = documentary_verification
        self.selfie_check = selfie_check
        self.kyc_check = kyc_check
        self.risk_check = risk_check
        self.watchlist_screening_id = watchlist_screening_id
        self.redacted_at = redacted_at
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
    def __init__(self, id, client_user_id, created_at, completed_at, previous_attempt_id, shareable_url, template, user, status, steps, documentary_verification, selfie_check, kyc_check, risk_check, watchlist_screening_id, redacted_at, *args, **kwargs):  # noqa: E501
        """IdentityVerification - a model defined in OpenAPI

        Args:
            id (str): ID of the associated Identity Verification attempt.
            client_user_id (ClientUserID):
            created_at (datetime): An ISO8601 formatted timestamp.
            completed_at (datetime, none_type): An ISO8601 formatted timestamp.
            previous_attempt_id (str, none_type): The ID for the Identity Verification preceding this session. This field will only be filled if the current Identity Verification is a retry of a previous attempt.
            shareable_url (str, none_type): A shareable URL that can be sent directly to the user to complete verification
            template (IdentityVerificationTemplateReference):
            user (IdentityVerificationUserData):
            status (IdentityVerificationStatus):
            steps (IdentityVerificationStepSummary):
            documentary_verification (DocumentaryVerification):
            selfie_check (SelfieCheck):
            kyc_check (KYCCheckDetails):
            risk_check (RiskCheckDetails):
            watchlist_screening_id (str, none_type): ID of the associated screening.
            redacted_at (datetime, none_type): An ISO8601 formatted timestamp.

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

        self.id = id
        self.client_user_id = client_user_id
        self.created_at = created_at
        self.completed_at = completed_at
        self.previous_attempt_id = previous_attempt_id
        self.shareable_url = shareable_url
        self.template = template
        self.user = user
        self.status = status
        self.steps = steps
        self.documentary_verification = documentary_verification
        self.selfie_check = selfie_check
        self.kyc_check = kyc_check
        self.risk_check = risk_check
        self.watchlist_screening_id = watchlist_screening_id
        self.redacted_at = redacted_at
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
