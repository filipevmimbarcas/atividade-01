from flask import Flask, jsonify
import os, psycopg2
DB_CFG = {
 "dbname": os.environ["db-app"],
 "user": os.environ["aluno"],
 "password": os.environ["senac2010"],
 "host": os.environ["db-postgres"], 
 "port": 5432,
}
app = Flask(__name__)
def get_conn():
 return psycopg2.connect(**DB_CFG)
@app.route("/visitantes")
def visitantes():
 with get_conn() as conn:
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS visitas (n INT);")
        cur.execute("INSERT INTO visitas VALUES (1);")
        cur.execute("SELECT SUM(n) FROM visitas;")
        total, = cur.fetchone()
 return jsonify(total_visitas=total)

if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000) 


