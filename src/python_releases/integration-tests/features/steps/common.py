from behave import given

import csv
import tempfile

@given("the following Python releases")
def add_python_releases(context):
    given_releases = []
    # For now, "kind" is hardcoded to "full"
    with tempfile.NamedTemporaryFile("w") as temp_csv:
        table = context.table
        headings = table.headings + ["kind"]
        release_csv = csv.writer(temp_csv)
        release_csv.writerow(headings)
        for row in table.rows:
            release = list(row) + ["full"]
            release_csv.writerow(release)
            given_releases.append(dict(zip(headings, release)))
        temp_csv.flush()
        context.run_script("load_releases", temp_csv.name)
    # API doesn't report python_version yet
    for release in given_releases:
        release.pop("python_version")
    context._given_releases = given_releases

@given("a running instance of the backend service")
def start_backend_service(context):
    context.run_service(context)
