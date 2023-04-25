#!/usr/bin/env python3
#coding: utf8
import os, cgi
from datetime import datetime

def escrever_arquivo(texto, nome_arquivo):
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(texto)

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        return arquivo.read()

form = cgi.FieldStorage()
author = "Autor: "+ form["autor"].value+'\n'
message = "Mensagem: "+ form["mensagem"].value+'\n'
now = datetime.now()
http_date = now.strftime('%a, %d %b %Y %H:%M:%S GMT')

escrever_arquivo(author, "bd.txt")
escrever_arquivo(message, "bd.txt")
escrever_arquivo(f'{http_date}\n', "bd.txt")

str = ler_arquivo("bd.txt")

data = []

print("Content-type: text/html; charset=utf-8")
print("\n")
print("<html><head><title>Post Example</title></head><body>")
print("<form method='POST' action='http://10.65.215.64:8080/cgi-bin/blog.py'>")
print("Autor: <br />")
print("<input type='text' size='64' name='autor' value='--autor--' /><br /><br />")
print("Mensagem: <br />")
print("<textarea rows='3' cols='46' name='mensagem'>--mensagem--</textarea><br /><br />")
print("<input type='submit' /> <input type='reset' />")
print("</form>")
with open('bd.txt', 'r') as f:
    while True:
        autor = f.readline()
        mensagem = f.readline()
        hora = f.readline()
        val = dict(autor = autor,mensagem=mensagem,hora=hora)
        data.append(val) 
        if not hora:
            break
data.reverse()
for val in data:
    print(val['autor'] + "<br>")
    print(val['mensagem'] + "<br>")
    print(val['hora'] + "<br>")
    print("<hr>")
print("<a href='../index.html'>Voltar</a>")
print("</body></html>")

