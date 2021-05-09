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


class AggregateApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_aggregates(self, uri, group_by, **kwargs):  # noqa: E501
        """Groups the resources at the given URI by the values of the provided fields and returns aggregated computations for each group   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.get_aggregates(uri, group_by, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str uri: URI of collection to aggregate (required)
        :param str group_by: Comma-separated list of fields to aggregate on (required)
        :return: Aggregates
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_http_request'):
            return self.get_aggregates_with_http_info(uri, group_by, **kwargs)  # noqa: E501
        else:
            (data) = self.get_aggregates_with_http_info(uri, group_by, **kwargs)  # noqa: E501
            return data

    def get_aggregates_with_http_info(self, uri, group_by, **kwargs):  # noqa: E501
        """Groups the resources at the given URI by the values of the provided fields and returns aggregated computations for each group   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_http_request=True
        >>> thread = api.get_aggregates_with_http_info(uri, group_by, async_http_request=True)
        >>> result = thread.get()

        :param async_http_request bool
        :param str uri: URI of collection to aggregate (required)
        :param str group_by: Comma-separated list of fields to aggregate on (required)
        :return: Aggregates
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uri', 'group_by']  # noqa: E501
        all_params.append('async_http_request')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_aggregates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uri' is set
        if ('uri' not in params or
                params['uri'] is None):
            raise ValueError("Missing the required parameter `uri` when calling `get_aggregates`")  # noqa: E501
        # verify the required parameter 'group_by' is set
        if ('group_by' not in params or
                params['group_by'] is None):
            raise ValueError("Missing the required parameter `group_by` when calling `get_aggregates`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uri' in params:
            query_params.append(('uri', params['uri']))  # noqa: E501
        if 'group_by' in params:
            query_params.append(('group_by', params['group_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/aggregates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Aggregates',  # noqa: E501
            auth_settings=auth_settings,
            async_http_request=params.get('async_http_request'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
