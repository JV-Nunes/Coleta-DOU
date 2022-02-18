
import pandas as pd
import basedosdados as bd
import datetime
import slack
import os
from pathlib import Path
from dotenv import load_dotenv


from vars import BILLING_ID
from getters import GetDou
from calculators import Calculator

load_dotenv(dotenv_path='.env')

get = GetDou()
calc = Calculator()

today, yesterday, day_before_yesterday = calc.get_dates()
all_dates = list(today, yesterday, day_before_yesterday)

# To load the dataset with basedosdados api:
df = bd.read_table(dataset_id='br_imprensa_nacional_dou', 
            table_id='secao_1',
            billing_project_id=BILLING_ID)

pd.set_option('display.max_colwidth', None)


for date in all_dates:
    collection = get.extract_filtered_section1(df, date, filter)
    if collection != -1:
        break

all_text = []
title = []
ementa =[]

for item in collection['texto_principal']: all_text.append(str(item))

for item in collection['titulo']: title.append(str(item))
    
for item in collection['ementa']: ementa.append(str(item))

# # Enviando a mensagem ao Slack



slack_token = os.environ["SLACK_TOKEN"]
client = slack.WebClient(token=slack_token)

for i in range(0,len(lista)):
    client.chat_postMessage(channel='#legislative-affairs',text=titulo[i])
    client.chat_postMessage(channel='#legislative-affairs',text=ementa[i])
  


#RODAR CASO QUEIRA EXECUTAR O TEXTO COMPLETO
for i in range(0,len(lista)):
    client.chat_postMessage(channel='#texto-completo',text=titulo[i])
    client.chat_postMessage(channel='#texto-completo',text=lista[i])
    client.chat_postMessage(channel='#texto-completo',text='::::::::::::::::::::::::::::::::::::::::::')

