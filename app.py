from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '123456'  # Necesaria para usar sesiones

# Datos de usuario simulados (normalmente estarían en una base de datos)
users = {
    "Rodrigo": "pass123",
    "Joel": "pass456",
    "Alastor": "pass789",
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verifica qué usuario y contraseña está recibiendo
        print(f"Usuario ingresado: {username}")
        print(f"Contraseña ingresada: {password}")

        # Verificamos si el usuario y contraseña son correctos
        if username in users and users[username] == password:
            session['username'] = username  # Guardamos el usuario en la sesión
            print("Login exitoso!")  # Verifica si el login es exitoso
            return redirect(url_for('welcome'))  # Redirigimos a la página de bienvenida
        else:
            print("Login fallido, credenciales incorrectas.")  # Mensaje de fallo
            return render_template('login.html', error='Usuario o contraseña incorrectos')

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username']
        return render_template('welcome.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Eliminamos la información de sesión
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)