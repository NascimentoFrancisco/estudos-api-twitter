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
