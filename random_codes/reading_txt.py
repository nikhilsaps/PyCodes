import sqlite3
from sqlite3 import Error

def create_database():
    try:
        # Connect to SQLite database (or create if not exists)
        connection = sqlite3.connect('love_database.db')

        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()

        # Create the table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS love_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                dob DATE,
                year INTEGER
            )
        ''')

        # Commit the changes and close the connection
        connection.commit()
        print('Database "love_database.db" created successfully.')

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        if connection:
            connection.close()

def add_entry(name, age, dob, year):
    try:
        # Connect to SQLite database
        connection = sqlite3.connect('love_database.db')
        cursor = connection.cursor()

        # Insert a new entry into the table
        cursor.execute('''
            INSERT INTO love_data (name, age, dob, year)
            VALUES (?, ?, ?, ?)
        ''', (name, age, dob, year))

        # Commit the changes and close the connection
        connection.commit()
        print('Entry added successfully.')

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        if connection:
            connection.close()

def main():
    # Create the SQLite database if it doesn't exist
    create_database()

    # Get input for a new entry
    name = input('Enter name: ')
    age = input('Enter age: ')
    dob = input('Enter date of birth (YYYY-MM-DD): ')
    year = input('Enter year: ')

    # Add the new entry to the SQLite database
    add_entry(name, age, dob, year)

if __name__ == "__main__":
    main()
