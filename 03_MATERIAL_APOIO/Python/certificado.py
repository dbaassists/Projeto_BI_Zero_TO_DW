# %%

import warnings
import pandas as pd
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def envia_arquivo_unidades(diretorioArquivo ,fromaddr ,toaddr, nome):

    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = "{0} - Certificado de Participação do Workshop - Bi do Zero Até o DW".format(nome)
    body = "Olá Meu amigo {0}!!\n\nEspero que esteja tudo bem contigo! \n\nQuero expressar minha sincera gratidão pelo seu empenho e dedicação, e principalmente por acreditar no projeto que apresentei a você. \n\nConfesso que nem eu mesmo esperava que o resultado fosse tão promissor quanto foi. Isso só foi possível graças ao seu apoio e contribuição.\n\nAgradeço imensamente pela doação do seu tempo e pela colaboração neste projeto. Seu envolvimento fez toda a diferença.\n\nEstou ansioso para nos reunirmos em breve para enfrentarmos novos desafios juntos!\n\nGrande Abraço, \n\nGabriel Quintella".format(nome)
    msg.attach(MIMEText(body, 'plain')) 
    filename = "Certificado_{0}.pdf".format(nome.replace(' ','_'))
    attachment = open("{0}\Certificado_{1}.pdf".format(diretorioArquivo,nome.replace(' ','_')), "rb")
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, "qiwb hnqt ucvn ehfx") 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()    


# %%

diretorioArquivo = fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\03_MATERIAL_APOIO\Certificado'
fromaddr = "dbaassists@gmail.com"

dados = {
'id':[1,2,3,4,5]
, 'nome':['Daniel Duarte','Edmagno Gomes dos Santos','Mateus Luís Soncin Gazola','Renato Fidelis Ribeiro', 'Wallace Camargo Pereira da Graça']
, 'email':['danielduarte0496@gmail.com', 'edmagnogomes@gmail.com', 'magazola06@gmail.com','fidelisrenato8@gmail.com','wallacecpdg@gmail.com']
#, 'email':['dbaassists@gmail.com', 'dbaassists@gmail.com', 'dbaassists@gmail.com','dbaassists@gmail.com','dbaassists@gmail.com']
}

df = pd.DataFrame(dados)

for indice, linha in df.iterrows():

    nome = linha['nome']

    email = linha['email']

    print(nome , ' - ' , email)

    envia_arquivo_unidades(diretorioArquivo ,fromaddr ,email, nome)

# %%
