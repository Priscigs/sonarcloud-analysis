import os
import sqlite3

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

def get_user_input():
    user_input = input("Enter some text: ")
    return user_input

def process_data(data):
    processed_data = data.lower()
    return processed_data

def insecure_sql_query(user_input):
    # Insecure SQL query (SQL Injection vulnerability)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def main():
    file_path = "example.txt"
    hardcoded_password = "P@ssw0rd"  # Hardcoded credentials
    api_key = "12345-ABCDE"  # Another hardcoded secret
    
    # Reading from a file
    data = read_file(file_path)
    if data is None:
        return
    
    # Processing data
    processed_data = process_data(data)
    print(f"Processed Data: {processed_data}")
    
    # Getting user input and writing to a file
    user_input = get_user_input()
    
    # Unrestricted eval usage
    eval(user_input)  # This is dangerous and should be avoided
    
    # Writing to a potentially insecure temporary file
    temp_file_path = "/tmp/tempfile.txt"
    with open(temp_file_path, 'w') as temp_file:
        temp_file.write("This is a temporary file.")
    
    # Insecure SQL query
    results = insecure_sql_query(user_input)
    print(f"SQL Query Results: {results}")
    
    # Command injection
    os.system(user_input)  # Using user input in system command
    
    # Logging sensitive information
    print(f"Logging sensitive data: {hardcoded_password}, {api_key}")
    
    try:
        write_file(file_path, user_input)
    except Exception as e:
        print("An error occurred.")  # Generic exception handling
    
if __name__ == "__main__":
    main()
