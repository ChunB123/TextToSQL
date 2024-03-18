from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_app.service.chatgpt_service import text_to_sql, sql_is_query_or_not
from flask_app.db_config.extensions import postgresDB


app = Flask(__name__)
postgresDB.init_app(app)


@app.route('/query', methods=['POST'])
def run_query():
    data = request.json
    text_query = data.get('query')

    if not text_query:
        return jsonify({"error": "No text query provided"}), 400

    try:
        # Generate and check the SQL with models
        sql_query = text_to_sql(text_query)
        if not sql_is_query_or_not(sql_query):
            return jsonify({"error": "Query is not a SELECT SQL", "sql_query": sql_query}), 400

        with postgresDB.get_cursor() as cursor:
            cursor.execute(sql_query)
            if cursor.description:
                result = cursor.fetchall()
                return jsonify(result), 200
            else:  # Successful query but nothing to fetch (e.g., INSERT/UPDATE)
                return jsonify({"success": "Query executed successfully, but no output to show."}), 200
    except psycopg2.DatabaseError as error:
        return jsonify({"error": "Failed to execute query", "sql_query": sql_query, "database_error": str(error)}), 400
    except Exception as e:  # This will capture any other exceptions not caught by the previous clause
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.errorhandler(Exception)
def handle_exception(error):
    """Handle all application errors."""
    response = {"error": "An unexpected error occurred", "details": str(error)}
    return jsonify(response), 500