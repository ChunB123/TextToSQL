from flask import jsonify
import os


def find_env_path():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    root_dir = current_dir
    while root_dir != os.path.dirname(root_dir):  # Check until the root of the file system is reached
        if os.path.isfile(os.path.join(root_dir, '.env')):
            return os.path.join(root_dir, '.env')
        root_dir = os.path.dirname(root_dir)
    raise FileNotFoundError(".env file not found")


def respond(success=True, sql_query=None, result=None, internal_error=None, message=None, status_code=200):
    response = {
        "status": "success" if success else "error",
        "sql_query": sql_query,
        "result": result,
        "internal_error": internal_error,
        "message": message
    }
    # Remove None values to keep the response clean
    response = {key: value for key, value in response.items() if value is not None}
    return jsonify(response), status_code
