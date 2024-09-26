#!/usr/bin/env python
# encoding: utf-8
import smtplib
import socket
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Validação de argumentos
if len(sys.argv) < 3:
    print("Uso: python script.py <nome> <ip>")
    sys.exit(1)

# Dados fornecidos via linha de comando
nome = sys.argv[1]
ip = sys.argv[2]

# Leitura do sistema operacional
adress_os = '/etc/issue.net'
if os.path.exists(adress_os):
    with open(adress_os) as f:
        sistema_operacional = f.readline().strip()
else:
    sistema_operacional = "Desconhecido"

# Data e hora da instalação
data_instalacao = datetime.now()
dia = data_instalacao.strftime('%d')
mes = data_instalacao.strftime('%m')
ano = data_instalacao.strftime('%Y')
hora = data_instalacao.strftime('%H')
minuto = data_instalacao.strftime('%M')
segundo = data_instalacao.strftime('%S')

# Composição do e-mail
msg = MIMEMultipart('alternative')
msg['Subject'] = "INSTALACAO DO SSHPLUS"
msg['From'] = os.getenv('EMAIL_SENDER', 'www.infinitenet.net@gmail.com')  # Use variáveis de ambiente
msg['To'] = os.getenv('EMAIL_RECIPIENT', 'infinitenet.net@gmail.com')

texto_email = f"""
<html>
<head></head>
<body>
<b><i>Olá! Crazy</i></b>
<br></br>
<b><i>SEU SCRIPT FOI INSTALADO EM UM VPS<i></b>
<br></br>
<b>══════════════════════════</b><br/>
<b><i>INFORMAÇÕES DA INSTALAÇÃO<i></b><br/>
<b><font color="blue">IP:</b></font> <i><b><font color="red">{ip}</font></b></i><br/>
<b><font color="blue">Nome:</b></font> <i><b><font color="red">{nome}</font></b></i><br/>
<b><font color="blue">Sistema:</b></font> <i><b><font color="red">{sistema_operacional}</font></b></i><br/>
<b>══════════════════════════</b><br/>
<b><i>DATA DA INSTALAÇÃO</i></b><br/>
<b><font color="blue">Dia:</b></font> <i><b><font color="red">{dia}</font></b></i><br/>
<b><font color="blue">Mês:</b></font> <i><b><font color="red">{mes}</font></b></i><br/>
<b><font color="blue">Ano:</b></font> <i><b><font color="red">{ano}</font></b></i><br/>
<b>══════════════════════════</b><br/>
<b><i>HORA DA INSTALAÇÃO</i></b><br/>
<b><font color="blue">Hora:</b></font> <i><b><font color="red">{hora}</font></b></i><br/>
<b><font color="blue">Minutos:</b></font> <i><b><font color="red">{minuto}</font></b></i><br/>
<b><font color="blue">Segundos:</b></font> <i><b><font color="red">{segundo}</font></b></i><br/>
<b>══════════════════════════</b><br/>
<b><i><font color="#00FF00">By: Alves S.A</i></b></br></p>
</body>
</html>
"""

msg.attach(MIMEText(texto_email, 'html'))

# Envio do e-mail com tratamento de exceções
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # Utilize variáveis de ambiente para evitar expor credenciais
    email_sender = os.getenv('EMAIL_SENDER', 'www.infinitenet.net@gmail.com')
    email_password = os.getenv('EMAIL_PASSWORD', 'Gvt@946894334')

    server.login(email_sender, email_password)
    server.sendmail(email_sender, msg['To'], msg.as_string())
    server.quit()
    print("E-mail enviado com sucesso.")
except Exception as e:
    print(f"Falha ao enviar o e-mail: {e}")
