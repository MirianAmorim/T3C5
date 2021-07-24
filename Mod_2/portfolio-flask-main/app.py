# Criei um gmail novo.

#Configurei os acessos:
   # Permitir aplicativos menos seguros (Ativar): https://myaccount.google.com/lesssecureapps
   # Desbloquear acesso os gmail: https://accounts.google.com/b/2/DisplayUnlockCaptcha
   # Ativar o acesso via IMAP: https://mail.google.com/mail/#settings/fwdandpop
   
# Instalei o flask_mail no terminal

from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
mail_settings = {
   "MAIL_SERVER": 'smtp.gmail.com',
   "MAIL_PORT": 465,
   "MAIL_USE_TLS": False,
   "MAIL_USE_SSL": True,
   "MAIL_USERNAME": 'mi.amorim.work@gmail.com',
   "MAIL_PASSWORD": 'udzssq120664'
}

app.config.update(mail_settings)
mail = Mail(app)

class Contato:
   def __init__ (self, nome, email, mensagem):
      self.nome = nome
      self.email = email
      self.mensagem = mensagem

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
   if request.method == 'POST':
      formContato = Contato(
         request.form['nome'],
         request.form['email'],
         request.form['mensagem']
      )

      msg = Message(
         subject= 'Contato do seu Portfólio', #Assunto do email
         sender=app.config.get("MAIL_USERNAME"), # Quem vai enviar o email, pega o email configurado no app (mail_settings)
         recipients=[app.config.get("MAIL_USERNAME")], # Quem vai receber o email, mando pra mim mesmo, posso mandar pra mais de um email.
         # Corpo do email.
         body=f'''O {formContato.nome} com o email {formContato.email}, te mandou a seguinte mensagem: 
         
               {formContato.mensagem}''' 
         )
      mail.send(msg) #envio efetivo do objeto msg através do método send() que vem do Flask_Mail
   return render_template('send.html', formContato=formContato) # Renderiza a página de confirmação de envio.

if __name__ == '__main__':
   app.run(debug=True)