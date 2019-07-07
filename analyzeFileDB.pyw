import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PASSWORD = ''
EMAIL    = ''

try:
    unityAndFile = open('unityAndFile.txt', 'r').readlines()
except:
    unityAndFile[0] = "Undefined"
#time.sleep(10)
def sendEmail(file, unity = unityAndFile[0]):
    msg = MIMEMultipart()
    message = """
      <body> 
        <div style="
        
        font-family: Arial, Helvetica, sans-serif;
                width: 510px;
                height: auto;
                padding: 30px;
                margin: 0 auto;
        ">
            <h1
                style="
                width: 100%;
                text-align: center;
                background: rgb(113, 218, 120);
                border-radius: 5px;
                color: #fff;
                height: 40px;
                "
            >{}</h1>
            <hr>
            <section
            style="
             margin-top: 50px;
                height: 100px;
                font-size: 15px;
                color: #000;
                "
            >
                    Precisa de Atenção.. <br>
                    Atualmente o arquivo esta com:
            </section>
            <foote>"servercontrolldb@gmail.com"
                    <div style="
                    margin: 0 auto;
                width: 500px;
                background: rgb(209, 100, 100);
                font-weight: bold;
                color: #fff;
                text-align: center;
                font-size: 25pt;
                ">
                            {} MB
                    </div>
            </footer>
        </div>    
    </body>
    """.format(unity, str(file)[0:3])
    # setup the parameters of the message
    msg['From'] = EMAIL
    msg['Subject'] = "Loja {} Clean DB".format(unityAndFile[0])
    # add in the message body
    msg.attach(MIMEText(message, 'html'))
        #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], PASSWORD)
    # send the message via the server.
    emails = open('email.txt','r').readlines()

    for email in emails:
        server.sendmail(msg['From'], email, msg.as_string())

    server.quit()

def getSizeOfFile():
    # AGUARANDO 24 HORAS PARA A PROXIMA VERIFICAÇÃO
    time.sleep(86400)
    Sizefile = os.path.getsize(unityAndFile[1])
    # 275530668 TAMANHO DO ARQUIVO EM KB
    sendEmail(Sizefile) if Sizefile >= 275530668 else 'pass'

while True:
    getSizeOfFile()
