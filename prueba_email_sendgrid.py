import os
from flask import Flask
from flask import request
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

app= Flask(__name__)

load_dotenv()

@app.route('/e-mail')
def mail():

    destino=request.args.get("correo_destino")
    asunto = request.args.get("asunto")
    mensaje = request.args.get("contenido")

    message = Mail(
        from_email = 'fadedevs22@gmail.com',
        to_emails=destino,
        subject=asunto,
        html_content=mensaje)
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY3'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return "Correo enviado exitosamente!"
    except Exception as e:
        print(e.message)
        return "error, el correo no fue enviado"

if __name__ == '__main__':
    app.run(debug=True)