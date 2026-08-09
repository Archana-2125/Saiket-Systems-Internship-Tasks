try:
    with open("sample.txt", "r") as file:
        data = file.read()

    print("Original Data:")
    print(data)

    old_word = input("Enter word to find: ")
    new_word = input("Enter word to replace with: ")

    modified_data = data.replace(old_word, new_word)

    with open("sample.txt", "w") as file:
        file.write(modified_data)

    print("File updated successfully!")

except FileNotFoundError:
    print("Error: sample.txt file not found.")
