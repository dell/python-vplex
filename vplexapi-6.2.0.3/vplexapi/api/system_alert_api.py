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


class SystemAlertApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_system_alerts(self, **kwargs):  # noqa: E501
        """Returns the list of active system alerts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_system_alerts(async=True)
        >>> result = thread.get()

        :param async bool
        :param int offset: Index of the first element to include in paginated results.<br> <b>'limit' must also be specified.</b>
        :param int limit: <p>Maximum number of elements to include in paginated results.<br> <b>'offset' must also be specified.<b>
        :param str sort_by: Specify the field priority order and direction for sorting.  See SortingOrderExpression for details. 
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :param str state: Filter results by state. See LexicalQueryExpression for details.
        :param str severity: Filter results by severity. See LexicalQueryExpression for details.
        :param str scope: Filter results by scope. See LexicalQueryExpression for details.
        :param str message: Filter results by message. See LexicalQueryExpression for details.
        :param int id: Filter results by id.
        :return: list[SystemAlert]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_system_alerts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_system_alerts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_system_alerts_with_http_info(self, **kwargs):  # noqa: E501
        """Returns the list of active system alerts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_system_alerts_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int offset: Index of the first element to include in paginated results.<br> <b>'limit' must also be specified.</b>
        :param int limit: <p>Maximum number of elements to include in paginated results.<br> <b>'offset' must also be specified.<b>
        :param str sort_by: Specify the field priority order and direction for sorting.  See SortingOrderExpression for details. 
        :param str fields: Select which fields are included in the response. 'name' is always included. See FieldSelectionExpression for details. 
        :param str state: Filter results by state. See LexicalQueryExpression for details.
        :param str severity: Filter results by severity. See LexicalQueryExpression for details.
        :param str scope: Filter results by scope. See LexicalQueryExpression for details.
        :param str message: Filter results by message. See LexicalQueryExpression for details.
        :param int id: Filter results by id.
        :return: list[SystemAlert]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'sort_by', 'fields', 'state', 'severity', 'scope', 'message', 'id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_system_alerts" % key
                )
            params[key] = val
        del params['kwargs']

        if 'offset' in params and params['offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `get_system_alerts`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_system_alerts`, must be a value less than or equal to `100`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_system_alerts`, must be a value greater than or equal to `1`")  # noqa: E501
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
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'severity' in params:
            query_params.append(('severity', params['severity']))  # noqa: E501
        if 'scope' in params:
            query_params.append(('scope', params['scope']))  # noqa: E501
        if 'message' in params:
            query_params.append(('message', params['message']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/notification/system_alerts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemAlert]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)