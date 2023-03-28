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

print("Content-type: text/html; charset=utf-8")
print("\n")
print("<html><head><title>Post Example</title></head><body>")
with open('bd.txt', 'r') as f:
    while True:
        autor = f.readline()
        mensagem = f.readline()
        hora = f.readline()
        if not hora:
            break
        print(autor + "<br>")
        print(mensagem + "<br>")
        print(hora + "<br>")
        print("<hr>")
print("<a href='../index.html'>Voltar</a>")
print("</body></html>")

