import tweepy
import configparser
import pandas as pd

#Lendo as configurações de login, que estão em um arqui do tipo .ini, para uso da API
config = configparser.ConfigParser()
config.read('config.ini')

#Salvando as informaões de autenticação em variáveis constantes
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secert = config['twitter']['access_token_secert']

#Atenticação
autenticacao = tweepy.OAuthHandler(api_key,api_key_secret)
autenticacao.set_access_token(access_token,access_token_secert)

#Conectando na API com os dados de autenticação
api = tweepy.API(autenticacao)

#Esta linha de comando irá pegar os tweets da linhado tempo e armazenará na variável 
public_twetts = api.home_timeline()

#Printando o texto do primeiro tweet
print(public_twetts[0].text)

#Organizndo os dados dos tweets obtidos
columns = ['Time','User','Tweet']
dados = []
for tweet in public_twetts:
                #Data de criação  / Usuário que fez o tweet /texto do twet
    dados.append([tweet.created_at, tweet.user.screen_name, tweet.text])

#criando um data_frame
data_frame = pd.DataFrame(dados,columns=columns)

#Criando um arquivo csv com os tweets obtidos 
data_frame.to_csv('tweets.csv')
