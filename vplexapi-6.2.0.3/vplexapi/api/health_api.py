# coding: utf-8

"""
    VPlex REST API

    A defnition for the next-gen VPlex API  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vplexapi.api_client import ApiClient


class HealthApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_local_com_health(self, cluster_name, **kwargs):  # noqa: E501
        """Return local-COM health information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_local_com_health(cluster_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_name: The name of the cluster (required)
        :return: LocalComHealth
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_local_com_health_with_http_info(cluster_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_local_com_health_with_http_info(cluster_name, **kwargs)  # noqa: E501
            return data

    def get_local_com_health_with_http_info(self, cluster_name, **kwargs):  # noqa: E501
        """Return local-COM health information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_local_com_health_with_http_info(cluster_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_name: The name of the cluster (required)
        :return: LocalComHealth
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_local_com_health" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_name' is set
        if ('cluster_name' not in params or
                params['cluster_name'] is None):
            raise ValueError("Missing the required parameter `cluster_name` when calling `get_local_com_health`")  # noqa: E501

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
            '/clusters/{cluster_name}/health/local_com', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LocalComHealth',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_wan_com_health(self, **kwargs):  # noqa: E501
        """Return WAN-COM health information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_wan_com_health(async=True)
        >>> result = thread.get()

        :param async bool
        :return: WanComHealth
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_wan_com_health_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_wan_com_health_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_wan_com_health_with_http_info(self, **kwargs):  # noqa: E501
        """Return WAN-COM health information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_wan_com_health_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: WanComHealth
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wan_com_health" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/health/wan_com', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WanComHealth',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
