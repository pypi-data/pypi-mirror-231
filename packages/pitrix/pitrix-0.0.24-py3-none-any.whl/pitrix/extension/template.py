#!/usr/bin/python3
# -*- coding: utf-8 -*-


api_template = """
{{tag}}
{{emoji_api}} <API>: {{caller_name}} {{doc}}
{{emoji_req}} <Request>
     URL: {{url}}
{% if method -%}
{% raw %}     Method: {%endraw%}{{method}}
{% endif -%}
{% if headers -%}
{% raw %}     Headers: {%endraw%}{{headers}}
{% endif -%}
{% if request_params -%}
{% raw %}     Request Params: {%endraw%}{{request_params}}
{% endif -%}
{% if request_data -%}
{% raw %}     Request Data: {%endraw%}{{request_data}}
{% endif -%}
{% if request_json -%}
{% raw %}     Request Json: {%endraw%}{{request_json}}
{% endif -%}
{{emoji_rep}} <Response>
{% if status_code -%}
{% raw %}     Status Code: {%endraw%}{{status_code}}
{% endif -%}
{% raw %}     Response Body: {%endraw%}{{response_body}}
{% if elapsed -%}
    {% raw %}     Elapsed: {%endraw%}{{elapsed}}s
{% endif -%}
{{tag}}
"""


categories_json = [
        {
            "name": "忽略的测试",
            "matchedStatuses": ["skipped"]
        },
        {
            "name": "基础设施问题",
            "matchedStatuses": ["broken", "failed"],
            "messageRegex": ".*bye-bye.*"
        },
        {
            "name": "过期的测试",
            "matchedStatuses": ["broken"],
            "traceRegex": ".*FileNotFoundException.*"
        },
        {
            "name": "产品缺陷",
            "matchedStatuses": ["failed"]
        },
        {
            "name": "测试缺陷",
            "matchedStatuses": ["broken"]
        }
    ]