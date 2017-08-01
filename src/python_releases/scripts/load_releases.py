import csv
import datetime
import pathlib

from release_latency.models import PythonImplementation, PythonRelease

_REPO_DIR = pathlib.Path(__file__).parent.parent.parent.parent
_DATA_DIR = _REPO_DIR / "data"
_RELEASES_CSV_PATH = _DATA_DIR / "releases.csv"

def _load_releases_from_csv(csv_path):
    with open(csv_path) as releases_csv:
        releases = csv.DictReader(releases_csv)
        for record in releases:
            impl_name = record["implementation"]
            impl, is_new = PythonImplementation.objects.get_or_create(name=impl_name)
            if is_new:
                print(f"Added implementation: {impl_name}")
            record["implementation"] = impl
            release, is_new = PythonRelease.objects.get_or_create(**record)
            if is_new:
                print(f"Added {impl_name} release {release.version} on {release.release_date}")

# Run as "python manage.py runscript load_releases [csv_file]"
def run(*args):
    if not args:
        args = (_RELEASES_CSV_PATH,)
    for csv_path in args:
        try:
            _load_releases_from_csv(csv_path)
        except:
            import traceback
            traceback.print_exc()
            raise