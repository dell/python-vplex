# coding: utf-8

"""
    VPlex REST API

    A definition for the next-gen VPlex API  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vplexapi.api_client import ApiClient


class LicensesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_licenses(self, cluster_name, **kwargs):  # noqa: E501
        """Deletes the licenses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.delete_licenses(cluster_name, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_http_request'):
            return self.delete_licenses_with_http_info(cluster_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_licenses_with_http_info(cluster_name, **kwargs)  # noqa: E501
            return data

    def delete_licenses_with_http_info(self, cluster_name, **kwargs):  # noqa: E501
        """Deletes the licenses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.delete_licenses_with_http_info(cluster_name, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name']  # noqa: E501
        all_params.append('async_http_request')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_licenses" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `delete_licenses`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_name' in params:
            path_params['cluster_name'] = params['cluster_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{cluster_name}/licenses', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_http_request=params.get('async_http_request'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_license_info(self, cluster_name, **kwargs):  # noqa: E501
        """Returns a list of installed licenses on the setup  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.get_license_info(cluster_name, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param int offset: Index of the first element to include in paginated results.<br> <b>'limit' must also be specified.</b>
        :param int limit: <p>Maximum number of elements to include in paginated results.<br> <b>'offset' must also be specified.<b>
        :param str sort_by: Specify the field priority order and direction for sorting.  See SortingOrderExpression for details. 
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: LicenseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_http_request'):
            return self.get_license_info_with_http_info(cluster_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_license_info_with_http_info(cluster_name, **kwargs)  # noqa: E501
            return data

    def get_license_info_with_http_info(self, cluster_name, **kwargs):  # noqa: E501
        """Returns a list of installed licenses on the setup  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.get_license_info_with_http_info(cluster_name, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param int offset: Index of the first element to include in paginated results.<br> <b>'limit' must also be specified.</b>
        :param int limit: <p>Maximum number of elements to include in paginated results.<br> <b>'offset' must also be specified.<b>
        :param str sort_by: Specify the field priority order and direction for sorting.  See SortingOrderExpression for details. 
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: LicenseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'offset', 'limit', 'sort_by', 'fields']  # noqa: E501
        all_params.append('async_http_request')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_license_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `get_license_info`")  # noqa: E501

        if 'offset' in params and params['offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `get_license_info`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_license_info`, must be a value less than or equal to `100`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_license_info`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_name' in params:
            path_params['cluster_name'] = params['cluster_name']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{cluster_name}/licenses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LicenseArray',  # noqa: E501
            auth_settings=auth_settings,
            async_http_request=params.get('async_http_request'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def install_license(self, cluster_name, license_payload, **kwargs):  # noqa: E501
        """Install a new license file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.install_license(cluster_name, license_payload, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param LicensePayload license_payload: (required)
        :param bool validate:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_http_request'):
            return self.install_license_with_http_info(cluster_name, license_payload, **kwargs)  # noqa: E501
        else:
            (data) = self.install_license_with_http_info(cluster_name, license_payload, **kwargs)  # noqa: E501
            return data

    def install_license_with_http_info(self, cluster_name, license_payload, **kwargs):  # noqa: E501
        """Install a new license file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.install_license_with_http_info(cluster_name, license_payload, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param LicensePayload license_payload: (required)
        :param bool validate:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'license_payload', 'validate']  # noqa: E501
        all_params.append('async_http_request')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method install_license" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `install_license`")  # noqa: E501
        # verify the required parameter 'license_payload' is set
        if ('license_payload' not in params or
                params['license_payload'] is None):
            raise ValueError("Missing the required parameter `license_payload` when calling `install_license`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_name' in params:
            path_params['cluster_name'] = params['cluster_name']  # noqa: E501

        query_params = []
        if 'validate' in params:
            query_params.append(('validate', params['validate']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'license_payload' in params:
            body_params = params['license_payload']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{cluster_name}/licenses', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_http_request=params.get('async_http_request'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validate_license(self, cluster_name, validate_payload, **kwargs):  # noqa: E501
        """Validate a license file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.validate_license(cluster_name, validate_payload, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param ValidatePayload validate_payload: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_http_request'):
            return self.validate_license_with_http_info(cluster_name, validate_payload, **kwargs)  # noqa: E501
        else:
            (data) = self.validate_license_with_http_info(cluster_name, validate_payload, **kwargs)  # noqa: E501
            return data

    def validate_license_with_http_info(self, cluster_name, validate_payload, **kwargs):  # noqa: E501
        """Validate a license file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.validate_license_with_http_info(cluster_name, validate_payload, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param ValidatePayload validate_payload: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'validate_payload']  # noqa: E501
        all_params.append('async_http_request')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_license" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `validate_license`")  # noqa: E501
        # verify the required parameter 'validate_payload' is set
        if ('validate_payload' not in params or
                params['validate_payload'] is None):
            raise ValueError("Missing the required parameter `validate_payload` when calling `validate_license`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_name' in params:
            path_params['cluster_name'] = params['cluster_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'validate_payload' in params:
            body_params = params['validate_payload']
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{cluster_name}/licenses/validate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_http_request=params.get('async_http_request'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
