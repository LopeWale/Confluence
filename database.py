import mysql.connector
import json

class DatabaseConnection:
    def __init__(self, host, user, password, database):
        try:
            self.db = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.db.cursor()
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def create_tables(self):
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS user_info (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255),
                    data JSON
                )
                """
            )

            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS user_groups (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT,
                    group_name VARCHAR(255),
                    FOREIGN KEY(user_id) REFERENCES user_info(id)
                )
                """
            )

            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS content (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    content_id VARCHAR(255),
                    data JSON
                )
                """
            )

            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS content_watchers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    content_id INT,
                    user_id INT,
                    FOREIGN KEY(content_id) REFERENCES content(id),
                    FOREIGN KEY(user_id) REFERENCES user_info(id)
                )
                """
            )

            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS blogs (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    blog_id VARCHAR(255),
                    data JSON
                )
                """
            )
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def insert_user_info(self, data):
        try:
            query = "INSERT INTO user_info (username, data) VALUES (%s, %s)"
            values = (data["username"], json.dumps(data))
            self.cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def insert_user_groups(self, user_id, data):
        try:
            query = "INSERT INTO user_groups (user_id, group_name) VALUES (%s, %s)"
            for group in data:
                values = (user_id, group["name"])
                self.cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def insert_content(self, data):
        try:
            query = "INSERT INTO content (content_id, data) VALUES (%s, %s)"
            values = (data["id"], json.dumps(data))
            self.cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def insert_content_watchers(self, content_id, user_id):
        try:
            query = "INSERT INTO content_watchers (content_id, user_id) VALUES (%s, %s)"
            values = (content_id, user_id)
            self.cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def fetch_user_info(self):
        try:
            query = "SELECT * FROM user_info"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def fetch_user_groups(self):
        try:
            query = "SELECT * FROM user_groups"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def fetch_content(self):
        try:
            query = "SELECT * FROM content"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def fetch_content_watchers(self):
        try:
            query = "SELECT * FROM content_watchers"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def insert_blog(self, data):
        try:
            query = "INSERT INTO blogs (blog_id, data) VALUES (%s, %s)"
            values = (data["id"], json.dumps(data))
            self.cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def fetch_blogs(self):
        try:
            query = "SELECT * FROM blogs"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print("Error occurred:", err)
