from flask import Flask, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

# データベースのセットアップ
DATABASE = 'data.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.data.decode('utf-8')
    timestamp = datetime.utcnow().isoformat()
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO data (content, timestamp) VALUES (?, ?)', (data, timestamp))
    conn.commit()
    conn.close()
    print(f"Received data: {data} at {timestamp}")
    return "Data received and saved", 200

if __name__ == '__main__':
    init_db()
    print("portNo.: 5000")
    app.run(host='0.0.0.0', port=5000)      #  サーバー側ポートは5000に設定
    
