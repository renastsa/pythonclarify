import re #biblioteca de procura e padronização de regex
import os
import smtplib
import openpyxl
import email    
import pywhatkit
from email.message import EmailMessage
from time import sleep
import pandas as pd

import pywhatkit as kit

class ToDO:

    def iniciar(self):
        # self.lista_tarefas = []
        # self.lista_datas = []
        # self.email_destino()
        # self.menu()
        # self.criar_planilha() 
        # sleep(1)
        # self.enviar_email()
        self.Enviar_whats() 
   
    def email_destino(self):
        while True:
            self.email = str(input('E-mail de destino: ')).lower()

            padrao_email = re.search(
            '^[a-z0-9._]+@[a-z0-9]+.[a-z]+(.[a-z]+)?$', self.email #no parenteses é opcional, ja que muitos emails terminam em .com
            )

            if padrao_email:
                print('Email válido!')
                break
            else:
                print('Email inválido')

    def menu(self):
        while True:
            menu_principal = int(input('''
                MENU PRINCIPAL
                [1] CADASTRAR
                [2] VISUALIZAR
                [3] SAIR
                Opção: '''))
            
            match menu_principal:
                case 1: self.cadastrar()
                case 2: self.visualizar()
                case 3: break
                case _: print("\nopção inválida") #quando for so uma instrução no mesmo bloco pode ficar na mesma linha

    def cadastrar(self):

        while True:
            self.tarefa = str(input('Digite uma tarefa ou [S] para sair:')).capitalize()

            if self.tarefa == 'S':
                break
            else: 
                self.lista_tarefas.append(self.tarefa) #criar arquivo pedindo para ele tentar criar arquivo
                try:
                        with open('./SRC/TAREFAS/historico_tarefas.txt','a', encoding='utf8') as arquivo: 
                             arquivo.write(f'{self.tarefa}\n') #copiar caminho sempre vem com contrabarra, sempre mudar a barra
#o modo 'a' cria o arquivo caso nao exista e caso exista ele segue alimentando o arquivo existente
                    #utf8 é sempre para reconhecer caracteres especiais como ç etc
             
                except FileNotFoundError as e:
                        print(f'Erro:{e}')

    def visualizar(self):
        try:
              with open('./SRC/TAREFAS/historico_tarefas.txt', 'r', encoding='utf8') as arquivo:
                   print(arquivo.read())
        except FileNotFoundError as e:
            print(f'Erro:{e}')

    def criar_planilha(self):
        if len(self.lista_tarefas) > 0:
            try:
                df = pd.DataFrame({
                    'Tarefas': self.lista_tarefas
                    })
                
                self.nome_arquivo = str(input('Nome do arquivo: ')).lower()

                if self.nome_arquivo[-5:] == '.xlsx':
                    df.to_excel(f'./SRC/TAREFAS/{self.nome_arquivo}', index=False)
                         
                else:
                    df.to_excel(f'./SRC/TAREFAS/{self.nome_arquivo}.xlsx', index =False)    
                print('\nPlanilha criada com sucesso.')
            
            except Exception as e:
                print(f'Erro:{e}')
        else:
            print('\nLista de tarefas vazia.')    

    def enviar_email(self):
        endereco = 'renatatomazxd@gmail.com'
        with open('./SRC/Senha/senha.txt', encoding='utf8') as arquivo:
            s = arquivo.readlines()
        senha= s[0]

        msg = EmailMessage()
        msg['From'] = endereco
        msg['To'] = self.email
        msg['Subject'] = 'ooo zé, chegou a planilha!'
        msg.set_content(
            'Clarify, me dê todos os módulos'
        )
        arquivos = [f'./SRC/TAREFAS/{self.nome_arquivo}.xlsx']

        for arquivo in arquivos:
            with open(arquivo, 'rb') as arq:
                dados = arq.read()
                nome_arquivo = arq.name
            
            msg.add_attachment(
                dados,
                maintype='application',
                subtype='octet-stream',
                filename=nome_arquivo
            )
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(endereco, senha, initial_response_ok=True)
        server.send_message(msg)
        print('Email enviado com sucesso.')

    def Enviar_whats(self):
        try:
            numero_destino = '+5511970974321'
            mensagem = "tinhamu, teste do python"

            kit.sendwhatmsg_instantly(numero_destino, mensagem, wait_time=40)
            print(f'Whats enviado')
        except Exception as e:
            print(f"Erro:{e}")    
### regex é a expressao para padroes tanto faz para qual dado      
          

start = ToDO()
start.iniciar()
