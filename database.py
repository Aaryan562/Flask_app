import psycopg2

def get_database_connection():
    conn = psycopg2.connect(database="flask_db",  
                            user="postgres", 
                            password="1234",  
                            host="localhost", port="5433")
    return conn

