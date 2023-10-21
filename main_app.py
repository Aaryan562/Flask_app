from flask import Flask, render_template, jsonify
from database import get_database_connection

app = Flask(__name__)

def get_full_details(conn, query):
  cur = conn.cursor()
  cur.execute(query)
  rows = cur.fetchall()
  column_names = [desc[0] for desc in cur.description]

  result = []
  for row in rows:
      result.append(dict(zip(column_names, row)))

  cur.close()
  conn.close()

  return result

@app.route("/")
def hello_docsumo():
    conn=get_database_connection()
    query = "SELECT * FROM carrer"
    result = get_full_details(conn, query)
    return render_template('home.html', 
                           jobs=result, 
                           company_name='Docsumo')

@app.route("/api/jobs")
def list_jobs():
  conn=get_database_connection()
  query = "SELECT * FROM carrer"
  result = get_full_details(conn, query)
  return jsonify(result)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)