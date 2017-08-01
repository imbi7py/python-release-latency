Feature: Releases Page

  @wip
  Scenario: Displaying all releases
    Given the following Python releases:
        | implementation | version | python_version | release_date |
        | CPython        | 3.6.0   |                | 2016-12-23   |
        | CPython        | 3.6.2   |                | 2017-07-17   |
        | PyPy           | 5.8     | 2.7.13         | 2017-06-09   |
        | PyPy3          | 5.8     | 3.5.4          | 2017-06-09   |
      And a running instance of the backend service

    When I visit the Upstream Releases page
    Then the page title should be Python Upstream Releases
     And all given releases should be displayed
