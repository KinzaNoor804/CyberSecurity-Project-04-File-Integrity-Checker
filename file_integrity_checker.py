import hashlib

print("FILE INTEGRITY CHECKER")

file_name = input("Enter file name with extension: ")

try:
    with open(file_name, "rb") as file:
        file_data = file.read()

    hash_value = hashlib.sha256(file_data).hexdigest()

    print("File Name:", file_name)
    print("SHA-256 Hash:")
    print(hash_value)

except FileNotFoundError:
    print("Error: File not found. Please check the file name.")