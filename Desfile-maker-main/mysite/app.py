from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template,json,redirect
#from flask.wrappers import Response
#import git
from datetime import datetime
import os
import time

os.environ["TZ"] = "America/Recife"
time.tzset()

header_key = '*'

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Recnplay2022:2507phph@Recnplay2022.mysql.pythonanywhere-services.com/Recnplay2022$default'
db = SQLAlchemy(app)

class votos(db.Model):
    id_voto = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(20))
    hora = db.Column(db.Time)
    nome_modelo = db.Column(db.String(20),nullable=False)

    def to_json(self):
        return {"id": self.id_voto,"data": self.data, "hora": self.hora, "nome_modelo": self.nome_modelo }

class curtidas(db.Model):
    id_curtida = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(20))
    hora = db.Column(db.Time)
    nome_modelo = db.Column(db.String(20),nullable=False)

    def to_json(self):
        return {"id": self.id_curtida,"data": self.data, "hora": self.hora, "nome_modelo": self.nome_modelo}


###Rotas

@app.route('/galeria')
def galeria():
    return render_template("galeria.html")

@app.route('/look1')
def look1():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play1"))
        return render_template("look1.html", curtida=curtido.count() )
    except :
        return render_template("look1.html", curtida=" " )

@app.route('/look2')
def look2():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play2"))
        return render_template('look2.html', curtida=curtido.count())
    except :
        return render_template('look2.html', curtida=" ")

@app.route('/look3')
def look3():
    try:
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play3"))
        return render_template('look3.html', curtida=curtido.count())
    except :
        return render_template('look3.html', curtida=" ")

@app.route('/look4')
def look4():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play4"))
        return render_template('look4.html', curtida=curtido.count())
    except :
        return render_template('look4.html', curtida=" ")

@app.route('/look5')
def look5():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play5"))
        return render_template('look5.html', curtida=curtido.count())
    except :
        return render_template('look5.html', curtida=" ")

@app.route('/look6')
def look6():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play6"))
        return render_template('look6.html', curtida=curtido.count())
    except :
        return render_template('look6.html', curtida=" ")


@app.route('/look7')
def look7():
    try:
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play7"))
        return render_template('look7.html', curtida=curtido.count())
    except :
        return render_template('look7.html', curtida=" ")

@app.route('/look8')
def look8():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play8"))
        return render_template('look8.html', curtida=curtido.count())
    except :
        return render_template('look8.html', curtida=" ")

@app.route('/look9')
def look9():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play9"))
        return render_template('look9.html', curtida=curtido.count())
    except :
        return render_template('look9.html', curtida=" ")

@app.route('/look10')
def look10():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play10"))
        return render_template('look10.html', curtida=curtido.count())
    except :
        return render_template('look10.html', curtida=" ")

@app.route('/look11')
def look11():
    try:
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play11"))
        return render_template('look11.html', curtida=curtido.count())
    except :
        return render_template('look11.html', curtida=" ")


@app.route('/cardin')
def cardin():
    setamodeloFuncao( "janela" )
    return render_template("cardin.html")

@app.route('/sobrenos')
def sobre():
    setamodeloFuncao( "colar" )
    return render_template("sobrenos.html")

@app.route('/votacao')
def vote():
    setamodeloFuncao( "olhos" )
    return render_template("votacao.html")

@app.route('/arduino')
def arduino():
    return render_template("arduino.html")

@app.route('/')
def principal():
    setamodeloFuncao( "todos" )
    return render_template("principal.html")


@app.route('/voto', methods = ['GET','POST'])
def inserir():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("M01")
            novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")
    else : # se o methodo for GET ou outro
        try :
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")


@app.route('/voto2', methods = ['GET','POST'])
def inserir2():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("M02")
            novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")
    else : # se o methodo for GET ou outro
        try :
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")

@app.route('/voto3', methods = ['GET','POST'])
def inserir3():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("M03")
            novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")
    else : # se o methodo for GET ou outro
        try :
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")

@app.route('/voto4', methods = ['GET','POST'])
def inserir4():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("M04")
            novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")
    else : # se o methodo for GET ou outro
        try :
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")

@app.route('/voto5', methods = ['GET','POST'])
def inserir5():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("M05")
            novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")
    else : # se o methodo for GET ou outro
        try :
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")

@app.route('/voto6', methods = ['GET','POST'])
def inserir6():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("M06")
            novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")
    else : # se o methodo for GET ou outro
        try :
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")

@app.route('/voto7', methods = ['GET','POST'])
def inserir7():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("M07")
            novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")
    else : # se o methodo for GET ou outro
        try :
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")

@app.route('/voto8', methods = ['GET','POST'])
def inserir8():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("M08")
            novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")
    else : # se o methodo for GET ou outro
        try :
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")

@app.route('/voto9', methods = ['GET','POST'])
def inserir9():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("M09")
            novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")
    else : # se o methodo for GET ou outro
        try :
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")

@app.route('/voto10', methods = ['GET','POST'])
def inserir10():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("M10")
            novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")
    else : # se o methodo for GET ou outro
        try :
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")

@app.route('/voto11', methods = ['POST'])
def inserir11():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("M11")
            novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")
    else : # se o methodo for GET ou outro
        try :
            return render_template("votacao.html")
        except :
            return render_template("votacao.html")

@app.route('/curtida', methods = ['GET','POST'])
def curtir1():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play1")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play1"))
            return render_template("look1.html", curtida=curtido.count() )
        except :
            return render_template("look1.html", curtida=" " )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play1"))
            return render_template("look1.html", curtida=curtido.count() )
        except :
            return render_template("look1.html", curtida=" " )


@app.route('/curtida2', methods = ['GET','POST'])
def curtir2():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play2")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play2"))
            return render_template("look2.html", curtida=curtido.count() )
        except :
            return render_template("look2.html", curtida=" " )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play2"))
            return render_template("look2.html", curtida=curtido.count() )
        except :
            return render_template("look2.html", curtida=" " )

@app.route('/curtida3', methods = ['GET','POST'])
def curtir3():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play3")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play3"))
            return render_template("look3.html", curtida=curtido.count() )
        except :
            return render_template("look3.html", curtida=" " )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play3"))
            return render_template("look3.html", curtida=curtido.count() )
        except :
            return render_template("look3.html", curtida=" " )

@app.route('/curtida4', methods = ['GET','POST'])
def curtir4():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play4")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play4"))
            return render_template("look4.html", curtida=curtido.count() )
        except :
            return render_template("look4.html", curtida=" " )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play4"))
            return render_template("look4.html", curtida=curtido.count() )
        except :
            return render_template("look4.html", curtida=" " )

@app.route('/curtida5', methods = ['GET','POST'])
def curtir5():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play5")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play5"))
            return render_template("look5.html", curtida=curtido.count() )
        except :
            return render_template("look5.html", curtida=" " )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play5"))
            return render_template("look5.html", curtida=curtido.count() )
        except :
            return render_template("look5.html", curtida=" " )

@app.route('/curtida6', methods = ['GET','POST'])
def curtir6():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play6")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play6"))
            return render_template("look6.html", curtida=curtido.count() )
        except :
            return render_template("look6.html", curtida=" " )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play6"))
            return render_template("look6.html", curtida=curtido.count() )
        except :
            return render_template("look6.html", curtida=" " )

@app.route('/curtida7', methods = ['GET','POST'])
def curtir7():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play7")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play7"))
            return render_template("look7.html", curtida=curtido.count() )
        except :
            return render_template("look7.html", curtida=" " )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play7"))
            return render_template("look7.html", curtida=curtido.count() )
        except :
            return render_template("look7.html", curtida=" " )

@app.route('/curtida8', methods = ['GET','POST'])
def curtir8():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play8")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play8"))
            return render_template("look8.html", curtida=curtido.count() )
        except :
            return render_template("look8.html", curtida=" " )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play8"))
            return render_template("look8.html", curtida=curtido.count() )
        except :
            return render_template("look8.html", curtida=" " )

@app.route('/curtida9', methods = ['GET','POST'])
def curtir9():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play9")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play9"))
            return render_template("look9.html", curtida=curtido.count() )
        except :
            return render_template("look9.html", curtida=" " )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play9"))
            return render_template("look9.html", curtida=curtido.count() )
        except :
            return render_template("look9.html", curtida=" " )

@app.route('/curtida10', methods = ['GET','POST'])
def curtir10():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play10")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play10"))
            return render_template("look10.html", curtida=curtido.count() )
        except :
            return render_template("look10.html", curtida=" " )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play10"))
            return render_template("look10.html", curtida=curtido.count() )
        except :
            return render_template("look10.html", curtida=" " )

@app.route('/curtida11', methods = ['GET','POST'])
def curtir11():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play11")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play11"))
            return render_template("look11.html", curtida=curtido.count() )
        except :
            return render_template("look11.html", curtida=" " )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play11"))
            return render_template("look11.html", curtida=curtido.count() )
        except :
            return render_template("look11.html", curtida=" " )

def takeDataHora():
    data = str(datetime.today().strftime("%d/%m/%Y"))
    hora = str(datetime.time(datetime.now()))
    hora = hora[0:8]
    return data, hora


def consulta():
    consulta = votos.query.filter(votos.nome_modelo.like("M01"))
    return consulta.count()



def consulta2():
    consulta = votos.query.filter(votos.nome_modelo.like("M02"))
    return consulta.count()




def consulta3():
    consulta = votos.query.filter(votos.nome_modelo.like("M03"))
    return consulta.count()



def consulta4():
    consulta = votos.query.filter(votos.nome_modelo.like("M04"))
    return consulta.count()



def consulta5():
    consulta = votos.query.filter(votos.nome_modelo.like("M05"))
    return consulta.count()



def consulta6():
    consulta = votos.query.filter(votos.nome_modelo.like("M06"))
    return consulta.count()



def consulta7():
    consulta = votos.query.filter(votos.nome_modelo.like("M07"))
    return consulta.count()



def consulta8():
    consulta = votos.query.filter(votos.nome_modelo.like("M08"))
    return consulta.count()



def consulta9():
    consulta = votos.query.filter(votos.nome_modelo.like("M09"))
    return consulta.count()


def consulta10():
    consulta = votos.query.filter(votos.nome_modelo.like("M10"))
    return consulta.count()


def consulta11():
    consulta = votos.query.filter(votos.nome_modelo.like("M11"))
    return consulta.count()

def maior():
    modelo=["M01","M02","M03","M04","M05","M06","M07","M08","M09","M10","M11"]
    alto=0
    N=[consulta(),consulta2(),consulta3(),consulta4(),consulta5(),consulta6(),consulta7(),consulta8(),consulta9(),consulta10(),consulta11()]
    pos=0
    for i in N:
        if i>alto:
           alto=i
           posmaior=pos
        pos+=1
    Ganhou = [str(alto), modelo[posmaior]]
    return str(Ganhou)

@app.route('/ganhador', methods=['GET'])
def ganhador():
    return maior()

###Funções Arduíno
statusModeloUm = "Null"

@app.route('/setamodelo', methods=['GET','POST'])
def setamodelo():
    if request.method == 'POST':
        colar = request.form['.colar']
        print(colar)
    global statusModeloUm
    statusModeloUm = colar
    return {"Stat Modelo Um": statusModeloUm}

def setamodeloFuncao(valor):
    global statusModeloUm
    statusModeloUm = valor
    return {"Stat Modelo Um": statusModeloUm}

@app.route('/setamodelocolar', methods=['GET','POST'])
def setamodelocolar():
    setamodeloFuncao( "colar" )
    return render_template("arduino.html")

@app.route('/setamodelojanela', methods=['GET','POST'])
def setamodelojanela():
    setamodeloFuncao( "janela" )
    return render_template("arduino.html")

@app.route('/setamodeloolhos', methods=['GET','POST'])
def setamodeloolhos():
    setamodeloFuncao( "olhos" )
    return render_template("arduino.html")

@app.route('/setamodelotodos', methods=['GET','POST'])
def setamodelocolartodos():
    setamodeloFuncao( "todos" )
    return render_template("arduino.html")

@app.route('/statusmodeloum', methods=['GET', 'POST'])
def testaget():
    global statusModeloUm
    valor = statusModeloUm
    statusModeloUm = "Null"
    return  str(valor)

if __name__ == '__main__':
    app.run()