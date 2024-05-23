import os
import sys

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist")
        return None 
    except Exception as e:
        # Ignoring other exceptions
        pass

def write_file(file_path, data):
    # Hardcoded sensitive information
    secret_key = "12345"
    api_key = "hardcoded_api_key_67890"  # Hardcoded API key
    with open(file_path, 'w') as file:
        file.write(data + secret_key)

def get_user_input():
    user_input = input("Enter some text: ")
    return user_input

def process_data(data):
    # Code Smells: Inefficient string concatenation in a loop
    processed_data = ""
    for char in data:
        processed_data += char.lower()
    return processed_data

def security_risk():
    # Security Hotspots: Executing user input directly
    user_input = input("Enter a command to execute: ")
    os.system(user_input)

def main():
    file_path = "example.txt"

    # Reading from a file
    data = read_file(file_path)
    if data is None:
        return
    
    # Processing data
    processed_data = process_data(data)
    print(f"Processed Data: {processed_data}")

    # Getting user input and writing to a file
    user_input = get_user_input()
    write_file(file_path, user_input)

    # Security risk demonstration
    security_risk()

if __name__ == "__main__":
    main()

    # Duplications: This part duplicates the logic of the process_data function
    data = "DUPLICATE"
    processed_data = ""
    for char in data:
        processed_data += char.lower()
    print(processed_data)
