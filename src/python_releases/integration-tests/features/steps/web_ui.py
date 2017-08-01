from behave import when, then
from hamcrest import (assert_that, equal_to, instance_of,
                      has_entries, contains_inanyorder)

import bs4
import splinter

@when("I visit the {link_text} page")
def visit_web_ui_page(context, link_text):
    context._browser = browser = splinter.Browser()
    context.resource_manager.enter_context(browser) # Ensure window is closed
    browser.visit(context.server_url)
    browser.find_link_by_text(link_text).first.click()

@then("the page title should be {expected_title}")
def check_page_title(context, expected_title):
    assert_that(context._browser.title, equal_to(expected_title))

@then("all given releases should be displayed")
def check_displayed_releases(context):
    parser = bs4.BeautifulSoup(context._browser.html, "lxml")
    tbody = parser.find_all("tbody")[0]
    fields = "implementation", "version", "release_date", "kind"
    data = [{key: cell.get_text()
                for key, cell in zip(fields, row.find_all("td"))}
                    for row in tbody.find_all("tr")]
    expected = [has_entries(r) for r in context._given_releases]
    assert_that(len(data), equal_to(len(expected)))
    assert_that(data, contains_inanyorder(expected))
