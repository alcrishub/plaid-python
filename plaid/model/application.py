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


class Application(ModelNormal):
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

    additional_properties_type = None

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
            'application_id': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'display_name': (str, none_type,),  # noqa: E501
            'join_date': (date,),  # noqa: E501
            'logo_url': (str, none_type,),  # noqa: E501
            'application_url': (str, none_type,),  # noqa: E501
            'reason_for_access': (str, none_type,),  # noqa: E501
            'use_case': (str, none_type,),  # noqa: E501
            'company_legal_name': (str, none_type,),  # noqa: E501
            'city': (str, none_type,),  # noqa: E501
            'region': (str, none_type,),  # noqa: E501
            'postal_code': (str, none_type,),  # noqa: E501
            'country_code': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'application_id': 'application_id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'display_name': 'display_name',  # noqa: E501
        'join_date': 'join_date',  # noqa: E501
        'logo_url': 'logo_url',  # noqa: E501
        'application_url': 'application_url',  # noqa: E501
        'reason_for_access': 'reason_for_access',  # noqa: E501
        'use_case': 'use_case',  # noqa: E501
        'company_legal_name': 'company_legal_name',  # noqa: E501
        'city': 'city',  # noqa: E501
        'region': 'region',  # noqa: E501
        'postal_code': 'postal_code',  # noqa: E501
        'country_code': 'country_code',  # noqa: E501
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
    def __init__(self, application_id, name, display_name, join_date, logo_url, application_url, reason_for_access, use_case, company_legal_name, city, region, postal_code, country_code, *args, **kwargs):  # noqa: E501
        """Application - a model defined in OpenAPI

        Args:
            application_id (str): This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect.
            name (str): The name of the application
            display_name (str, none_type): A human-readable name of the application for display purposes
            join_date (date): The date this application was granted production access at Plaid in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC.
            logo_url (str, none_type): A URL that links to the application logo image.
            application_url (str, none_type): The URL for the application's website
            reason_for_access (str, none_type): A string provided by the connected app stating why they use their respective enabled products.
            use_case (str, none_type): A string representing client’s broad use case as assessed by Plaid.
            company_legal_name (str, none_type): A string representing the name of client’s legal entity.
            city (str, none_type): A string representing the city of the client’s headquarters.
            region (str, none_type): A string representing the region of the client’s headquarters.
            postal_code (str, none_type): A string representing the postal code of the client’s headquarters.
            country_code (str, none_type): A string representing the country code of the client’s headquarters.

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

        self.application_id = application_id
        self.name = name
        self.display_name = display_name
        self.join_date = join_date
        self.logo_url = logo_url
        self.application_url = application_url
        self.reason_for_access = reason_for_access
        self.use_case = use_case
        self.company_legal_name = company_legal_name
        self.city = city
        self.region = region
        self.postal_code = postal_code
        self.country_code = country_code
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
