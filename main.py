from flask import Flask, request, render_template, session, url_for, redirect
import sqlite3
import hashlib
import os
import json
import smtplib
import random

app = Flask(__name__, template_folder='pages')
app.secret_key = os.urandom(20).hex()


@app.route('/qu', methods=['GET', 'POST'])
def qu():
    if 'email' in session:
        print(session['email'])
        db_lp = sqlite3.connect('bases/login_password.db')
        cursor_db = db_lp.cursor()
        try:
            log1 = \
                cursor_db.execute(
                    ('''SELECT name FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[0]
            log2 = cursor_db.execute(
                ('''SELECT surname FROM info WHERE email = '{}'; ''').format(session['email'])).fetchone()[0]
            log = log1 + ' ' + log2
        except:
            return redirect(url_for('reg'))
        # db_lp = sqlite3.connect('bases/login_password.db')
        # cursor_db = db_lp.cursor()
        username = \
            cursor_db.execute(('''SELECT name FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[0]
        surname = \
            cursor_db.execute(('''SELECT surname FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[
                0]
        patronymic = \
            cursor_db.execute(
                ('''SELECT patronymic FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[
                0]
        number = \
            cursor_db.execute(('''SELECT phone FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[0]
        tg = cursor_db.execute(('''SELECT tg FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[0]
        vk = cursor_db.execute(('''SELECT vk FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[0]
        mainSkill = \
            cursor_db.execute(
                ('''SELECT mainSkill FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[0]
        mainHour = \
            cursor_db.execute(
                ('''SELECT mainHour FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[0]
        secondSkill = \
            cursor_db.execute(
                ('''SELECT secondSkill FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[
                0]
        secondHour = \
            cursor_db.execute(
                ('''SELECT secondHour FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[
                0]
        language = \
            cursor_db.execute(
                ('''SELECT language FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[0]
        workHoure = \
            cursor_db.execute(
                ('''SELECT workHoure FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[0]
        typeConnect = \
            cursor_db.execute(
                ('''SELECT typeConnect FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[
                0]
        description = \
            cursor_db.execute(
                ('''SELECT description FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[
                0]
        rus_zac = \
            cursor_db.execute(('''SELECT ruszac FROM info WHERE email = '{}';''').format(session['email'])).fetchone()[
                0]
        cursor_db.close()
        db_lp.commit()
        db_lp.close()
        language1 = language.split()
        alllanguage = ['английский', 'французкий', 'немецкий', 'итальянский', 'русский', 'украинский', 'белорусский']
        english = ''
        french = ''
        german = ''
        italian = ''
        russian = ''
        ukraian = ''
        belorussian = ''
        print(language1)
        ruszac1 = ''
        if 'английский' in language1:
            english = 'checked'
        if 'французский' in language1:
            french = 'checked'
        if 'немецкий' in language1:
            german = 'checked'
        if 'итальянский' in language1:
            italian = 'checked'
        if 'русский' in language1:
            russian = 'checked'
        if 'украинский' in language1:
            ukraian = 'checked'
        if 'белорусский' in language1:
            belorussian = 'checked'
        typeConnect1 = typeConnect.split()
        messenger = ''
        site = ''
        if 'messenger' in typeConnect1:
            messenger = 'checked'
        if 'site' in typeConnect1:
            site = 'checked'
        if rus_zac != '':
            ruszac1 = 'checked'

        video_editing1 = ''
        photo_editing1 = ''
        front_end_application_development1 = ''
        front_end_website_development1 = ''
        back_end_website_development1 = ''
        zero_coding1 = ''
        electronic_music1 = ''
        live_music1 = ''
        music_vocals1 = ''
        announcer_art1 = ''
        text1 = ''
        translations1 = ''
        cgi1 = ''
        smm1 = ''
        UI_design1 = ''
        UX_design1 = ''
        painting_digital1 = ''
        painting_classic1 = ''
        wood_crafts1 = ''
        fabric_wool_handicrafts1 = ''
        handicrafts1 = ''

        video_editing2 = ''
        photo_editing2 = ''
        front_end_application_development2 = ''
        front_end_website_development2 = ''
        back_end_website_development2 = ''
        zero_coding2 = ''
        electronic_music2 = ''
        live_music2 = ''
        music_vocals2 = ''
        announcer_art2 = ''
        text2 = ''
        translations2 = ''
        cgi2 = ''
        smm2 = ''
        UI_design2 = ''
        UX_design2 = ''
        painting_digital2 = ''
        painting_classic2 = ''
        wood_crafts2 = ''
        fabric_wool_handicrafts2 = ''
        handicrafts2 = ''

        one1 = ''
        two1 = ''
        three1 = ''
        four1 = ''
        five1 = ''
        six1 = ''
        seven1 = ''
        eight1 = ''
        nine1 = ''
        ten1 = ''
        more1 = ''

        one2 = ''
        two2 = ''
        three2 = ''
        four2 = ''
        five2 = ''
        six2 = ''
        seven2 = ''
        eight2 = ''
        nine2 = ''
        ten2 = ''
        more2 = ''

        one_five = ''
        five_ten = ''
        ten_twenty = ''
        twenty_thirty = ''
        thirty_fourty = ''
        fourty_more = ''

        if mainSkill == 'видеомонтаж':
            video_editing1 = 'selected'
        elif mainSkill == 'фоторедактура':
            photo_editing1 = 'selected'
        elif mainSkill == 'фронт-энд разработка приложений':
            front_end_application_development1 = 'selected'
        elif mainSkill == 'фронт-энд разработка сайтов':
            front_end_website_development1 = 'selected'
        elif mainSkill == 'бэк-энд разработка сайтов':
            back_end_website_development1 = 'selected'
        elif mainSkill == 'zero coding':
            zero_coding1 = 'selected'
        elif mainSkill == 'музыка электронная':
            electronic_music1 = 'selected'
        elif mainSkill == 'музыка живая':
            live_music1 = 'selected'
        elif mainSkill == 'музыка вокал':
            music_vocals1 = 'selected'
        elif mainSkill == 'дикторское искусство':
            announcer_art1 = 'selected'
        elif mainSkill == 'текст':
            text1 = 'selected'
        elif mainSkill == 'переводы (укажите язык ниже)':
            translations1 = 'selected'
        elif mainSkill == 'SMM':
            smm1 = 'selected'
        elif mainSkill == 'CGI (комп.графика)':
            cgi1 = 'selected'
        elif mainSkill == 'Ui-дизайн (пользовательский интерфейс)':
            UI_design1 = 'selected'
        elif mainSkill == 'UX-дизайн (архитектура, удобство пользования)':
            UX_design1 = 'selected'
        elif mainSkill == 'живопись -digital':
            painting_digital1 = 'selected'
        elif mainSkill == 'живопись - классика':
            painting_classic1 = 'selected'
        elif mainSkill == 'поделки руками из дерева':
            wood_crafts1 = 'selected'
        elif mainSkill == 'поделки руками из ткани/шерсти':
            fabric_wool_handicrafts1 = 'selected'
        elif mainSkill == 'поделки руками из прочих худ. материалов':
            handicrafts1 = 'selected'

        if mainHour == '1':
            one1 = 'selected'
        elif mainHour == '2':
            two1 = 'selected'
        elif mainHour == '3':
            three1 = 'selected'
        elif mainHour == '4':
            four1 = 'selected'
        elif mainHour == '5':
            five1 = 'selected'
        elif mainHour == '6':
            six1 = 'selected'
        elif mainHour == '7':
            seven1 = 'selected'
        elif mainHour == '8':
            eight1 = 'selected'
        elif mainHour == '9':
            nine1 = 'selected'
        elif mainHour == '10':
            ten1 = 'selected'
        elif mainHour == 'более 10':
            more1 = 'selected'

        if secondSkill == 'видеомонтаж':
            video_editing2 = 'selected'
        elif secondSkill == 'фоторедактура':
            photo_editing2 = 'selected'
        elif secondSkill == 'фронт-энд разработка приложений':
            front_end_application_development2 = 'selected'
        elif secondSkill == 'фронт-энд разработка сайтов':
            front_end_website_development2 = 'selected'
        elif secondSkill == 'бэк-энд разработка сайтов':
            back_end_website_development2 = 'selected'
        elif secondSkill == 'zero coding':
            zero_coding2 = 'selected'
        elif secondSkill == 'музыка электронная':
            electronic_music2 = 'selected'
        elif secondSkill == 'музыка живая':
            live_music2 = 'selected'
        elif secondSkill == 'музыка вокал':
            music_vocals2 = 'selected'
        elif secondSkill == 'дикторское искусство':
            announcer_art2 = 'selected'
        elif secondSkill == 'текст':
            text2 = 'selected'
        elif secondSkill == 'переводы (укажите язык ниже)':
            translations2 = 'selected'
        elif secondSkill == 'SMM':
            smm2 = 'selected'
        elif secondSkill == 'CGI (комп.графика)':
            cgi2 = 'selected'
        elif secondSkill == 'Ui-дизайн (пользовательский интерфейс)':
            UI_design2 = 'selected'
        elif secondSkill == 'UX-дизайн (архитектура, удобство пользования)':
            UX_design2 = 'selected'
        elif secondSkill == 'живопись -digital':
            painting_digital2 = 'selected'
        elif secondSkill == 'живопись - классика':
            painting_classic2 = 'selected'
        elif secondSkill == 'поделки руками из дерева':
            wood_crafts2 = 'selected'
        elif secondSkill == 'поделки руками из ткани/шерсти':
            fabric_wool_handicrafts2 = 'selected'
        elif secondSkill == 'поделки руками из прочих худ. материалов':
            handicrafts2 = 'selected'

        if secondHour == '1':
            one2 = 'selected'
        elif secondHour == '2':
            two2 = 'selected'
        elif secondHour == '3':
            three2 = 'selected'
        elif secondHour == '4':
            four2 = 'selected'
        elif secondHour == '5':
            five2 = 'selected'
        elif secondHour == '6':
            six2 = 'selected'
        elif secondHour == '7':
            seven2 = 'selected'
        elif secondHour == '8':
            eight2 = 'selected'
        elif secondHour == '9':
            nine2 = 'selected'
        elif secondHour == '10':
            ten2 = 'selected'
        elif secondHour == 'более 10':
            more2 = 'selected'

        if workHoure == '1-5':
            one_five = 'selected'
        elif workHoure == '5-10':
            five_ten = 'selected'
        elif workHoure == '10-20':
            ten_twenty = 'selected'
        elif workHoure == '20-30':
            twenty_thirty = 'selected'
        elif workHoure == '30-40':
            thirty_fourty = 'selected'
        elif workHoure == 'более 40':
            fourty_more = 'selected'

        if request.method == 'POST':
            if request.form['button'] == 'save':
                db_lp1 = sqlite3.connect('bases/login_password.db')
                cursor_db1 = db_lp1.cursor()
                mainSkill = request.form['mainSkill']
                mainHour = request.form['mainHour']
                secondSkill = request.form['secondSkill']
                secondHour = request.form['secondHour']
                workHoure = request.form['workHoure']
                username = request.form['username']
                surname = request.form['surname']
                patronymic = request.form['patronymic']
                number = request.form['number']
                tg = request.form['tg']
                vk = request.form['vk']
                rus_zac = request.form['rus_zac']
                description = request.form['description']
                language = ' '.join(request.form.getlist('language'))
                typeConnect = ' '.join(request.form.getlist('typeConnect'))
                cursor_db1.execute(
                    f'''UPDATE info SET name = "{username}", surname = "{surname}", patronymic = "{patronymic}", phone = "{number}", tg = "{tg}", vk = "{vk}", mainSkill = "{mainSkill}",mainHour = "{mainHour}",secondSkill = "{secondSkill}",
                    secondHour = "{secondHour}", language = "{language}", workHoure = "{workHoure}", typeConnect = "{typeConnect}",  description = "{description}", ruszac = "{rus_zac}"
                        WHERE email ="{session['email']}";''')
                cursor_db1.close()
                db_lp1.commit()
                db_lp1.close()
                print(mainSkill, mainHour, secondSkill, secondHour, language, typeConnect)
                return redirect(url_for('account'))
            if request.form['button'] == 'reset':
                return redirect(url_for('resPas'))
        return render_template('qu.html', log=log, Username=username, Surname=surname, Patronymic=patronymic,
                               Number=number, Tg=tg, Vk=vk, Rus_zac=ruszac1, Messenger=messenger, Site=site,
                               English=english, French=french, German=german, Italian=italian, Russian=russian,
                               Ukrain=ukraian, Belorussian=belorussian,
                               video_editing1=video_editing1, photo_editing1=photo_editing1,
                               front_end_application_development1=front_end_application_development1,
                               front_end_website_development1=front_end_website_development1,
                               back_end_website_development1=back_end_website_development1, zero_coding1=zero_coding1,
                               electronic_music1=electronic_music1, live_music1=live_music1,
                               music_vocals1=music_vocals1, announcer_art1=announcer_art1, text1=text1,
                               translations1=translations1, smm1=smm1, cgi1=cgi1, UI_design1=UI_design1,
                               UX_design1=UX_design1, painting_digital1=painting_digital1,
                               painting_classic1=painting_classic1, wood_crafts1=wood_crafts1,
                               fabric_wool_handicrafts1=fabric_wool_handicrafts1, handicrafts1=handicrafts1, one1=one1,
                               two1=two1, three1=three1, four1=four1, five1=five1, six1=six1, seven1=seven1,
                               eight1=eight1, nine1=nine1, ten1=ten1, more1=more1,
                               video_editing2=video_editing2, photo_editing2=photo_editing2,
                               front_end_application_development2=front_end_application_development2,
                               front_end_website_development2=front_end_website_development2,
                               back_end_website_development2=back_end_website_development2, zero_coding2=zero_coding2,
                               electronic_music2=electronic_music2, live_music2=live_music2,
                               music_vocals2=music_vocals2, announcer_art2=announcer_art2, text2=text2,
                               translations2=translations2, smm2=smm2, cgi2=cgi2, UI_design2=UI_design2,
                               UX_design2=UX_design2, painting_digital2=painting_digital2,
                               painting_classic2=painting_classic2, wood_crafts2=wood_crafts2,
                               fabric_wool_handicrafts2=fabric_wool_handicrafts2, handicrafts2=handicrafts2, one2=one2,
                               two2=two2, three2=three2, four2=four2, five2=five2, six2=six2, seven2=seven2,
                               eight2=eight2, nine2=nine2, ten2=ten2, more2=more2,
                               one_five=one_five, five_ten=five_ten, ten_twenty=ten_twenty, twenty_thirty=twenty_thirty,
                               thirty_fourty=thirty_fourty, fourty_more=fourty_more, Description=description)
    else:
        return redirect(url_for('auth'))


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    error = 'error'
    msg = ''
    if request.method == 'POST':
        try:
            session['email'] = request.form['username']
            email = request.form['username']
            password = request.form['password']
            db_lp = sqlite3.connect('bases/login_password.db')
            cursor_db = db_lp.cursor()
            cur = cursor_db.execute(f'''SELECT password FROM login_password
                                                WHERE login = "{email}"''').fetchone()
            cur1 = cursor_db.execute(f'''SELECT password FROM login_password
                                                WHERE login = "{email}"''').fetchone()
            print(cur1)
            print(cur)
            if cur1 is None:
                cursor_db.close()
                print('reg')
                db_lp.close()
                error = 'error active'
                msg = 'Введён неверный логин или пароль'
            else:
                print(cur[0], hashlib.sha512(password.encode()).hexdigest())
                if cur[0] != str(hashlib.sha512(password.encode()).hexdigest()):
                    cursor_db.close()
                    db_lp.close()
                    error = 'error active'
                    msg = 'Введён неверный логин или пароль'
                else:
                    skill = cursor_db.execute(('''SELECT mainSkill FROM info
                                                WHERE email = '{}';
                                                ''').format(session['email'])).fetchone()[0]
                    print(skill)
                    print(type(skill))
                    cursor_db.close()
                    db_lp.close()
            if skill != '':
                return redirect(url_for('account'))
            else:
                return redirect(url_for('qu'))
        except UnboundLocalError:
                error = 'error active'
                msg = 'Введён неверный логин или пароль'
    return render_template('auth.html', Error = error, Msg = msg)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    error = 'error'
    error_msg = ''
    code = ''
    surname = ''
    name = ''
    patronymic = ''
    email = ''
    number = ''
    tg = ''
    vk = ''
    password = ''
    if request.method == 'POST':
        if request.form['button'] == 'reg':
            surname = request.form['surname']
            name = request.form['username']
            patronymic = request.form['patronymic']
            email = request.form['email']
            number = request.form['number']
            tg = request.form['tg']
            vk = request.form['vk']
            code = request.form['code']
            password = request.form['password']
            try:
                print(code, session['code'])
                if session['code'] == code:
                    session.pop('code', None)
                    db_lp = sqlite3.connect('bases/login_password.db')
                    cursor_db = db_lp.cursor()
                    print('yes')
                    if cursor_db.execute(f'''SELECT password FROM login_password
                                                    WHERE login = "{email}"''').fetchone() == None:
                        sql_insert = f'''INSERT INTO login_password VALUES('{email}','{str(hashlib.sha512(password.encode()).hexdigest())}');'''
                        sql_insert1 = f'''INSERT INTO info VALUES('{email}','{name}', '{surname}', '{patronymic}', '{number}', '{vk}', '{tg}', '{""}', '{""}', '{""}', '{""}', '{""}', '{""}', '{""}', '{""}', '{""}');'''
                        cursor_db.execute(sql_insert)
                        cursor_db.execute(sql_insert1)
                        cursor_db.close()
                        db_lp.commit()
                        db_lp.close()
                        return redirect(url_for('auth'))
                    else:
                        print('no')
                        error = 'error active'
                        error_msg = 'Такой аккаунт уже существует'
                else:
                    error = 'error active'
                    error_msg = 'Код введен не верно'
                    session.pop('code', None)
            except KeyError:
                error = 'error active'
                error_msg = 'отправьте новый код на почту'
        if request.form['button'] == 'code':
            session.pop('code', None)
            surname = request.form['surname']
            name = request.form['username']
            patronymic = request.form['patronymic']
            email = request.form['email']
            number = request.form['number']
            tg = request.form['tg']
            vk = request.form['vk']
            password = request.form['password']
            session['code'] = generate(5)
            letter(email, session['code'])
    return render_template('reg.html', Error_msg=error_msg, Error=error, Surname=surname, Username=name,
                           Patronymic=patronymic, Email=email, Number=number, Tg=tg, Vk=vk, Password=password)


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('auth'))



@app.route('/account', methods=['GET', 'POST'])
def account():
    fio = ''
    summ = 0
    if 'email' in session:
        if request.method == 'POST':
            db_lp1 = sqlite3.connect('bases/login_password.db')
            cur = db_lp1.cursor()
            mainSkill = cur.execute(f'''SELECT mainSkill FROM info WHERE email = "{session['email']}";''').fetchone()[0]
            secondSkill = cur.execute(f'''SELECT secondSkill FROM info WHERE email = "{session['email']}";''').fetchone()[0]
            rus_zak = cur.execute(f'''SELECT ruszac FROM info WHERE email = "{session['email']}";''').fetchone()[0]
            print(f'''INSERT INTO queue VALUES("{session['email']}", "{mainSkill}", "{secondSkill}", "{rus_zak}");''')
            cur.execute(f'''INSERT INTO queue VALUES("{session['email']}", "{mainSkill}", "{secondSkill}", "{rus_zak}");''')
            db_lp1.commit()
            cur.close()
            db_lp1.close()
        db_lp = sqlite3.connect('bases/login_password.db')
        cursor_db = db_lp.cursor()
        Log1 = cursor_db.execute(('''SELECT name FROM info
                                              WHERE email = '{}';
                                               ''').format(session['email'])).fetchone()[0]
        Log2 = cursor_db.execute(('''SELECT surname FROM info
                                               WHERE email = '{}';
                                               ''').format(session['email'])).fetchone()[0]
        fio = Log1 + ' ' + Log2

        # Получаю из базы список email-ов
        Des = cursor_db.execute('''SELECT email FROM history;''').fetchall()
        Des_task = cursor_db.execute('''SELECT email FROM task;''').fetchall()
        des_hi = []
        des_task = []
        # прохожу по списку email-ов
        for i in Des:
            des_hi.append(i[0])
        for i in Des_task:
            des_task.append(i[0])
        print(des_hi)
        print(des_task)
        all_json = {}

        print(set(des_task))
        for i in set(des_task):
            Full_name = cursor_db.execute(('''SELECT full_name FROM task WHERE email = '{}';''').format(i)).fetchall()
            Des1 = cursor_db.execute(('''SELECT status FROM task WHERE email = '{}';''').format(i)).fetchall()
            Des2 = cursor_db.execute(('''SELECT name FROM task WHERE email = '{}';''').format(i)).fetchall()
            Des3 = cursor_db.execute(('''SELECT price FROM task WHERE email = '{}';''').format(i)).fetchall()
            Des4 = cursor_db.execute(('''SELECT description FROM task WHERE email = '{}';''').format(i)).fetchall()
            Des5 = cursor_db.execute(('''SELECT information FROM task WHERE email = '{}';''').format(i)).fetchall()
            Des6 = cursor_db.execute(('''SELECT contact FROM task WHERE email = '{}';''').format(i)).fetchall()
            Des7 = cursor_db.execute(('''SELECT information_meneger FROM task WHERE email = '{}';''').format(i)).fetchall()
            Des8 = cursor_db.execute(('''SELECT contact_meneger FROM task WHERE email = '{}';''').format(i)).fetchall()
            full_name = []
            des1 = []
            des2 = []
            des3 = []
            des4 = []
            des5 = []
            des6 = []
            des7 = []
            des8 = []
            arr01 = []
            arr02 = []
            for j in Full_name:
                full_name.append(j[0])
            for j in Des1:
                des1.append(j[0])
            for j in Des2:
                des2.append(j[0])
            for j in Des3:
                des3.append(j[0])
            for j in Des4:
                des4.append(j[0])
            for j in Des5:
                des5.append(j[0])
            for j in Des6:
                des6.append(j[0])
            for j in Des7:
                des7.append(j[0]) 
            for j in Des8:
                des8.append(j[0])

            for j in range(len(des1)):
                arr01.append(full_name[j])
                arr01.append([des1[j], des2[j], des3[j], des4[j], des5[j], des6[j], des7[j], des8[j]])
                arr02.append(arr01)
                arr01 = []
            #if i == session['email']:
            all_json[i] = arr02
            print(arr02)
        print(all_json)
        with open('static/animation/temp2.json', 'w') as f1:
            json.dump(all_json, f1, indent=7)
        f1.close()      
            
        for i in set(des_hi):
            if i == session['email']:
                # получаю описание по взятому email-у
                Des1 = cursor_db.execute(('''SELECT des FROM history WHERE email = '{}';''').format(i)).fetchall()
                #  получаю цену по взятому email-у
                Des2 = cursor_db.execute(('''SELECT pr FROM history WHERE email = '{}';''').format(i)).fetchall()
                des = []
                for j in Des1:
                    # создаю массив с описаниями
                    des.append(j[0])
                des1 = []
                for j in Des2:
                    # создаю массив с ценами и датами
                    des1.append(j[0])
                for j in des1:
                    k = j.index('(')
                    l = j[:k]
                    summ = summ + int(l)
                    print(l)
                des5 = []
                for j in range(len(des)):
                    # создаю масив с соответсвующими полями из des и des1
                    des6 = [des[j], des1[j]]
                    # создаю общий массив состоящий из масивов
                    des5.append(des6)
                    # создает словарь с индетификаторм email и значением масив
                obj = {i: des5}
                with open('static/animation/temp1.json', 'w') as f:
                    # записывает получившийся словарь в json
                    json.dump(obj, f, indent=2)
                f.close()   
        cursor_db.close()
        db_lp.close()
    return render_template('account.html', Log=fio, Sum=summ, Email=session['email'])


@app.route('/')
def main():
    return render_template('main_page.html')


@app.route('/newpassword', methods=['GET', 'POST'])
def newpassword():
    if request.method == 'POST':
        code1 = str(request.form['code'])
        print(session['code'], code1)
        if code1 == session['code']:
            print('yes')
            session.pop('code', None)
            return redirect(url_for('qu'))
        else:
            session.pop('code', None)
            print('вы мошеник')
    return render_template('code.html')


@app.route('/sent_accept')
def sent_accept():
    session.pop('code', None)
    code = generate(5)
    letter(session['email'], code)
    session['code'] = code
    return redirect(url_for('reg'))


@app.route('/sentps')
def sent():
    session.pop('code', None)
    code = generate(5)
    letter('kuprvvv@gmail.com', code)
    session['code'] = code
    return redirect(url_for('newpassword'))


def generate(length):
    lower_case = "abcdefghiklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    Use_for = lower_case + upper_case
    length_for_pass = length
    code = "".join(random.sample(Use_for, length_for_pass))
    return code


def letter(email, ms):
    with smtplib.SMTP_SSL("smtp.gmail.com") as smtp:
        smtp.login('Helpyrussia@gmail.com', 'jsxs pshp sndf fqok') #https://myaccount.google.com/apppasswords
        smtp.sendmail('kuprvvv@gmail.com', email, msg = ms)


@app.route('/resPas', methods=['GET', 'POST'])
#return redirect(url_for('.re', code = '', codeOld = '', codeNew = '', oldpas = '', newpas1 = '', pos = '', newpas2 = '', emailOld = '', emailNew = ''))
def resPas():
    oldPass1 = ''
    newpas1 = ''
    newpas2 = ''
    code = ''
    email = ''
    if request.method == 'POST':
        if request.form['button'] == 'code':
            oldPass1 = request.form['Ppassword']
            newpas1 = request.form['newPassword']
            newpas2 = request.form['newPassagain']
            email = request.form['Pemail']
            code = generate(5)
            letter(email, code)
        if request.form['button'] == 'Pas':
            code1 = request.form['Pcode']
            db_lp = sqlite3.connect('bases/login_password.db')
            cursor = db_lp.cursor()
            oldpass = cursor.execute(f'''SELECT password FROM login_password
                                                WHERE login = "{session['email']}"''').fetchone()[0]
            oldPass = str(hashlib.sha512(request.form['Ppassword'].encode()).hexdigest())
            code = request.form['Pcode']
            if code1 == code:
                if oldPass == oldpass:
                    newpass = request.form['newPassword']
                    cursor.execute(f'''UPDATE login_password SET Password = "{str(hashlib.sha512(newpass.encode()).hexdigest())}" WHERE Login = "{session['email']}";''')
                    db_lp.commit()
                    return redirect(url_for('account'))
            cursor.close()
            db_lp.close()
    return render_template('resPas.html', Email = email, OldPas = oldPass1, newPas1 = newpas1, newPas2 = newpas2 )
    

@app.route('/resMail', methods=['GET', 'POST'])
def resMail():
    oldEmail = ''
    newEmail = ''
    newEmail1 = ''
    password = ''
    codeOld = ''
    codeNew = ''
    codeOld1 = ''
    codeNew1 = ''
    if request.method == 'POST':
        if request.form['button'] == 'CodeOld':
            codeNew1 = request.form['codeNew1']
            oldEmail = request.form['email']
            newEmail = request.form['newMail']
            password = request.form['passwordMail']
            codeOld = generate(5)
            session.pop('codeOld', None)
            session['codeOld'] = codeOld
            letter(oldEmail, codeOld)
        if request.form['button'] == 'CodeNew':
            codeOld1 = request.form['codeOld1']
            oldEmail = request.form['email']
            newEmail = request.form['newMail']
            password = request.form['passwordMail']
            codeNew = generate(5)
            session.pop('codeNew', None)
            session['codeNew'] = codeNew
            letter(newEmail, codeNew)
        if request.form['button'] == 'Mail':
            oldEmail = request.form['email']
            newEmail = request.form['newMail']
            password = request.form['passwordMail']
            db_lp = sqlite3.connect('bases/login_password.db')
            cursor = db_lp.cursor()
            oldpass = cursor.execute(f'''SELECT password FROM login_password
                                                WHERE login = "{oldEmail}"''').fetchone()[0]
            password = str(hashlib.sha512(password.encode()).hexdigest())
            codeOld1 = request.form['codeOld1']
            codeNew1 = request.form['codeNew1']
            if session['codeOld'] == codeOld1 and session['codeNew'] == codeNew1:
                if oldpass == password:
                    cursor.execute(f'''UPDATE login_password SET login = "{newEmail}" WHERE login = "{oldEmail}";''')
                    cursor.execute(f'''UPDATE info SET login = "{newEmail}" WHERE email = "{oldEmail}";''')
                    cursor.execute(f'''UPDATE task SET login = "{newEmail}" WHERE email = "{oldEmail}";''')
                    cursor.execute(f'''UPDATE history SET login = "{newEmail}" WHERE email = "{oldEmail}";''')
                    db_lp.commit()
                    cursor.close()
                    db_lp.close
                    return redirect(url_for('account'))
                else:
                    cursor.close()
                    db_lp.close()
            else:
                cursor.close()
                db_lp.close()
    return render_template('resMail.html', Email = oldEmail, NewMail = newEmail, MailPas = password, codeOld = codeOld1, codeNew = codeNew1)



@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    email = ''
    newpass1 = ''
    newpass2 = ''
    code = ''
    if request.method == 'POST':
        if request.form['button'] == 'Сode':
            email = request.form['Pemail']
            newpass1 = request.form['newPassword']
            newpass2 = request.form['newPassagain']
            code = generate(5)
            session.pop('code', None)
            session['code'] = code
            letter(email, code)
        if request.form['button'] == 'Pas':
            print(f'code: {session["code"]}')
            code1 = request.form['Pcode']
            if session['code'] == code1:
                newpass1 = request.form['newPassword']
                email = request.form['Pemail']
                db_lp = sqlite3.connect('bases/login_password.db')
                cur = db_lp.cursor()
                cur.execute(f'''UPDATE login_password SET Password = "{str(hashlib.sha512(newpass1.encode()).hexdigest())}" WHERE Login = "{email}";''')
                db_lp.commit()
                cur.close()
                db_lp.close()
                return redirect(url_for('auth'))
            else:  print('error code', code, code1)
    return render_template('forgotPas.html', Email = email, newPas1 = newpass1, newPas2 = newpass2)


@app.route('/qu_admin')
def qu_admin():
    return render_template('qu_admin.html')


@app.route('/admin')
def admin():
    return render_template('admin_account.html')


@app.route('/add_admin')
def add_admin():
    return render_template('add_admin.html')

@app.route('/number')
def number():
    return render_template('number.html')

@app.route('/mail')
def mail():
    return render_template('mail.html')

app.run(debug=True)