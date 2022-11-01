from flask import Flask, request, render_template, session, url_for, redirect
import sqlite3
import hashlib
import os

app = Flask(__name__, template_folder='pages')
app.secret_key = os.urandom(20).hex()


@app.route('/qu', methods=['GET', 'POST'])
def qu():
    if 'email' in session:
        db_lp = sqlite3.connect('bases/login_password.db')
        cursor_db = db_lp.cursor()
        log = cursor_db.execute(('''SELECT fio FROM info
                                               WHERE login = '{}';
                                               ''').format(session['email'])).fetchone()[0]
        return render_template('qu.html', log=log)
    else:
        return redirect(url_for('auth'))


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        session['email'] = request.form['email']
        email = request.form['email']
        print(email)
        Password = request.form['password']

        db_lp = sqlite3.connect('bases/login_password.db')
        cursor_db = db_lp.cursor()
        cur = cursor_db.execute(f'''SELECT password FROM login_password
                                               WHERE login = "{email}"''').fetchone()
        if cur is not None:
            print(cur[0], hashlib.sha512(Password.encode()).hexdigest())
            if cur[0] != str(hashlib.sha512(Password.encode()).hexdigest()):
                return render_template('auth_bad.html')
            else:
                redirect(url_for('qu'))
        else:
            redirect(url_for('reg'))

        db_lp.close()

        return redirect(url_for('qu'))

    return render_template('auth.html')


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        login = str(request.form['login'])
        password = request.form['password']
        phone = request.form['phone']
        fio = request.form['fio']

        db_lp = sqlite3.connect('bases/login_password.db')
        cursor_db = db_lp.cursor()
        sql_insert = f'''INSERT INTO login_password VALUES('{login}','{str(hashlib.sha512(password.encode()).hexdigest())}');'''
        sql_insert1 = f'''INSERT INTO info VALUES('{login}','{fio}', '{phone}');'''

        cursor_db.execute(sql_insert)
        cursor_db.execute(sql_insert1)

        cursor_db.close()

        db_lp.commit()
        db_lp.close()

        return redirect(url_for('auth'))

    return render_template('reg.html')


if __name__ == "__main__":
    app.run(debug=True)
