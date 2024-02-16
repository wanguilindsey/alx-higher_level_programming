#!/usr/bin/python3
import MySQLdb
import sys

def main():
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database_name,
                         port=3306)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows using fetchall() method
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Disconnect from server
    db.close()

if __name__ == "__main__":
    main()
