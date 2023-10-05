import sqlite3
import requests
import schedule
import time

# Function to update the database
def update_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('waves.db')  # Replace with your database name
    cursor = conn.cursor()

    # Define the table structure for the 'livello' table based on the provided columns
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

    # Fetch data from the URI for the 'livello' table
    response_livello = requests.get('https://dati.venezia.it/sites/default/files/dataset/opendata/livello.json')

    if response_livello.status_code == 200:
        data = response_livello.json()
        
        for item in data:
            # Extract data from the JSON and insert it into the 'livello' table
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
        
        print('Database (livello) updated successfully.')
    else:
        print('Failed to fetch data for livello from the URI')

    # Define the table structure for the 'vento' table based on the provided columns
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_stazione INTEGER,
            stazione TEXT,
            data    TEXT,
            valore  REAL
        )
    ''')

    # Fetch data from the URI for the 'vento' table
    response_vento = requests.get('https://dati.venezia.it/sites/default/files/dataset/opendata/vento.json')

    if response_vento.status_code == 200:
        data = response_vento.json()
        
        for item in data:
            # Extract data from the JSON and insert it into the 'vento' table
            cursor.execute('''
                INSERT INTO vento (ID_stazione, stazione, data, valore)
                VALUES (?, ?, ?, ?)
            ''', (
                item['ID_stazione'], 
                item['stazione'], 
                item['data'], 
                item['valore']
            ))
        
        print('Database (vento) updated successfully.')
    else:
        print('Failed to fetch data for vento from the URI')

    # Define the table structure for the 'pressione' table based on the provided columns
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pressione (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ordine INTEGER,
            ID_stazione INTEGER,
            stazione TEXT,
            nome_abbr TEXT,
            latDMSN REAL,
            lonDMSE REAL,
            latDDN REAL,
            lonDDE REAL,
            data TEXT,
            valore REAL
        )
    ''')

    # Fetch data from the URI for the 'pressione' table
    response_pressione = requests.get('https://dati.venezia.it/sites/default/files/dataset/opendata/pressione.json')

    if response_pressione.status_code == 200:
        data = response_pressione.json()

        for item in data:
            # Extract data from the JSON and insert it into the 'pressione' table
            cursor.execute('''
                INSERT INTO pressione (ordine, ID_stazione, stazione, nome_abbr, latDMSN, lonDMSE, latDDN, lonDDE, data, valore)
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

        print('Database (pressione) updated successfully.')
    else:
        print('Failed to fetch data for pressione from the URI')

    # Define the table structure for the 'radiazione' table based on the provided columns
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS radiazione (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DATA TEXT,
            ID_stazione INTEGER,
            STAZIONE TEXT,
            VALORE REAL
        )
    ''')

    # Fetch data from the URI for the 'radiazione' table
    response_radiazione = requests.get('https://dati.venezia.it/sites/default/files/dataset/opendata/radiazione.json')

    if response_radiazione.status_code == 200:
        data = response_radiazione.json()

        for item in data:
            # Extract data from the JSON and insert it into the 'radiazione' table
            cursor.execute('''
                INSERT INTO radiazione (DATA, ID_stazione, STAZIONE, VALORE)
                VALUES (?, ?, ?, ?)
            ''', (
                item['DATA'],
                item['ID_stazione'],
                item['STAZIONE'],
                item['VALORE']
            ))

        print('Database (radiazione) updated successfully.')
    else:
        print('Failed to fetch data for radiazione from the URI')

    # Define the table structure for the 'tempacqua' table based on the provided columns
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tempacqua (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ordine INTEGER,
            ID_stazione INTEGER,
            stazione TEXT,
            nome_abbr TEXT,
            latDMSN REAL,
            lonDMSE REAL,
            latDDN REAL,
            lonDDE REAL,
            data TEXT,
            valore REAL
        )
    ''')

    # Fetch data from the URI for the 'tempacqua' table
    response_tempacqua = requests.get('https://dati.venezia.it/sites/default/files/dataset/opendata/tempacqua.json')

    if response_tempacqua.status_code == 200:
        data = response_tempacqua.json()

        for item in data:
            # Extract data from the JSON and insert it into the 'tempacqua' table
            cursor.execute('''
                INSERT INTO tempacqua (ordine, ID_stazione, stazione, nome_abbr, latDMSN, lonDMSE, latDDN, lonDDE, data, valore)
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

        conn.commit()  # Commit the changes to the 'tempacqua' table
        print('Database (tempacqua) updated successfully.')
    else:
        print('Failed to fetch data for tempacqua from the URI')

    conn.close()

# Schedule the update to run every 30 minutes
schedule.every(30).minutes.do(update_database)

# Run the scheduled tasks continuously
while True:
    schedule.run_pending()
    time.sleep(1)