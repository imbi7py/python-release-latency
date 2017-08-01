from behave import when, then
from hamcrest import (assert_that, equal_to, instance_of,
                      has_entries, contains_inanyorder)

import requests

@when("I query the {collection_name} collection")
def query_api_collection(context, collection_name):
    collection_url = context.server_api_url + collection_name + "/"
    context._api_response = requests.get(collection_url)

@then("the reported HTTP status should be {expected_status:d}")
def check_reported_http_status(context, expected_status):
    assert_that(context._api_response.status_code, equal_to(expected_status))

@then("all given releases should be reported")
def check_reported_releases(context):
    data = context._api_response.json()["results"]
    assert_that(data, instance_of(list))
    for release in data: release.pop("url")
    expected = [has_entries(r) for r in context._given_releases]
    assert_that(len(data), equal_to(len(expected)))
    assert_that(data, contains_inanyorder(*expected))