
with open("output.txt", "w") as file:
    user_input = input("Enter some text to write to the file: ")
    file.write(user_input + "\n")


with open("output.txt", "a") as file:
    additional_data = input("Enter additional text to append to the file: ")
    file.write(additional_data + "\n")


with open("output.txt", "r") as file:
    print("\nFinal content of output.txt:")
    print(file.read())
