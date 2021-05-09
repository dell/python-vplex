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


class AmpApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_array_management_provider(self, cluster_name, name, **kwargs):  # noqa: E501
        """Returns the details of an AMP  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.get_array_management_provider(cluster_name, name, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: ArrayManagementProvider
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_http_request'):
            return self.get_array_management_provider_with_http_info(cluster_name, name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_array_management_provider_with_http_info(cluster_name, name, **kwargs)  # noqa: E501
            return data

    def get_array_management_provider_with_http_info(self, cluster_name, name, **kwargs):  # noqa: E501
        """Returns the details of an AMP  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.get_array_management_provider_with_http_info(cluster_name, name, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: ArrayManagementProvider
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'name', 'fields']  # noqa: E501
        all_params.append('async_http_request')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_array_management_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `get_array_management_provider`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_array_management_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_name' in params:
            path_params['cluster_name'] = params['cluster_name']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{cluster_name}/array_management_providers/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArrayManagementProvider',  # noqa: E501
            auth_settings=auth_settings,
            async_http_request=params.get('async_http_request'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_array_management_providers(self, cluster_name, **kwargs):  # noqa: E501
        """Returns a list of registered AMPs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.get_array_management_providers(cluster_name, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param int offset: Index of the first element to include in paginated results.<br> <b>'limit' must also be specified.</b>
        :param int limit: <p>Maximum number of elements to include in paginated results.<br> <b>'offset' must also be specified.<b>
        :param str sort_by: Specify the field priority order and direction for sorting.  See SortingOrderExpression for details. 
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :param str connectivity_status: Filter results by connectivity_status. See LexicalQueryExpression for details.
        :return: list[ArrayManagementProvider]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_http_request'):
            return self.get_array_management_providers_with_http_info(cluster_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_array_management_providers_with_http_info(cluster_name, **kwargs)  # noqa: E501
            return data

    def get_array_management_providers_with_http_info(self, cluster_name, **kwargs):  # noqa: E501
        """Returns a list of registered AMPs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.get_array_management_providers_with_http_info(cluster_name, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param int offset: Index of the first element to include in paginated results.<br> <b>'limit' must also be specified.</b>
        :param int limit: <p>Maximum number of elements to include in paginated results.<br> <b>'offset' must also be specified.<b>
        :param str sort_by: Specify the field priority order and direction for sorting.  See SortingOrderExpression for details. 
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :param str connectivity_status: Filter results by connectivity_status. See LexicalQueryExpression for details.
        :return: list[ArrayManagementProvider]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'offset', 'limit', 'sort_by', 'fields', 'connectivity_status']  # noqa: E501
        all_params.append('async_http_request')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_array_management_providers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `get_array_management_providers`")  # noqa: E501

        if 'offset' in params and params['offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `get_array_management_providers`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_array_management_providers`, must be a value less than or equal to `100`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_array_management_providers`, must be a value greater than or equal to `1`")  # noqa: E501
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
        if 'connectivity_status' in params:
            query_params.append(('connectivity_status', params['connectivity_status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{cluster_name}/array_management_providers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ArrayManagementProvider]',  # noqa: E501
            auth_settings=auth_settings,
            async_http_request=params.get('async_http_request'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def register_array_management_provider(self, cluster_name, amp_payload, **kwargs):  # noqa: E501
        """Register a new ArrayManagementProvider  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.register_array_management_provider(cluster_name, amp_payload, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param AmpPayload amp_payload: (required)
        :return: ArrayManagementProvider
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_http_request'):
            return self.register_array_management_provider_with_http_info(cluster_name, amp_payload, **kwargs)  # noqa: E501
        else:
            (data) = self.register_array_management_provider_with_http_info(cluster_name, amp_payload, **kwargs)  # noqa: E501
            return data

    def register_array_management_provider_with_http_info(self, cluster_name, amp_payload, **kwargs):  # noqa: E501
        """Register a new ArrayManagementProvider  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.register_array_management_provider_with_http_info(cluster_name, amp_payload, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param AmpPayload amp_payload: (required)
        :return: ArrayManagementProvider
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'amp_payload']  # noqa: E501
        all_params.append('async_http_request')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register_array_management_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `register_array_management_provider`")  # noqa: E501
        # verify the required parameter 'amp_payload' is set
        if ('amp_payload' not in params or
                params['amp_payload'] is None):
            raise ValueError("Missing the required parameter `amp_payload` when calling `register_array_management_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_name' in params:
            path_params['cluster_name'] = params['cluster_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'amp_payload' in params:
            body_params = params['amp_payload']
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{cluster_name}/array_management_providers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArrayManagementProvider',  # noqa: E501
            auth_settings=auth_settings,
            async_http_request=params.get('async_http_request'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unregister_array_management_provider(self, cluster_name, name, **kwargs):  # noqa: E501
        """Unregisters an AMP  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.unregister_array_management_provider(cluster_name, name, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_http_request'):
            return self.unregister_array_management_provider_with_http_info(cluster_name, name, **kwargs)  # noqa: E501
        else:
            (data) = self.unregister_array_management_provider_with_http_info(cluster_name, name, **kwargs)  # noqa: E501
            return data

    def unregister_array_management_provider_with_http_info(self, cluster_name, name, **kwargs):  # noqa: E501
        """Unregisters an AMP  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.unregister_array_management_provider_with_http_info(cluster_name, name, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'name']  # noqa: E501
        all_params.append('async_http_request')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unregister_array_management_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `unregister_array_management_provider`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `unregister_array_management_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_name' in params:
            path_params['cluster_name'] = params['cluster_name']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{cluster_name}/array_management_providers/{name}', 'DELETE',
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
