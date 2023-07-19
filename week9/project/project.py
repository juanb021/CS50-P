import csv
import random
import os
import string

class U_data:

    def __init__(self, name, username, length=12, numbers=True, capitals=True , password='123456789'):
        if not name:
            raise ValueError('Missing Name')
        if not username:
            raise ValueError('Missing Username')
        self._name = name
        self._username = username
        self._length = length
        self._numbers = numbers
        self._capitals = capitals
        self._password = password

    def __str__(self):
        return f'{self.name} username is {self.username} and the password is {self.password}'

    @property
    def name(self):
        return self._name

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return generate(self._length, self._numbers, self._capitals)



def main():

    # get user input and generate password
    user = U_data(*get_data())

    # save password to csv file
    save_file(user.name, user.username, user.password)
    print("Password saved!")

    # read passwords from csv file and print them
    data = read_file()
    for row in data:
        print(row['Name'], row['Username'], row['Password'])


def get_data():
    while True:
        name = input('Name for the password: ')

        if name and len(name) < 12:
            break
    while True:
        username = input('Username for the password: ')

        if username and len(username) < 20:
            break
    try:
        length = int(input('Length of the password: '))
    except:
        length = 12
    try:
        number = input('Do you want to use numbers (y/n)').lower().strip() == 'y'
    except:
        pass

    try:
        capital = input('Do you want to use capital letters (y/n)').lower().strip() == 'y'
    except:
        pass

    return name, username, length , number, capital

def generate(length, numbers=False, capital=False):
    """Generate a password of a given length with optional numbers and capital letters."""
    characters = string.ascii_lowercase
    if numbers:
        characters += string.digits
    if capital:
        characters += string.ascii_uppercase
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_file(name, username, password):

    # Create the variables that will be needed.
    headers = ['Name', 'Username', 'Password']
    data = [name, username, password]

    # Check if the file exists
    file_exists = os.path.isfile('passwords.csv')
    with open('passwords.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        # If the file doesnt exists writte the headers.
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(data)

def read_file():
    with open('passwords.csv', newline='') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)
        return data


if __name__ == '__main__':
    main()
