import sqlite3

DATABASE = 'data.db'

def fetch_data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == '__main__':
    data = fetch_data()
    for row in data:
        print(f"ID: {row[0]}, Content: {row[1]}, Timestamp: {row[2]}")
