#!/usr/bin/env python
# coding: utf-8

# # Importando os dados do DOU e aplicando filtro

# In[1]:


#Caso necessário, instalar os seguintes pacotes no ambiente de execução:
get_ipython().system('pip install basedosdados')
get_ipython().system('pip install slackclient')
get_ipython().system('pip install python-dotenv')


# In[2]:


import pandas as pd
import basedosdados as bd
# Para carregar o dado direto no pandas
df = bd.read_table(dataset_id='br_imprensa_nacional_dou', 
            table_id='secao_1',
            billing_project_id=<PROJECT ID FROM GCP>)


# In[ ]:


pd.set_option('display.max_colwidth', None)


# In[ ]:


import datetime

today = datetime.date.today()

hoje = today.strftime("%Y-%m-%d")
ontem_date = today - datetime.timedelta(days=1)
ontem = str(ontem_date)
anteontem = str(ontem_date - datetime.timedelta(days=1))


# In[ ]:


def secao_1_inteira(data):
  df1=df[df['data_publicacao'].astype(str).str.contains(data,regex=True,na=False)]
  if (len(df1) != 0):
    return df1
  else: 
    print('Ainda não temos a publicação deste dia!') 


# In[ ]:


def secao_1_filtro(data):
  df1=df[df['data_publicacao'].astype(str).str.contains(data,regex=True,na=False)]
  if (len(df1) != 0):
    #INSERIR OS FILTROS DESEJADOS NO REGEX ABAIXO:
    return df1[df1['titulo'].str.contains('DECRETO|MEDIDA PROVISÓRIA|LEI|EMENDA|CONSTITUIÇÃO',regex=True,na=False)] 
  df1=df[df['data_publicacao'].astype(str).str.contains(ontem,regex=True,na=False)]
  check=df1[df1['titulo'].str.contains('DECRETO|MEDIDA PROVISÓRIA|LEI|EMENDA|CONSTITUIÇÃO',regex=True,na=False)]
  if (len(check) !=0):
      return check    
  return print('Verificação concluída: Nenhuma lei publicada')  


# In[ ]:


coleta=secao_1_filtro(hoje)


# In[ ]:


lista=[]
for item in coleta['texto_principal']:
    lista.append(str(item))
titulo=[]
for item in coleta['titulo']:
    titulo.append(str(item))
ementa =[]
for item in coleta['ementa']:
    ementa.append(str(item))


# # Enviando a mensagem ao Slack

# In[ ]:


import slack
import os
from pathlib import Path
from dotenv import load_dotenv


# In[ ]:


load_dotenv(dotenv_path='.env')
slack_token = os.environ["SLACK_TOKEN"]
client = slack.WebClient(token=slack_token)

for i in range(0,len(lista)):
    client.chat_postMessage(channel='#legislative-affairs',text=titulo[i])
    client.chat_postMessage(channel='#legislative-affairs',text=ementa[i])
  


# In[ ]:


#RODAR CASO QUEIRA EXECUTAR O TEXTO COMPLETO
for i in range(0,len(lista)):
    client.chat_postMessage(channel='#texto-completo',text=titulo[i])
    client.chat_postMessage(channel='#texto-completo',text=lista[i])
    client.chat_postMessage(channel='#texto-completo',text='::::::::::::::::::::::::::::::::::::::::::')

