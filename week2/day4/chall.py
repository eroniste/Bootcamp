import psycopg2
import requests
import random

DB_NAME = "your_database"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )

def create_countries_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Countries (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            capital VARCHAR(100),
            flag TEXT,
            subregion VARCHAR(100),
            population BIGINT
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def fetch_random_countries():
    response = requests.get("https://restcountries.com/v3.1/all")
    if response.status_code != 200:
        print("Failed to fetch countries.")
        return
    
    countries = response.json()
    random_countries = random.sample(countries, 10)
    
    conn = get_connection()
    cursor = conn.cursor()
    
    for country in random_countries:
        name = country.get("name", {}).get("common", "Unknown")
        capital = country.get("capital", ["Unknown"])[0]
        flag = country.get("flags", {}).get("png", "")
        subregion = country.get("subregion", "Unknown")
        population = country.get("population", 0)
        
        cursor.execute("""
            INSERT INTO Countries (name, capital, flag, subregion, population)
            VALUES (%s, %s, %s, %s, %s);
        """, (name, capital, flag, subregion, population))
    
    conn.commit()
    cursor.close()
    conn.close()
    print("10 random countries added to the database.")

def show_countries():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, capital, flag, subregion, population FROM Countries;")
    countries = cursor.fetchall()
    cursor.close()
    conn.close()
    
    print("\nStored Countries:")
    for country in countries:
        print(f"{country[0]} - Capital: {country[1]}, Subregion: {country[3]}, Population: {country[4]}")

if __name__ == "__main__":
    create_countries_table()
    fetch_random_countries()
    show_countries()
