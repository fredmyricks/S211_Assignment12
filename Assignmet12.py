import sqlite3

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE quizzes (
    id INTEGER PRIMARY KEY,
    subject TEXT NOT NULL,
    num_questions INTEGER NOT NULL,
    date DATE NOT NULL
);

CREATE TABLE results (
    id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    quiz_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (quiz_id) REFERENCES quizzes (id)
);


INSERT INTO students (id, first_name, last_name)
VALUES (1, 'John', 'Smith');

INSERT INTO quizzes (id, subject, num_questions, date)
VALUES (1, 'Python Basics', 5, '2015-02-05');

INSERT INTO results (id, student_id, quiz_id, score)
VALUES (1, 1, 1, 85);


from flask import Flask, request, redirect, render_template, session, url_for

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')


from flask import Flask, request, redirect, render_template, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    conn = sqlite3.connect('hw13.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.execute('SELECT * FROM quizzes')
    quizzes = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', students=students, quizzes=quizzes)


<!doctype html>
<html>
  <head>
    <title>Dashboard</title>
  </head>
  <body>
    <h1>Students:</h1>
    <table>
      <tr>
        <th>ID</th>
        <th>First Name</th>
        <th>Last Name</th>
      </tr>
      {% for student in students %}
        <tr>
          <td>{{ student[0] }}</td>
          <td>{{ student[1] }}</td>
          <td>{{ student[2] }}</td>
        </tr>
      {% endfor %}
    </table>
    <h1>Quizzes:</h1>
    <table>
      <tr>
        <th>ID</th>
        <th>Subject</th>
        <th>Number of Questions</th>
        <th>Date</th>
      </tr>
      {% for quiz in quizzes %}
        <tr>
          <



