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
    from plaid.model.option_contract import OptionContract
    globals()['OptionContract'] = OptionContract


class Security(ModelNormal):
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
            'security_id': (str,),  # noqa: E501
            'isin': (str, none_type,),  # noqa: E501
            'cusip': (str, none_type,),  # noqa: E501
            'sedol': (str, none_type,),  # noqa: E501
            'institution_security_id': (str, none_type,),  # noqa: E501
            'institution_id': (str, none_type,),  # noqa: E501
            'proxy_security_id': (str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'ticker_symbol': (str, none_type,),  # noqa: E501
            'is_cash_equivalent': (bool, none_type,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
            'close_price': (float, none_type,),  # noqa: E501
            'close_price_as_of': (date, none_type,),  # noqa: E501
            'iso_currency_code': (str, none_type,),  # noqa: E501
            'unofficial_currency_code': (str, none_type,),  # noqa: E501
            'market_identifier_code': (str, none_type,),  # noqa: E501
            'sector': (str, none_type,),  # noqa: E501
            'industry': (str, none_type,),  # noqa: E501
            'option_contract': (OptionContract,),  # noqa: E501
            'update_datetime': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'security_id': 'security_id',  # noqa: E501
        'isin': 'isin',  # noqa: E501
        'cusip': 'cusip',  # noqa: E501
        'sedol': 'sedol',  # noqa: E501
        'institution_security_id': 'institution_security_id',  # noqa: E501
        'institution_id': 'institution_id',  # noqa: E501
        'proxy_security_id': 'proxy_security_id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'ticker_symbol': 'ticker_symbol',  # noqa: E501
        'is_cash_equivalent': 'is_cash_equivalent',  # noqa: E501
        'type': 'type',  # noqa: E501
        'close_price': 'close_price',  # noqa: E501
        'close_price_as_of': 'close_price_as_of',  # noqa: E501
        'iso_currency_code': 'iso_currency_code',  # noqa: E501
        'unofficial_currency_code': 'unofficial_currency_code',  # noqa: E501
        'market_identifier_code': 'market_identifier_code',  # noqa: E501
        'sector': 'sector',  # noqa: E501
        'industry': 'industry',  # noqa: E501
        'option_contract': 'option_contract',  # noqa: E501
        'update_datetime': 'update_datetime',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, security_id, isin, cusip, sedol, institution_security_id, institution_id, proxy_security_id, name, ticker_symbol, is_cash_equivalent, type, close_price, close_price_as_of, iso_currency_code, unofficial_currency_code, market_identifier_code, sector, industry, option_contract, *args, **kwargs):  # noqa: E501
        """Security - a model defined in OpenAPI

        Args:
            security_id (str): A unique, Plaid-specific identifier for the security, used to associate securities with holdings. Like all Plaid identifiers, the `security_id` is case sensitive. The `security_id` may change if inherent details of the security change due to a corporate action, for example, in the event of a ticker symbol change or CUSIP change.
            isin (str, none_type): 12-character ISIN, a globally unique securities identifier. A verified CUSIP Global Services license is required to receive this data. This field will be null by default for new customers, and null for existing customers starting March 12, 2024. If you would like access to this field, please start the verification process [here](https://docs.google.com/forms/d/e/1FAIpQLSd9asHEYEfmf8fxJTHZTAfAzW4dugsnSu-HS2J51f1mxwd6Sw/viewform).
            cusip (str, none_type): 9-character CUSIP, an identifier assigned to North American securities. A verified CUSIP Global Services license is required to receive this data. This field will be null by default for new customers, and null for existing customers starting March 12, 2024. If you would like access to this field, please start the verification process [here](https://docs.google.com/forms/d/e/1FAIpQLSd9asHEYEfmf8fxJTHZTAfAzW4dugsnSu-HS2J51f1mxwd6Sw/viewform).
            sedol (str, none_type): 7-character SEDOL, an identifier assigned to securities in the UK.
            institution_security_id (str, none_type): An identifier given to the security by the institution
            institution_id (str, none_type): If `institution_security_id` is present, this field indicates the Plaid `institution_id` of the institution to whom the identifier belongs.
            proxy_security_id (str, none_type): In certain cases, Plaid will provide the ID of another security whose performance resembles this security, typically when the original security has low volume, or when a private security can be modeled with a publicly traded security.
            name (str, none_type): A descriptive name for the security, suitable for display.
            ticker_symbol (str, none_type): The security’s trading symbol for publicly traded securities, and otherwise a short identifier if available.
            is_cash_equivalent (bool, none_type): Indicates that a security is a highly liquid asset and can be treated like cash.
            type (str, none_type): The security type of the holding.  In rare instances, a null value is returned when institutional data is insufficient to determine the security type.  Valid security types are:  `cash`: Cash, currency, and money market funds  `cryptocurrency`: Digital or virtual currencies  `derivative`: Options, warrants, and other derivative instruments  `equity`: Domestic and foreign equities  `etf`: Multi-asset exchange-traded investment funds  `fixed income`: Bonds and certificates of deposit (CDs)  `loan`: Loans and loan receivables  `mutual fund`: Open- and closed-end vehicles pooling funds of multiple investors  `other`: Unknown or other investment types
            close_price (float, none_type): Price of the security at the close of the previous trading session. Null for non-public securities.  If the security is a foreign currency this field will be updated daily and will be priced in USD.  If the security is a cryptocurrency, this field will be updated multiple times a day. As crypto prices can fluctuate quickly and data may become stale sooner than other asset classes, refer to `update_datetime` with the time when the price was last updated. 
            close_price_as_of (date, none_type): Date for which `close_price` is accurate. Always `null` if `close_price` is `null`.
            iso_currency_code (str, none_type): The ISO-4217 currency code of the price given. Always `null` if `unofficial_currency_code` is non-`null`.
            unofficial_currency_code (str, none_type): The unofficial currency code associated with the security. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
            market_identifier_code (str, none_type): The ISO-10383 Market Identifier Code of the exchange or market in which the security is being traded.
            sector (str, none_type): The sector classification of the security, such as Finance, Health Technology, etc.  For a complete list of possible values, please refer to the [\"Sectors and Industries\" spreadsheet](https://docs.google.com/spreadsheets/d/1L7aXUdqLhxgM8qe7hK67qqKXiUdQqILpwZ0LpxvCVnc).
            industry (str, none_type): The industry classification of the security, such as Biotechnology, Airlines, etc.  For a complete list of possible values, please refer to the [\"Sectors and Industries\" spreadsheet](https://docs.google.com/spreadsheets/d/1L7aXUdqLhxgM8qe7hK67qqKXiUdQqILpwZ0LpxvCVnc).
            option_contract (OptionContract):

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
            update_datetime (datetime, none_type): Date and time at which `close_price` is accurate, in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ). Always `null` if `close_price` is `null`.. [optional]  # noqa: E501
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

        self.security_id = security_id
        self.isin = isin
        self.cusip = cusip
        self.sedol = sedol
        self.institution_security_id = institution_security_id
        self.institution_id = institution_id
        self.proxy_security_id = proxy_security_id
        self.name = name
        self.ticker_symbol = ticker_symbol
        self.is_cash_equivalent = is_cash_equivalent
        self.type = type
        self.close_price = close_price
        self.close_price_as_of = close_price_as_of
        self.iso_currency_code = iso_currency_code
        self.unofficial_currency_code = unofficial_currency_code
        self.market_identifier_code = market_identifier_code
        self.sector = sector
        self.industry = industry
        self.option_contract = option_contract
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
    def __init__(self, security_id, isin, cusip, sedol, institution_security_id, institution_id, proxy_security_id, name, ticker_symbol, is_cash_equivalent, type, close_price, close_price_as_of, iso_currency_code, unofficial_currency_code, market_identifier_code, sector, industry, option_contract, *args, **kwargs):  # noqa: E501
        """Security - a model defined in OpenAPI

        Args:
            security_id (str): A unique, Plaid-specific identifier for the security, used to associate securities with holdings. Like all Plaid identifiers, the `security_id` is case sensitive. The `security_id` may change if inherent details of the security change due to a corporate action, for example, in the event of a ticker symbol change or CUSIP change.
            isin (str, none_type): 12-character ISIN, a globally unique securities identifier. A verified CUSIP Global Services license is required to receive this data. This field will be null by default for new customers, and null for existing customers starting March 12, 2024. If you would like access to this field, please start the verification process [here](https://docs.google.com/forms/d/e/1FAIpQLSd9asHEYEfmf8fxJTHZTAfAzW4dugsnSu-HS2J51f1mxwd6Sw/viewform).
            cusip (str, none_type): 9-character CUSIP, an identifier assigned to North American securities. A verified CUSIP Global Services license is required to receive this data. This field will be null by default for new customers, and null for existing customers starting March 12, 2024. If you would like access to this field, please start the verification process [here](https://docs.google.com/forms/d/e/1FAIpQLSd9asHEYEfmf8fxJTHZTAfAzW4dugsnSu-HS2J51f1mxwd6Sw/viewform).
            sedol (str, none_type): 7-character SEDOL, an identifier assigned to securities in the UK.
            institution_security_id (str, none_type): An identifier given to the security by the institution
            institution_id (str, none_type): If `institution_security_id` is present, this field indicates the Plaid `institution_id` of the institution to whom the identifier belongs.
            proxy_security_id (str, none_type): In certain cases, Plaid will provide the ID of another security whose performance resembles this security, typically when the original security has low volume, or when a private security can be modeled with a publicly traded security.
            name (str, none_type): A descriptive name for the security, suitable for display.
            ticker_symbol (str, none_type): The security’s trading symbol for publicly traded securities, and otherwise a short identifier if available.
            is_cash_equivalent (bool, none_type): Indicates that a security is a highly liquid asset and can be treated like cash.
            type (str, none_type): The security type of the holding.  In rare instances, a null value is returned when institutional data is insufficient to determine the security type.  Valid security types are:  `cash`: Cash, currency, and money market funds  `cryptocurrency`: Digital or virtual currencies  `derivative`: Options, warrants, and other derivative instruments  `equity`: Domestic and foreign equities  `etf`: Multi-asset exchange-traded investment funds  `fixed income`: Bonds and certificates of deposit (CDs)  `loan`: Loans and loan receivables  `mutual fund`: Open- and closed-end vehicles pooling funds of multiple investors  `other`: Unknown or other investment types
            close_price (float, none_type): Price of the security at the close of the previous trading session. Null for non-public securities.  If the security is a foreign currency this field will be updated daily and will be priced in USD.  If the security is a cryptocurrency, this field will be updated multiple times a day. As crypto prices can fluctuate quickly and data may become stale sooner than other asset classes, refer to `update_datetime` with the time when the price was last updated. 
            close_price_as_of (date, none_type): Date for which `close_price` is accurate. Always `null` if `close_price` is `null`.
            iso_currency_code (str, none_type): The ISO-4217 currency code of the price given. Always `null` if `unofficial_currency_code` is non-`null`.
            unofficial_currency_code (str, none_type): The unofficial currency code associated with the security. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
            market_identifier_code (str, none_type): The ISO-10383 Market Identifier Code of the exchange or market in which the security is being traded.
            sector (str, none_type): The sector classification of the security, such as Finance, Health Technology, etc.  For a complete list of possible values, please refer to the [\"Sectors and Industries\" spreadsheet](https://docs.google.com/spreadsheets/d/1L7aXUdqLhxgM8qe7hK67qqKXiUdQqILpwZ0LpxvCVnc).
            industry (str, none_type): The industry classification of the security, such as Biotechnology, Airlines, etc.  For a complete list of possible values, please refer to the [\"Sectors and Industries\" spreadsheet](https://docs.google.com/spreadsheets/d/1L7aXUdqLhxgM8qe7hK67qqKXiUdQqILpwZ0LpxvCVnc).
            option_contract (OptionContract):

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
            update_datetime (datetime, none_type): Date and time at which `close_price` is accurate, in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ). Always `null` if `close_price` is `null`.. [optional]  # noqa: E501
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

        self.security_id = security_id
        self.isin = isin
        self.cusip = cusip
        self.sedol = sedol
        self.institution_security_id = institution_security_id
        self.institution_id = institution_id
        self.proxy_security_id = proxy_security_id
        self.name = name
        self.ticker_symbol = ticker_symbol
        self.is_cash_equivalent = is_cash_equivalent
        self.type = type
        self.close_price = close_price
        self.close_price_as_of = close_price_as_of
        self.iso_currency_code = iso_currency_code
        self.unofficial_currency_code = unofficial_currency_code
        self.market_identifier_code = market_identifier_code
        self.sector = sector
        self.industry = industry
        self.option_contract = option_contract
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
