from flask import Flask, render_template

app = Flask(__name__)   #ustvarimo instanco

@app.route("/")                             # handler - dekorator. na route registrira funkcijo index
def index():                                # je route brez vsega, zato dobimo na strani tekst
    return render_template("index.html")    # če bi imeli za slashem tekst, ga moramo napisat tudi v vrstico v browserju
                                            # to je kontroler - na poti / se izvede fukncija def
                                           # / je osnovna stran, na katero pridemo. na isti poti imamo lahko en handler
@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/boogle")
def boogle():
    return render_template("/boogle.html")

@app.route("/boogle-login")
def boogle_login():
    return render_template("/boogle_login.html")

@app.route("/fakebook")
def fakebook():
    return render_template("/fakebook.html")

@app.route("/salon")
def salon():
    return render_template("/salon.html")

if __name__ == "__main__":
    app.run(use_reloader=True)   #zaženemo app

"""
MVC
model - podatkovni model aplikacije, odvisen od strani (npr. košarica, naročilo... v spletni banki)
modele modeliramo s classi
kontroler - program, ki povezuje model in view
preverja, če so podatki pravilni. npr struktura nakazila, oblika podatkov...
view - izgled strani. npr. tudi obrazec.
podatki iz obrazca se pošljejo kontrolerju, ki jih vstavi v model

naš html je samo html, ampak damo v funkcijo template, ker ga bomo še razširili
moramo jih dati v mapo html. uporabljali bomo templating engine, ki je mešanica med html in templatom
"""