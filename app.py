from flask import Flask #devo importare la libreria flask per poter creare un'applicazione web

app = Flask(__name__) #definisco l'applicazione web, il parametro __name__ serve a Flask per capire dove si trova l'applicazione

@app.route("/") #definisco il docoratore per la pagina principale
def hello_world():#definisco la funzione che verrà eseguita nel browser quando l'utente accede alla pagina principale
    return "<p>Ciao, questa è la prima app che programmo io</p>"