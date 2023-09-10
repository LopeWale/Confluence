import unittest
import logging
from confluenceAPIconnection import APIConnection
from database import DatabaseConnection

logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestAPIConnection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DatabaseConnection("localhost", "root", "root", "confluence_data")
        cls.api_connection = APIConnection("http://myhost:8080/confluence", cls.db, {"Authorization": "Basic base64_encoded_username:password"})
        
    def test_get_user_info(self):
        logging.info('Starting test_get_user_info')
        user_info = self.api_connection.get_user_info("jblogs")
        self.assertIsInstance(user_info, dict)
        self.assertIn("username", user_info)
        logging.info('Finished test_get_user_info')

    def test_get_user_groups(self):
        logging.info('Starting test_get_user_groups')
        user_groups = self.api_connection.get_user_groups("jblogs")
        self.assertIsInstance(user_groups, list)
        logging.info('Finished test_get_user_groups')

    def test_get_content_by_id(self):
        logging.info('Starting test_get_content_by_id')
        content_info = self.api_connection.get_content_by_id("12345")
        self.assertIsInstance(content_info, dict)
        self.assertIn("id", content_info)
        logging.info('Finished test_get_content_by_id')

    def test_search_content(self):
        logging.info('Starting test_search_content')
        search_results = self.api_connection.search_content("title='test'")
        self.assertIsInstance(search_results, dict)
        self.assertIn("results", search_results)
        logging.info('Finished test_search_content')

    def test_get_blogs_by_space_key(self):
        logging.info('Starting test_get_blogs_by_space_key')
        blog_data = self.api_connection.get_blogs_by_space_key("TEST")
        self.assertIsInstance(blog_data, dict)
        self.assertIn("results", blog_data)
        logging.info('Finished test_get_blogs_by_space_key')

class TestDatabaseConnection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DatabaseConnection("localhost", "root", "root", "confluence_data")

    def test_insert_user_info(self):
        logging.info('Starting test_insert_user_info')
        user_info = {"username": "jblogs", "email": "jblogs@example.com"}
        self.db.insert_user_info(user_info)
        # Here you would add code to fetch the inserted data from the database and check that it was inserted correctly
        logging.info('Finished test_insert_user_info')

    # Add more tests here as needed

if __name__ == "__main__":
    unittest.main()
