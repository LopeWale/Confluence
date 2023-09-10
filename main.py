from confluenceAPIconnection import APIConnection
from database import DatabaseConnection

def main():
    # Create a database connection
    db = DatabaseConnection(
        host="localhost",  # replace with your host
        user="root",  # replace with your MySQL user
        password="root",  # replace with your MySQL password
        database="confluence_data"  # replace with your database
    )

    # Create an API connection using the database connection
    headers = {"Authorization": "Basic base64_encoded_username:password"}  # replace with your base64-encoded username and password
    api_connection = APIConnection(base_url="http://myhost:8080/confluence", headers=headers, db=db)  # replace with your base URL

    # Test API functions and data will be automatically stored in the database
    user_info = api_connection.get_user_info(username="jblogs")  # replace with your username
    print(user_info)

    user_groups = api_connection.get_user_groups(username="jblogs")  # replace with your username
    print(user_groups)

    content_info = api_connection.get_content_by_id(content_id="12345")  # replace with your content id
    print(content_info)

    search_results = api_connection.search_content(cql="title=\'test\'")  # replace with your CQL query
    print(search_results)

    blog_results = api_connection.get_blogs_by_space_key(space_key="TEST")  # replace with your space key
    print(blog_results)

if __name__ == "__main__":
    main()
