from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from urllib.parse import urlparse
import os

app = Flask(__name__)

# Parse the database URL from the environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost/postgres")
url = urlparse(DATABASE_URL)

db_config = {
    "dbname": url.path[1:],
    "user": url.username,
    "password": url.password,
    "host": url.hostname,
    "port": url.port
}

def get_db_connection():
    conn = psycopg2.connect(**db_config)
    return conn


@app.route('/query', methods=['POST'])
def run_query():
    data = request.json
    sql_query = data.get('query')

    if not sql_query:
        return jsonify({"error": "No SQL query provided"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(sql_query)
        if cursor.description:  # If there is something to fetch
            result = cursor.fetchall()
            conn.close()
            return jsonify(result), 200
        else:  # Successful query but nothing to fetch (e.g., INSERT/UPDATE)
            conn.commit()
            conn.close()
            return jsonify({"success": "Query executed successfully, but no output to show."}), 200
    except (Exception, psycopg2.DatabaseError) as error:
        return jsonify({"error": "Failed to execute query", "sql_query": sql_query, "database_error": str(error)}), 400


if __name__ == '__main__':
    app.run(debug=True)