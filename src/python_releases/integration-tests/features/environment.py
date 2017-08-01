import contextlib
import pathlib
import requests
import subprocess
import sys

_APP_DIR = pathlib.Path(__file__).parent.parent.parent

def before_scenario(context, scenario):
    # Allow steps to register resources for cleanup after the scenario
    context.resource_manager = resource_manager = contextlib.ExitStack()

    # Clear the testing database
    _flush_db = [sys.executable, "manage.py", "flush", "--no-input"]
    subprocess.run(_flush_db, cwd=_APP_DIR,
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)

    # Provide a helper to run scripts
    context.run_script = run_script

    # Provide a helper to run the backend service
    context.run_service = run_service

def after_scenario(context, scenario):
    context.resource_manager.close()

#################################
# Context helper implementations
#################################

def run_script(script, *args, **kwds):
    """Run a utility script in the Django application context"""
    cmd = [sys.executable, "manage.py", "runscript", script]
    if args:
        cmd.append("--script-args")
        cmd.extend(args)
    print("Running", cmd)
    return subprocess.run(cmd, cwd=_APP_DIR, **kwds,
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)

def run_service(context):
    """Start the backend service in a separate process"""
    context.server_url = server_url = "http://localhost:8000/"
    context.server_api_url = server_api_url = server_url + "api/"
    _run_server = [sys.executable, "manage.py", "runserver"]
    server_process = subprocess.Popen(_run_server, cwd=_APP_DIR,
                                      stdout=subprocess.DEVNULL,
                                      stderr=subprocess.DEVNULL)
    response = None
    while response is None:
        try:
            response = requests.get(server_api_url)
        except requests.exceptions.ConnectionError:
            # TODO: Set a time limit here
            pass

    # And is restarted between scenarios
    context.resource_manager.enter_context(server_process)
    context.resource_manager.callback(server_process.terminate)
    return server_process
