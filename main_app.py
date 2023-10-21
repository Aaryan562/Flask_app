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
def execute_query_id(conn, query, params=None):
  cur = conn.cursor()
  cur.execute(query, params)  # Pass the params as a tuple
  rows = cur.fetchall()
  if len(rows)==0:
     return "There is no such id present in the database"
     
  column_names = [desc[0] for desc in cur.description]

  result = []
  for row in rows:
      result.append(dict(zip(column_names, row)))

  cur.close()
  conn.close()

  return result[0]

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

@app.route("/api/jobs/<id>")
def list_jobs_id(id):
  conn=get_database_connection()
  query = "SELECT * from carrer where id=%s"
  result = execute_query_id(conn, query,(id,))
  return render_template('page.html',job=result)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)