def connect_to_database():
    # Hard-coded database credentials (not recommended)
    db_username = "admin"
    db_password = "password123"
    db_host = "localhost"
    db_port = 5432
    db_name = "mydatabase"

    connection_string = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
    print("Connecting to database with connection string:", connection_string)
    # Code to connect to the database would go here

if __name__ == "__main__":
    connect_to_database()
