# Password Generator
    #### Video Demo:  https://youtu.be/tusgqNZA9qY
    #### Description:

This code is a Python program for generating passwords and saving them to a CSV file. The program is object-oriented, with a U_data class that encapsulates the user data and a few functions to generate, save, and retrieve data.

The U_data class takes the user's name, username, password length, and optional parameters for including numbers and capital letters. It checks that the name and username are not empty strings, and generates a random password based on the user's parameters. The __str__ method returns a string representation of the user data.

The main function is the entry point for the program. It calls the get_data function to prompt the user for their data, creates a U_data instance with that data, generates a password, saves it to a CSV file, and prints a confirmation message.

The get_data function prompts the user for their name, username, and password length, with default values of 12 for the length and no numbers or capital letters. It returns a tuple of the user's data.

The generate function takes a password length and optional parameters for including numbers and capital letters, and generates a random password using the random and string modules.

The save_file function takes a name, username, and password, and saves them to a CSV file named "passwords.csv". It uses the csv module to write the data to the file. If the file doesn't exist, it creates it and writes a header row.

The object-oriented design makes it easy to encapsulate user data and generate passwords, and the use of modules like csv and random simplifies file I/O and random string generation.

The libraries used in this program are:

    -csv: Used for reading and writing CSV files.
    -random: Used for generating random numbers and characters.
    -os: Used for checking if a file exists.
    -string: Used for accessing string constants like letters, digits, and punctuation.

