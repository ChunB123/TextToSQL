import unittest
from flask_app.models.chatgpt import text_to_sql_gpt3
from flask_app.service.chatgpt_service import text_to_sql, sql_is_query_or_not

class Test_chatgpt(unittest.TestCase):
    def test_text_to_sql_gpt3(self):
        test_prompt = "What date had the highest trading volume, and what was the closing price on that day?"

        result = text_to_sql_gpt3(test_prompt)

        self.assertIn("SELECT", result)

class Test_chatgpt_service(unittest.TestCase):
    def test_text_to_sql(self):
        test_prompt = "What date had the highest trading volume, and what was the closing price on that day?"

        result = text_to_sql(test_prompt)

        self.assertIn("SELECT", result)

    def test_text_to_sql_nonexist_table(self):
        test_prompt = "How many birds are there from the table birds_examples"

        result = text_to_sql(test_prompt)
        print(result)

        self.assertIn("SELECT", result)

    def test_sql_is_query_select(self):
        test_SQL = "SELECT * FROM tsla_stock_data LIMIT 1"

        result = sql_is_query_or_not(test_SQL)
        print(result)

        self.assertEquals(result, True)

    def test_sql_is_query_creat_table(self):
        test_SQL = "CREATE TABLE IF NOT EXISTS tsla_stock_data (date DATE PRIMARY KEY);"

        result = sql_is_query_or_not(test_SQL)
        print(result)
        self.assertEquals(result, False)

if __name__ == '__main__':
    unittest.main()

"""
# Test api server later
    def test_text_to_sql_modify_db(self):
        test_prompt = "Create birds_examples table"

        result = text_to_sql(test_prompt)
        print(result)

        self.assertIn("NO", result)
"""