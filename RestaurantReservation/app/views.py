import datetime
import sys

from app import app, db
from flask import render_template, flash, redirect, session, g, request, jsonify,url_for

from .forms import ReservationForm, ShowReservationsOnDateForm, AddTableForm
from .controller import create_reservation
from .models import Mesa, Reservacion, User


# Time Display: book table in fixed hours when the restaurant operates.
RESTAURANT_OPEN_TIME = 10
RESTAURANT_CLOSE_TIME = 22

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Reservacion para un restaurante")

@app.route('/users/create', methods=['POST','GET'])
def create_user():
    error1= False
    error2 = False
    error3 = False
    error = False
    response={}
    try:
        username = request.get_json()['user']#simula json.loads
        email = request.get_json()['email']
        password = request.get_json()['password']
        user_data = User.query.filter_by(username=username).first()
        user_email = User.query.filter_by(email=email).first()

        #Determinando errores
        if(len(username)==0 or len(password)==0 or len(email)==0 or len(username)>20 or len(password)>8):
            raise Exception
        if (user_data is not None) or (user_email is not None):
            raise Exception
        #Determinando errores

        usuarios = User(username=username, email=email,password=password)
        db.session.add(usuarios)
        db.session.commit()
        response['user'] = usuarios.username
        response['email'] = usuarios.email
        response['password'] = usuarios.password
    except Exception:
        if(len(username)==0):
            error1= True
            response['error_message1']= "Ingrese un usuario"
        if(len(password)==0):
            error2= True
            response['error_message2']= "Ingrese una contraseña"
        if(len(email)==0):
            error3= True
            response['error_message3']= "Ingrese un correo válido"
        
        if(len(username)>20):
            error1= True
            response['error_message1']= "El nombre del usuario debe tener un máximo de 20 caracteres"
        if(len(password)>8):
            error2 = True
            response['error_message2']= "La contraseña debe tener un máximo de 8 caracteres"

        if (user_data is not None) or (user_email is not None):
            error = True
            response['error_message'] = "El usuario o correo ya existe. Inicie sesion"

        print(sys.exc_info())
        db.session.rollback()
    finally:
        db.session.close()        

    response['error1'] = error1
    response['error2'] = error2
    response['error3'] = error3
    response['error'] = error
    return jsonify(response)


@app.route('/users/login', methods=['POST','GET'])
def login_user():
    exist = True
    response={}
    try:
        username = request.get_json()['user']
        password = request.get_json()['password']
        user_data = User.query.filter_by(username=username).first()
        if user_data is None:
            raise Exception
        elif not (password==user_data.password):
            raise Exception

        
    except Exception:
        exist = False
    finally:
        db.session.close()
    if not exist:
        response['error_message']= "Usuario o contraseña incorrecta"
    
    response['exist'] = exist

    return jsonify(response)    


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    return render_template("registration.html") 


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route('/reservation_status', methods=['GET', 'POST'])
def reservation_status():
    form = ReservationForm()
    if form.validate_on_submit():
        if form.reservacion_datetime.data < datetime.datetime.now():
            flash("No puedes reservar fechas en el pasado")
            return redirect('/reservation_status')
        fecha_reservacion = datetime.datetime.combine(form.reservacion_datetime.data.date(), datetime.datetime.min.time())
        if form.reservacion_datetime.data < fecha_reservacion + datetime.timedelta(hours=RESTAURANT_OPEN_TIME) or \
        form.reservacion_datetime.data > fecha_reservacion + datetime.timedelta(hours=RESTAURANT_CLOSE_TIME):
            flash("El restaurante esta cerrado en esa hora!")
            return redirect('/reservation_status')
        reservacion = create_reservation(form)
        if reservacion:
            flash("La reservacion ha sido creada!")
            return redirect('/index')
        else:
            flash("Esa hora ya ha sido tomada! Intente otra vez")
            return redirect('/reservation_status')
    return render_template('reservation_status.html', title="Hacer Reservacion", form=form)

@app.route('/show_tables', methods=['GET', 'POST'])
def show_tables():
    form = AddTableForm()

    if form.validate_on_submit():
        mesa = Mesa(capacidad=int(form.mesa_capacidad.data))
        db.session.add(mesa)
        db.session.commit()
        flash("La mesa ha sido creada!")
        return redirect('/show_tables')

    mesas = Mesa.query.all()
    return render_template('show_tables.html', title="Mesas", mesas=mesas, form=form)

@app.route('/show_reservations', methods=['GET', 'POST'])
@app.route('/show_reservations/<reservation_date>', methods=['GET', 'POST'])
def show_reservations(fecha_reservacion = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")):
    form = ShowReservationsOnDateForm()
    if form.validate_on_submit():
        res_date = datetime.datetime.strftime(form.fecha_reservacion.data, "%Y-%m-%d")
        return redirect('/show_reservations/' + res_date)
    res_date = datetime.datetime.strptime(fecha_reservacion, "%Y-%m-%d")
    reservaciones = Reservacion.query.filter(Reservacion.hora_reservacion >= res_date,
                                            Reservacion.hora_reservacion < res_date + datetime.timedelta(days=1)).all()

    return render_template('show_reservations.html', title="Reservaciones", reservaciones=reservaciones, form=form)

@app.route('/admin')
def admin():
    return render_template('admin.html', title="Admin")

