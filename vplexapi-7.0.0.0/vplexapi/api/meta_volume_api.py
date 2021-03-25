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


class MetaVolumeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_meta_volume(self, cluster_name, meta_volume_payload, **kwargs):  # noqa: E501
        """Create a new MetaVolume  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_meta_volume(cluster_name, meta_volume_payload, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_name: The name of the cluster (required)
        :param MetaVolumePayload meta_volume_payload: (required)
        :param str x_include_object: When passed as part of a POST request, controls whether the representation of the newly created object is included in the response. Defaults to 'true' which will include the object in the response. This header is useful because refreshing the newly created object is usually the slowest part of a POST operation. 
        :return: MetaVolume
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_meta_volume_with_http_info(cluster_name, meta_volume_payload, **kwargs)  # noqa: E501
        else:
            (data) = self.create_meta_volume_with_http_info(cluster_name, meta_volume_payload, **kwargs)  # noqa: E501
            return data

    def create_meta_volume_with_http_info(self, cluster_name, meta_volume_payload, **kwargs):  # noqa: E501
        """Create a new MetaVolume  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_meta_volume_with_http_info(cluster_name, meta_volume_payload, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_name: The name of the cluster (required)
        :param MetaVolumePayload meta_volume_payload: (required)
        :param str x_include_object: When passed as part of a POST request, controls whether the representation of the newly created object is included in the response. Defaults to 'true' which will include the object in the response. This header is useful because refreshing the newly created object is usually the slowest part of a POST operation. 
        :return: MetaVolume
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'meta_volume_payload', 'x_include_object']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_meta_volume" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `create_meta_volume`")  # noqa: E501
        # verify the required parameter 'meta_volume_payload' is set
        if ('meta_volume_payload' not in params or
                params['meta_volume_payload'] is None):
            raise ValueError("Missing the required parameter `meta_volume_payload` when calling `create_meta_volume`")  # noqa: E501

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
        if 'meta_volume_payload' in params:
            body_params = params['meta_volume_payload']
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{cluster_name}/meta_volumes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MetaVolume',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_meta_volume(self, cluster_name, name, **kwargs):  # noqa: E501
        """Deletes a single MetaVolume  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_meta_volume(cluster_name, name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_meta_volume_with_http_info(cluster_name, name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_meta_volume_with_http_info(cluster_name, name, **kwargs)  # noqa: E501
            return data

    def delete_meta_volume_with_http_info(self, cluster_name, name, **kwargs):  # noqa: E501
        """Deletes a single MetaVolume  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_meta_volume_with_http_info(cluster_name, name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_meta_volume" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `delete_meta_volume`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete_meta_volume`")  # noqa: E501

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
            '/clusters/{cluster_name}/meta_volumes/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_meta_volume(self, cluster_name, name, **kwargs):  # noqa: E501
        """Returns a single MetaVolume by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_meta_volume(cluster_name, name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: MetaVolume
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_meta_volume_with_http_info(cluster_name, name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_meta_volume_with_http_info(cluster_name, name, **kwargs)  # noqa: E501
            return data

    def get_meta_volume_with_http_info(self, cluster_name, name, **kwargs):  # noqa: E501
        """Returns a single MetaVolume by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_meta_volume_with_http_info(cluster_name, name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: MetaVolume
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'name', 'fields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_meta_volume" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `get_meta_volume`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_meta_volume`")  # noqa: E501

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
            '/clusters/{cluster_name}/meta_volumes/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MetaVolume',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_meta_volumes(self, cluster_name, **kwargs):  # noqa: E501
        """Returns a list of MetaVolume objects. Supports paging  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_meta_volumes(cluster_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: Filter results by name. See LexicalQueryExpression for details.
        :param str health_state: Filter results by health_state. See LexicalQueryExpression for details.
        :param str operational_status: Filter results by operational_status. See LexicalQueryExpression for details.
        :param int offset: Index of the first element to include in paginated results.<br> <b>'limit' must also be specified.</b>
        :param int limit: <p>Maximum number of elements to include in paginated results.<br> <b>'offset' must also be specified.<b>
        :param str sort_by: Specify the field priority order and direction for sorting.  See SortingOrderExpression for details. 
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: list[MetaVolume]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_meta_volumes_with_http_info(cluster_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_meta_volumes_with_http_info(cluster_name, **kwargs)  # noqa: E501
            return data

    def get_meta_volumes_with_http_info(self, cluster_name, **kwargs):  # noqa: E501
        """Returns a list of MetaVolume objects. Supports paging  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_meta_volumes_with_http_info(cluster_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: Filter results by name. See LexicalQueryExpression for details.
        :param str health_state: Filter results by health_state. See LexicalQueryExpression for details.
        :param str operational_status: Filter results by operational_status. See LexicalQueryExpression for details.
        :param int offset: Index of the first element to include in paginated results.<br> <b>'limit' must also be specified.</b>
        :param int limit: <p>Maximum number of elements to include in paginated results.<br> <b>'offset' must also be specified.<b>
        :param str sort_by: Specify the field priority order and direction for sorting.  See SortingOrderExpression for details. 
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: list[MetaVolume]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'name', 'health_state', 'operational_status', 'offset', 'limit', 'sort_by', 'fields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_meta_volumes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `get_meta_volumes`")  # noqa: E501

        if 'offset' in params and params['offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `get_meta_volumes`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_meta_volumes`, must be a value less than or equal to `100`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_meta_volumes`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_name' in params:
            path_params['cluster_name'] = params['cluster_name']  # noqa: E501

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'health_state' in params:
            query_params.append(('health_state', params['health_state']))  # noqa: E501
        if 'operational_status' in params:
            query_params.append(('operational_status', params['operational_status']))  # noqa: E501
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
            '/clusters/{cluster_name}/meta_volumes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MetaVolume]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_meta_volume(self, cluster_name, name, meta_volume_patch_payload, **kwargs):  # noqa: E501
        """Update attributes on a MetaVolume  # noqa: E501

        Settable attributes: 'active' . NOTE: only true value is allowed      # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.patch_meta_volume(cluster_name, name, meta_volume_patch_payload, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :param list[JsonPatchOp] meta_volume_patch_payload: (required)
        :return: MetaVolume
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.patch_meta_volume_with_http_info(cluster_name, name, meta_volume_patch_payload, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_meta_volume_with_http_info(cluster_name, name, meta_volume_patch_payload, **kwargs)  # noqa: E501
            return data

    def patch_meta_volume_with_http_info(self, cluster_name, name, meta_volume_patch_payload, **kwargs):  # noqa: E501
        """Update attributes on a MetaVolume  # noqa: E501

        Settable attributes: 'active' . NOTE: only true value is allowed      # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.patch_meta_volume_with_http_info(cluster_name, name, meta_volume_patch_payload, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_name: The name of the cluster (required)
        :param str name: The name of a specific instance of the resource (required)
        :param list[JsonPatchOp] meta_volume_patch_payload: (required)
        :return: MetaVolume
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name', 'name', 'meta_volume_patch_payload']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_meta_volume" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `patch_meta_volume`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `patch_meta_volume`")  # noqa: E501
        # verify the required parameter 'meta_volume_patch_payload' is set
        if ('meta_volume_patch_payload' not in params or
                params['meta_volume_patch_payload'] is None):
            raise ValueError("Missing the required parameter `meta_volume_patch_payload` when calling `patch_meta_volume`")  # noqa: E501

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
        if 'meta_volume_patch_payload' in params:
            body_params = params['meta_volume_patch_payload']
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/clusters/{cluster_name}/meta_volumes/{name}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MetaVolume',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
