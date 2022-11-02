from shareplum import Site
from requests_ntlm import HttpNtlmAuth
import pandas as pd
from shareplum import Office365

authcookie = Office365('https://*server*.sharepoint.com', username='usuário do sharepoint', password='senha').GetCookies()
site = Site('url do site Sharepoint', authcookie=authcookie)

new_list = site.List('Adicionar o nome da lista de destino')
my_data =[{"nome": "Guilherme"}] #DADOS A SER ENVIADOS PARA A LISTA
new_list.UpdateListItems(data=my_data, kind='New') #ENVIANDO OS DADOS PARA A LISTA