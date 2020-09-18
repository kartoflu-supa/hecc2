from flask import Flask, render_template
from random import randint
app = Flask(__name__)

frettir = [
    [0,"Eru blóm vond?","Maður á akureyri var fundi látin eftir hann fór að þefa blóminn. Þegar löggan kom á svæðið fundu þau lyktina og voru seinna þann dag fundinn látin. ekki mikið meir er vitað en við munum upfæra þessari grein þegar við lærum meir","Jón Jónsson","WitherRose.jpg","JónJón@serikfréttir.net"]
    ,[1,"Coronaveiran vill bara knús","Corona er einmana og vill fá knús frá hversem er. Ekki hafa áhyggjur ef það líkar við þig nóg þá byrjar það ekki næstu plágu. :)","Alls ekki CoronaVeirann ;)","CoronaVeira.jpg","atencion.modelo@gmodelo.com.mx"] 
    ,[2,"lorem ipsum","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce imperdiet tellus rhoncus mi placerat luctus. Nunc efficitur laoreet tellus in malesuada. Etiam sit amet lectus at justo egestas pretium. Suspendisse potenti. Vestibulum felis sapien, venenatis ut nunc ut, molestie ultricies neque. Aliquam vitae mi et mauris efficitur venenatis at non erat. Cras tristique leo sollicitudin justo viverra, et sodales sapien pharetra. Phasellus vehicula magna orci, aliquam fermentum elit lacinia non. Mauris vel nunc ut justo dignissim vehicula. Aenean bibendum, nunc id aliquet accumsan, felis enim ultrices est, sit amet ultrices nisi nulla quis libero. Quisque quis vehicula sapien, non feugiat purus. Sed lobortis odio quis felis facilisis interdum. ","Muspi Merol","LoremIpsum.jpg","muspi@ekkinetfang.is"]
    ,[3,"Sveppaland?","Áætlun til að opna vörðuskóla undir nafninu Sveppaland hafa verið lýst eftir að Sverrir Þór Sverrisson keypti bygginguna Í ágúst. Óþekktur hópur frá Upplýsinga- og Tölvuskólinn hafa sent kvartanir til borgarstjóran um hvernig að hann sé 'Corpratist shill' fyrir að hafa samþykkt þenna skemtigarð.","Jón Jónsson","sveppi.jpg","JónJón@serikfréttir.net"]
        ]

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/lidur1')
def lidur1():
    nyKennitala = ""
    for x in range(10):
        t1 = str(randint(0,9))
        nyKennitala = nyKennitala+t1
    return render_template("sida1.html",nyKennitala = nyKennitala)

@app.route('/kennitala/<kt1>')
def kt(kt1):
    sum = 0
    for x in str(kt1):
        sum += int(x)
    return str(sum)

@app.errorhandler(404)
def error404(error):
    return "lol þessi síða ekki til!",404

@app.route('/lidur2')
def lidur2():
    return render_template("sida2.html", frettir = frettir)

@app.route('/grein/<int:id>')
def frett(id):
    frett = frettir[id]
    return render_template("frett.html",frett = frett)

if __name__ == "__main__":
    app.run(debug = True)
