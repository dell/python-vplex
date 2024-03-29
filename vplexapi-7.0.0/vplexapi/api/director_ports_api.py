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


class DirectorPortsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_director_port(self, director_name, name, **kwargs):  # noqa: E501
        """Returns a single DirectorPort object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_director_port(director_name, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str director_name: The name of the director (required)
        :param str name: The name of a specific instance of the resource (required)
        :return: DirectorPort
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_director_port_with_http_info(director_name, name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_director_port_with_http_info(director_name, name, **kwargs)  # noqa: E501
            return data

    def get_director_port_with_http_info(self, director_name, name, **kwargs):  # noqa: E501
        """Returns a single DirectorPort object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_director_port_with_http_info(director_name, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str director_name: The name of the director (required)
        :param str name: The name of a specific instance of the resource (required)
        :return: DirectorPort
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['director_name', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_director_port" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'director_name' is set
        if ('director_name' not in params or
                params['director_name'] is None):
            raise ValueError("Missing the required parameter `director_name` when calling `get_director_port`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_director_port`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'director_name' in params:
            path_params['director_name'] = params['director_name']  # noqa: E501
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
            '/directors/{director_name}/ports/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectorPort',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_director_ports(self, director_name, **kwargs):  # noqa: E501
        """Returns a list of director ports  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_director_ports(director_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str director_name: The name of the director (required)
        :return: list[DirectorPort]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_director_ports_with_http_info(director_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_director_ports_with_http_info(director_name, **kwargs)  # noqa: E501
            return data

    def get_director_ports_with_http_info(self, director_name, **kwargs):  # noqa: E501
        """Returns a list of director ports  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_director_ports_with_http_info(director_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str director_name: The name of the director (required)
        :return: list[DirectorPort]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['director_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_director_ports" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'director_name' is set
        if ('director_name' not in params or
                params['director_name'] is None):
            raise ValueError("Missing the required parameter `director_name` when calling `get_director_ports`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'director_name' in params:
            path_params['director_name'] = params['director_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/directors/{director_name}/ports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DirectorPort]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_director_port(self, director_name, name, port_patch_payload, **kwargs):  # noqa: E501
        """Update attributes on a DirectorPort  # noqa: E501

        Settable attribute is 'enabled'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_director_port(director_name, name, port_patch_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str director_name: The name of the director (required)
        :param str name: The name of a specific instance of the resource (required)
        :param list[JsonPatchOp] port_patch_payload: (required)
        :return: DirectorPort
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_director_port_with_http_info(director_name, name, port_patch_payload, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_director_port_with_http_info(director_name, name, port_patch_payload, **kwargs)  # noqa: E501
            return data

    def patch_director_port_with_http_info(self, director_name, name, port_patch_payload, **kwargs):  # noqa: E501
        """Update attributes on a DirectorPort  # noqa: E501

        Settable attribute is 'enabled'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_director_port_with_http_info(director_name, name, port_patch_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str director_name: The name of the director (required)
        :param str name: The name of a specific instance of the resource (required)
        :param list[JsonPatchOp] port_patch_payload: (required)
        :return: DirectorPort
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['director_name', 'name', 'port_patch_payload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_director_port" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'director_name' is set
        if ('director_name' not in params or
                params['director_name'] is None):
            raise ValueError("Missing the required parameter `director_name` when calling `patch_director_port`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `patch_director_port`")  # noqa: E501
        # verify the required parameter 'port_patch_payload' is set
        if ('port_patch_payload' not in params or
                params['port_patch_payload'] is None):
            raise ValueError("Missing the required parameter `port_patch_payload` when calling `patch_director_port`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'director_name' in params:
            path_params['director_name'] = params['director_name']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'port_patch_payload' in params:
            body_params = params['port_patch_payload']
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/directors/{director_name}/ports/{name}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectorPort',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
