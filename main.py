import os

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
    with open(file_path, 'w') as file:
        file.write(data + secret_key)

def get_user_input():
    user_input = input("Enter some text: ")
    return user_input

def process_data(data):
    processed_data = data.lower()
    return processed_data

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

if __name__ == "__main__":
    main()
