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


class ExtentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_extent(self, cluster_name, extent_payload, **kwargs):  # noqa: E501
        """Create a new Extent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_extent(cluster_name, extent_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The name of the cluster (required)
        :param ExtentPayload extent_payload: (required)
        :param str x_include_object: When passed as part of a POST request, controls whether the representation of the newly created object is included in the response. Defaults to 'true' which will include the object in the response. This header is useful because refreshing the newly created object is usually the slowest part of a POST operation. 
        :return: Extent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_extent_with_http_info(cluster_name, extent_payload, **kwargs)  # noqa: E501
        else:
            (data) = self.create_extent_with_http_info(cluster_name, extent_payload, **kwargs)  # noqa: E501
            return data

    def create_extent_with_http_info(self, cluster_name, extent_payload, **kwargs):  # noqa: E501
        """Create a new Extent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_extent_with_http_info(cluster_name, extent_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The name of the cluster (required)
        :param ExtentPayload extent_payload: (required)
        :param str x_include_object: When passed as part of a POST request, controls whether the representation of the newly created object is included in the response. Defaults to 'true' which will include the object in the response. This header is useful because refreshing the newly created object is usually the slowest part of a POST operation. 
        :return: Extent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'extent_payload', 'x_include_object']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_extent" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `create_extent`")  # noqa: E501
        # verify the required parameter 'extent_payload' is set
        if ('extent_payload' not in params or
                params['extent_payload'] is None):
            raise ValueError("Missing the required parameter `extent_payload` when calling `create_extent`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_name' in params:
            path_params['cluster_name'] = params['cluster_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_include_object' in params:
            header_params['X-Include-Object'] = params['x_include_object']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'extent_payload' in params:
            body_params = params['extent_payload']
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{cluster_name}/extents', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Extent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_extent(self, cluster_name, name, **kwargs):  # noqa: E501
        """Delets a single Extent object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_extent(cluster_name, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_extent_with_http_info(cluster_name, name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_extent_with_http_info(cluster_name, name, **kwargs)  # noqa: E501
            return data

    def delete_extent_with_http_info(self, cluster_name, name, **kwargs):  # noqa: E501
        """Delets a single Extent object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_extent_with_http_info(cluster_name, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_extent" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `delete_extent`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete_extent`")  # noqa: E501

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
            '/clusters/{cluster_name}/extents/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_extent(self, cluster_name, name, **kwargs):  # noqa: E501
        """Returns a single Extent object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_extent(cluster_name, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: Extent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_extent_with_http_info(cluster_name, name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_extent_with_http_info(cluster_name, name, **kwargs)  # noqa: E501
            return data

    def get_extent_with_http_info(self, cluster_name, name, **kwargs):  # noqa: E501
        """Returns a single Extent object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_extent_with_http_info(cluster_name, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: Extent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'name', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_extent" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `get_extent`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_extent`")  # noqa: E501

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
            '/clusters/{cluster_name}/extents/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Extent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_extents(self, cluster_name, **kwargs):  # noqa: E501
        """Returns a list of Extent objects  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_extents(cluster_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: Filter results by name. See LexicalQueryExpression for details.
        :param str use: Filter results by use. See LexicalQueryExpression for details.
        :param str capacity: Filter results by capacity.  See NumericQueryExpression for details.
        :param int offset: Index of the first element to include in paginated results.<br> <b>'limit' must also be specified.</b>
        :param int limit: <p>Maximum number of elements to include in paginated results.<br> <b>'offset' must also be specified.<b>
        :param str sort_by: Specify the field priority order and direction for sorting.  See SortingOrderExpression for details. 
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: list[Extent]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_extents_with_http_info(cluster_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_extents_with_http_info(cluster_name, **kwargs)  # noqa: E501
            return data

    def get_extents_with_http_info(self, cluster_name, **kwargs):  # noqa: E501
        """Returns a list of Extent objects  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_extents_with_http_info(cluster_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: Filter results by name. See LexicalQueryExpression for details.
        :param str use: Filter results by use. See LexicalQueryExpression for details.
        :param str capacity: Filter results by capacity.  See NumericQueryExpression for details.
        :param int offset: Index of the first element to include in paginated results.<br> <b>'limit' must also be specified.</b>
        :param int limit: <p>Maximum number of elements to include in paginated results.<br> <b>'offset' must also be specified.<b>
        :param str sort_by: Specify the field priority order and direction for sorting.  See SortingOrderExpression for details. 
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: list[Extent]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'name', 'use', 'capacity', 'offset', 'limit', 'sort_by', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_extents" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `get_extents`")  # noqa: E501

        if 'offset' in params and params['offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `get_extents`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_extents`, must be a value less than or equal to `100`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_extents`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_name' in params:
            path_params['cluster_name'] = params['cluster_name']  # noqa: E501

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'use' in params:
            query_params.append(('use', params['use']))  # noqa: E501
        if 'capacity' in params:
            query_params.append(('capacity', params['capacity']))  # noqa: E501
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
            '/clusters/{cluster_name}/extents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Extent]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_extent(self, cluster_name, name, extent_patch_payload, **kwargs):  # noqa: E501
        """Update attributes on a Extent  # noqa: E501

        Settable attributes: 'name'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_extent(cluster_name, name, extent_patch_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :param list[JsonPatchOp] extent_patch_payload: (required)
        :return: Extent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_extent_with_http_info(cluster_name, name, extent_patch_payload, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_extent_with_http_info(cluster_name, name, extent_patch_payload, **kwargs)  # noqa: E501
            return data

    def patch_extent_with_http_info(self, cluster_name, name, extent_patch_payload, **kwargs):  # noqa: E501
        """Update attributes on a Extent  # noqa: E501

        Settable attributes: 'name'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_extent_with_http_info(cluster_name, name, extent_patch_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :param list[JsonPatchOp] extent_patch_payload: (required)
        :return: Extent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'name', 'extent_patch_payload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_extent" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `patch_extent`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `patch_extent`")  # noqa: E501
        # verify the required parameter 'extent_patch_payload' is set
        if ('extent_patch_payload' not in params or
                params['extent_patch_payload'] is None):
            raise ValueError("Missing the required parameter `extent_patch_payload` when calling `patch_extent`")  # noqa: E501

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
        if 'extent_patch_payload' in params:
            body_params = params['extent_patch_payload']
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{cluster_name}/extents/{name}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Extent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
