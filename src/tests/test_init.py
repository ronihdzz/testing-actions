from unittest import TestCase
from main import create_connection, execute_query
from settings import settings

class TestBooksAPI(TestCase):

    def test_assert_true(self):
        self.assertTrue(True)

    def test_posgresql_connection(self):
        connection = create_connection(settings.POSTGRESQL_URL)
        if connection:
            execute_query(connection, "SELECT version();")
            connection.dispose()

    def test_equal_strings(self):
        self.assertEqual("Hello", "Hello")
    