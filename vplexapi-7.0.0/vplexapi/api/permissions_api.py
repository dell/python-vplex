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


class PermissionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_permissions(self, **kwargs):  # noqa: E501
        """Returns the Role-Based Authentication configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_permissions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Index of the first element to include in paginated results.<br> <b>'limit' must also be specified.</b>
        :param int limit: <p>Maximum number of elements to include in paginated results.<br> <b>'offset' must also be specified.<b>
        :param str sort_by: Specify the field priority order and direction for sorting.  See SortingOrderExpression for details. 
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: list[Permission]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_permissions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_permissions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_permissions_with_http_info(self, **kwargs):  # noqa: E501
        """Returns the Role-Based Authentication configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_permissions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Index of the first element to include in paginated results.<br> <b>'limit' must also be specified.</b>
        :param int limit: <p>Maximum number of elements to include in paginated results.<br> <b>'offset' must also be specified.<b>
        :param str sort_by: Specify the field priority order and direction for sorting.  See SortingOrderExpression for details. 
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: list[Permission]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'sort_by', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_permissions" % key
                )
            params[key] = val
        del params['kwargs']

        if 'offset' in params and params['offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `get_permissions`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_permissions`, must be a value less than or equal to `100`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_permissions`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

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
            '/permissions/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Permission]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_role(self, rbac_role, **kwargs):  # noqa: E501
        """Return the Role-Based Authentication configuration for one role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role(rbac_role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rbac_role: The name of the role (required)
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: Permission
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_role_with_http_info(rbac_role, **kwargs)  # noqa: E501
        else:
            (data) = self.get_role_with_http_info(rbac_role, **kwargs)  # noqa: E501
            return data

    def get_role_with_http_info(self, rbac_role, **kwargs):  # noqa: E501
        """Return the Role-Based Authentication configuration for one role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_with_http_info(rbac_role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rbac_role: The name of the role (required)
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :return: Permission
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rbac_role', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rbac_role' is set
        if ('rbac_role' not in params or
                params['rbac_role'] is None):
            raise ValueError("Missing the required parameter `rbac_role` when calling `get_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rbac_role' in params:
            path_params['rbac_role'] = params['rbac_role']  # noqa: E501

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
            '/permissions/{rbac_role}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Permission',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_permissions(self, rbac_role, permission_patch_payload, **kwargs):  # noqa: E501
        """Modify the Role-Based Authentication configuration for this role  # noqa: E501

        To add/remove a path pattern rule, use an add/remove patch with path \"/\" and value \"/path/pattern\".  A new path pattern rule is created with all verbs forbidden.  To permit/forbid a verb at an existing path pattern, use an add/remove patch with path \"/path/pattern\" and value \"verb\".   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_permissions(rbac_role, permission_patch_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rbac_role: The name of the role (required)
        :param list[JsonPatchOp] permission_patch_payload: (required)
        :return: Permission
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_permissions_with_http_info(rbac_role, permission_patch_payload, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_permissions_with_http_info(rbac_role, permission_patch_payload, **kwargs)  # noqa: E501
            return data

    def patch_permissions_with_http_info(self, rbac_role, permission_patch_payload, **kwargs):  # noqa: E501
        """Modify the Role-Based Authentication configuration for this role  # noqa: E501

        To add/remove a path pattern rule, use an add/remove patch with path \"/\" and value \"/path/pattern\".  A new path pattern rule is created with all verbs forbidden.  To permit/forbid a verb at an existing path pattern, use an add/remove patch with path \"/path/pattern\" and value \"verb\".   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_permissions_with_http_info(rbac_role, permission_patch_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rbac_role: The name of the role (required)
        :param list[JsonPatchOp] permission_patch_payload: (required)
        :return: Permission
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rbac_role', 'permission_patch_payload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_permissions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rbac_role' is set
        if ('rbac_role' not in params or
                params['rbac_role'] is None):
            raise ValueError("Missing the required parameter `rbac_role` when calling `patch_permissions`")  # noqa: E501
        # verify the required parameter 'permission_patch_payload' is set
        if ('permission_patch_payload' not in params or
                params['permission_patch_payload'] is None):
            raise ValueError("Missing the required parameter `permission_patch_payload` when calling `patch_permissions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rbac_role' in params:
            path_params['rbac_role'] = params['rbac_role']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'permission_patch_payload' in params:
            body_params = params['permission_patch_payload']
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/permissions/{rbac_role}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Permission',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
