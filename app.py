from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Lagos, Nigeria',
    'salary': '$100,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Lagos, Nigeria',
    'salary': ' $150,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]

@app.route("/")
def tnsquad():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Techie Nerd Squad')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)