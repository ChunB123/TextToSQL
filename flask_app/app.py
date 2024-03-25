from flask import Flask, request
import psycopg2
from flask_app.service.chatgpt_service import text_to_sql, sql_is_query_or_not
from flask_app.db_config.extensions import postgresDB
from flask_app.utils import respond
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
postgresDB.init_app(app)


@app.route('/query', methods=['POST'])
def run_query():
    data = request.json
    text_query = data.get('query')

    if not text_query:
        return respond(success=False, message="No text query provided")

    try:
        sql_query = text_to_sql(text_query)
        if not sql_is_query_or_not(sql_query):
            return respond(success=False, sql_query=sql_query, message="Query is not a SELECT SQL")

        with postgresDB.get_cursor() as cursor:
            cursor.execute(sql_query)
            if cursor.description:
                result = cursor.fetchall()
                return respond(sql_query=sql_query, result=result)
            else:
                return respond(sql_query=sql_query, message="Query executed successfully, but no output to show.")
    except psycopg2.DatabaseError as e:
        return respond(success=False, sql_query=sql_query,
                       internal_error=str(e),
                       message="psycopg2.DatabaseError",
                       status_code=500)
    except Exception as e:
        return respond(success=False,
                       internal_error=str(e),
                       message="Unexpected error occurred inside the controller",
                       status_code=500)


@app.errorhandler(Exception)
def handle_exception(e):
    """Handle all application errors."""
    return respond(success=False,
                   internal_error=str(e),
                   message="Unexpected error", status_code=500)
