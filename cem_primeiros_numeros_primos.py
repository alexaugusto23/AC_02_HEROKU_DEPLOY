import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')

def numero_primos():
    primos=""
    qtdprimos=0
    
    for n in range(0,542):
        divisores=0
        for div in range(1,n+1):
            if n % div == 0:
                divisores += 1 
        if divisores == 2:
            qtdprimos +=1
            primos = primos + str(n) + " "
            if qtdprimos % 10 == 0:
                primos=primos + "= " + str(qtdprimos) + "<br>" 
    
    return ("<html style='background-color:orange;'>"+"<center><h1>Seja Bem-Vindo.</h1><center>"+"<a>"+
    "<center><h2>Aos 100 números primos.</h2><center>"+
    "<br>"+"<center>"+primos+"<center>"+"<br>"+
    "<center><p>Desenvolvido por: Alexsandro Augusto Ignácio.</p><center>"+"</html>")   

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
