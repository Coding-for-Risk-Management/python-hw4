import sqlite3
import pytest


@pytest.fixture
def db_connection():
    # Create an in-memory SQLite database and return the connection
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create the people table
    cursor.execute('''
        CREATE TABLE people(
            Id INT PRIMARY KEY NOT NULL,
            Name TEXT NOT NULL,
            Age INT NOT NULL,
            Job TEXT NOT NULL
        )
    ''')

    # Insert test data into the people table
    cursor.executescript('''
        INSERT INTO people(Id, Name, Age, Job) VALUES
        (1, 'Alan', 11, 'Unemployed'),
        (2, 'Bob', 22, 'Gamer'),
        (3, 'Chuck', 33, 'Farmer'),
        (4, 'Dave', 44, 'Painter'),
        (5, 'Ed', 55, 'Writer'),
        (6, 'Fred', 66, 'Writer'),
        (7, 'Greg', 77, 'Writer'),
        (8, 'Hank', 88, 'Retired'),
        (9, 'Ike', 99, 'Retired');
    ''')

    yield conn  # Provide the connection to the test

    # Close the connection after the test is done
    conn.close()


def test_self_join_same_job(db_connection):
    cursor = db_connection.cursor()

    # Read the SQL script that the student has provided
    with open('self_join.sql', 'r') as sql_file:
        student_query = sql_file.read()

    # Execute the student's SQL query
    cursor.execute(student_query)

    # Fetch all results from the query
    result = cursor.fetchall()

    # Define the expected result
    expected_result = [
        ('Ed', 'Fred', 'Writer'),
        ('Ed', 'Greg', 'Writer'),
        ('Fred', 'Ed', 'Writer'),
        ('Fred', 'Greg', 'Writer'),
        ('Greg', 'Ed', 'Writer'),
        ('Greg', 'Fred', 'Writer'),
        ('Hank', 'Ike', 'Retired'),
        ('Ike', 'Hank', 'Retired')
    ]

    # Assert that the query result matches the expected result
    assert result == expected_result
