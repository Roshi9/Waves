import sqlite3
import requests
import schedule
import time

# Function to update the database
def update_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('waves.db')  # Replace with your database name
    cursor = conn.cursor()

    # Define the table structure based on the provided columns
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livello (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ordine INTEGER,
            ID_stazione INTEGER,
            stazione TEXT,
            nome_abbr TEXT,   
            latDMSN REAL,   
            lonDMSE REAL,
            latDDN  REAL,
            lonDDE  REAL,
            data    TEXT,
            valore  REAL
        )
    ''')

    # Fetch data from the URI
    response = requests.get('https://dati.venezia.it/sites/default/files/dataset/opendata/livello.json')

    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            # Extract data from the JSON and insert it into the table
            cursor.execute('''
                INSERT INTO livello (ordine, ID_stazione, stazione, nome_abbr, latDMSN, lonDMSE, latDDN, lonDDE, data, valore)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                item['ordine'], 
                item['ID_stazione'], 
                item['stazione'], 
                item['nome_abbr'], 
                item['latDMSN'], 
                item['lonDMSE'], 
                item['latDDN'], 
                item['lonDDE'], 
                item['data'], 
                item['valore']
            ))
        
        conn.commit()  # Commit the changes to the database
        conn.close()
        print('Database updated successfully.')
    else:
        print('Failed to fetch data from the URI')

# Schedule the update to run every 30 minutes
schedule.every(30).minutes.do(update_database)

# Run the scheduled tasks continuously
while True:
    schedule.run_pending()
    time.sleep(1)
