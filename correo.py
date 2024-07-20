from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración del servidor de correo
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tu_email@example.com'
app.config['MAIL_PASSWORD'] = 'tu_password'

mail = Mail(app)

@app.route('/enviar-formulario', methods=['POST'])
def enviar_formulario():
    nombre = request.form['name']
    email = request.form['email']
    telefono = request.form['phone']
    servicio = request.form['service']
    mensaje = request.form['message']

    # Crear el mensaje de correo electrónico
    msg = Message('Nuevo mensaje de contacto',
                  sender='tu_email@example.com',
                  recipients=['tu_email@example.com'])
    msg.body = f"""
    Nombre: {nombre}
    Email: {email}
    Teléfono: {telefono}
    Servicio: {servicio}
    Mensaje:
    {mensaje}
    """
    # Enviar el correo electrónico
    mail.send(msg)

    return 'Formulario enviado correctamente'

if __name__ == '__main__':
    app.run(debug=True)
