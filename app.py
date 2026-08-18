from flask import Flask #devo importare la libreria flask per poter creare un'applicazione web
from flask import render_template

app = Flask(__name__) #definisco l'applicazione web, il parametro __name__ serve a Flask per capire dove si trova l'applicazione

# @app.route("/") #definisco il docoratore per la pagina principale
# def hello_world():#definisco la funzione che verrà eseguita nel browser quando l'utente accede alla pagina principale
#     return "<p>Ciao, questa è la prima app che programmo io</p>"

# @app.route("/info") #definisco il docoratore per la pagina principale
# def info():
#     return "<p>App Lista della Spesa — versione 1.0</p>"

#devo passare elenco di elementi alla pagina web, quindi creo una lista di elementi
items = ["latte", "uova", "pane", "burro", "formaggio", "frutta", "verdura"]   

#devo creare route per la pagina principale, quindi creo una funzione che restituisce il contenuto della pagina principale
@app.route("/") #definisco il docoratore per la pagina principale
def index():
    return render_template("index.html", titolo="Lista della spesa",  items=items)


