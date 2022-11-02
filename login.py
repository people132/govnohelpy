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
        try:
            log = cursor_db.execute(('''SELECT fio FROM info
                                               WHERE login = '{}';
                                               ''').format(session['email'])).fetchone()[0]
        except:
            return redirect(url_for('reg'))
        if request.method == 'POST':
            mainSkill = request.form['select1']
            mainHour = request.form['select2']
            secondSkill = request.form['select3']
            secondHour = request.form['select4']
            hour = request.form['select5']
            lengug = ' '.join(request.form.getlist('len'))
            work = ' '.join(request.form.getlist('field'))

            db_lp = sqlite3.connect('bases/login_password.db')
            cursor_db = db_lp.cursor()
            sql_insert1 = f'''UPDATE info SET mainskill = "{mainSkill}",mainhoure = "{mainHour}",secondskill = "{secondSkill}",
                    secondhour = "{secondHour}", laguage = "{lengug}", freehour = "{hour}", work = "{work}" 
                         WHERE login ="{session['email']}";'''

            cursor_db.execute(sql_insert1)

            cursor_db.close()

            db_lp.commit()
            db_lp.close()
            print(mainSkill, mainHour, secondSkill, secondHour, lengug, work)

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
        cur1 = cursor_db.execute(f'''SELECT password FROM login_password
                                            WHERE login = "{email}"''').fetchone()
        print(cur1)
        print(cur)
        if cur1 is None:
            print('reg')
            db_lp.close()
            redirect(url_for('reg'))
        else:
            print(cur[0], hashlib.sha512(Password.encode()).hexdigest())
            if cur[0] != str(hashlib.sha512(Password.encode()).hexdigest()):
                db_lp.close()
                return redirect(url_for('reg'))
            else:
                db_lp.close()
                redirect(url_for('qu'))


        return redirect(url_for('qu'))

    return render_template('auth.html')


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        phone = request.form['phone']
        fio = request.form['fio']

        db_lp = sqlite3.connect('bases/login_password.db')
        cursor_db = db_lp.cursor()
        if cursor_db.execute(f'''SELECT password FROM login_password
                                            WHERE login = "{login}"''').fetchone() == None:
            sql_insert = f'''INSERT INTO login_password VALUES('{login}','{str(hashlib.sha512(password.encode()).hexdigest())}');'''
            sql_insert1 = f'''INSERT INTO info VALUES('{login}','{fio}', '{phone}');'''

            cursor_db.execute(sql_insert)
            cursor_db.execute(sql_insert1)

            cursor_db.close()

            db_lp.commit()
            db_lp.close()
        else:
            return redirect(url_for('auth'))
            return '''<script> 
                alert('Пользователь уже существует')
            </script>'''
        return redirect(url_for('auth'))

    return render_template('reg.html')


app.run(debug=True)
