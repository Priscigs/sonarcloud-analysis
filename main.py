import os
import sys

# Lines of Code: This function has a high number of lines to increase LOC count
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist")
        return None 
    except Exception as e:
        # Bugs: Ignoring other exceptions can cause hidden issues
        pass

def write_file(file_path, data):
    # Vulnerabilities: Hardcoded sensitive information
    secret_key = "12345"
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

def duplicate_code():
    # Duplications: This function duplicates the logic of process_data
    data = "DUPLICATE"
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

    # Coverage: This part is added to show test coverage, it will not be executed normally
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Testing duplicate code to show test coverage
        print(duplicate_code())
