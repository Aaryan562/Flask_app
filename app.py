from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Engineering Manager (8+ years)',
    'location': 'Bengaluru, India',
    'type': 'Full-Time'
  },
  {
    'id': 2,
    'title': 'Senior Python Engineer (4+ years)',
    'location': 'Bengaluru, India',
    'type': 'Full-Time'
  },
  {
    'id': 3,
    'title': 'Python Interns (Mumbai)',
    'location': 'Mumbai, India',
    'type': 'Hybrid'
  }
]

@app.route("/")
def hello_docsumo():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Docsumo')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)