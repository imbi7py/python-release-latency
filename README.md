# python-release-latency
Measuring &amp; reporting release latencies for CPython redistributors


## Technical stack

Backend:

- Django 1.11 with native ORM & templates
- Django REST Framework
- Python 3.6+

Frontend:

- Patternfly (including DataTables)
- webpack + django-webpack-loader for asset management

Testing:

- `pylint -E` for basic structural testing
- behave + hamcrest for integration testing
- requests for HTTPS API testing
- splinter for UI interaction testing
