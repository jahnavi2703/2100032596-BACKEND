from flask import Flask, render_template
from mysql.connector import cursor
from prettytable import PrettyTable
import mysql.connector

app = Flask(__name__)
try:
    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jahnavi@03",
        database="BACKEND"
    )


    def index():
        # Define the SQL query
        query_join = """
            SELECT locations.location_id, locations.street_address, locations.city, locations.state_province, countries.country_name
            FROM locations
            JOIN countries ON locations.country_id = countries.country_id
            WHERE countries.country_name = 'Canada'
            """

        # Execute the query
        cursor = db_connection.cursor()
        cursor.execute(query_join)

        # Fetch the results
        results_join = cursor.fetchall()

        # Close the cursor
        cursor.close()

        # Define the SQL query without using JOIN
        query_without_join = """
                    SELECT location_id, street_address, city, state_province, 'Canada' AS country_name
                    FROM locations
                    WHERE country_id = (
                        SELECT country_id FROM countries WHERE country_name = 'Canada'
                    )
                    """

        # Execute the query
        cursor = db_connection.cursor()
        cursor.execute(query_without_join)

        # Fetch the results
        results_without_join = cursor.fetchall()

        # Close the cursor
        cursor.close()

        # Render the results in an HTML table
        return render_template('index.html', results_join=results_join, results_without_join=results_without_join)


    @app.route('/')
    def home():
        return index()


    if __name__ == '__main__':
        app.run(debug=True)

except mysql.connector.Error as e:
    print("Error while connecting to MySQL database:", e)



 # Function to insert data into the locations table
    """def insert_into_locations(data):
        cursor = db_connection.cursor()
        query = "INSERT IGNORE INTO locations (location_id, street_address, postal_code, city, state_province, country_id) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.executemany(query, data)
        db_connection.commit()
        cursor.close()

    # Function to insert data into the countries table
    def insert_into_countries(data):
        cursor = db_connection.cursor()
        query = "INSERT IGNORE INTO countries (country_id, country_name, region_id) VALUES (%s, %s, %s)"
        cursor.executemany(query, data)
        db_connection.commit()
        cursor.close()

    @app.route('/')
    def index():
        return "Data insertion to database successful!"

    if __name__ == '__main__':
        # Data to be inserted into the locations table
        locations_data = [
            (1000, "1297 Via Cola di Rie", 989, "Roma", " ", "IT"),
            (1100, "93091 Calle della Te", 10934, "Venice", " ", "IT"),
            (1200, "2017 Shinjuku-ku", 1689, "Tokyo", "Tokyo Prefectu", "JP"),
            (1300, "9450 Keniya-cho", 6823, "Hiroshima", " ", "JP"),
            (1400, "2014 Jabberwocky Rd", 26192, "Southlake", "Texas", "US"),
            (1500, "2011 Interiors Blvd", 99236, "South San", "California", "US"),
            (1600, "2007 Zagora St", 50090, "South Brun", "New Jersey", "US"),
            (1700, "2004 Charade Rd", 98199, "Seattle", "Washington", "US"),
            (1800, "147 Spadina Ave", "MSV 2L7", "Toronto", "Ontario", "CA")
        ]

        # Data to be inserted into the countries table
        countries_data = [
            ("AR", "Argentina", 2),
            ("AU", "Australia", 3),
            ("BE", "Belgium", 1),
            ("BR", "Brazil", 2),
            ("CA", "Canada", 2),
            ("CH", "Switzerland", 1),
            ("CN", "China", 3),
            ("DE", "Germany", 1)
        ]

        # Insert data into the locations table
        insert_into_locations(locations_data)

        # Insert data into the countries table
        insert_into_countries(countries_data)

        app.run(debug=True)


except mysql.connector.Error as e:
    print("Error while connecting to MySQL database:", e)"""