from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import csv
from csv import writer

app = Flask(__name__)

"""
    Enregistrer une ligne dans answers_qcm la fonction prend en paramètres 
    l'id de l'utilisateur, la quetion et la reponse de l'utilisateur 
"""
def insert_qcm_answer(user, question, answer) :

    #construire la ligne à inserer
    row_contents = [user, question, answer]

    #ouvrir le fichier 
    with open('data/answers_qcm.csv', 'a+', newline='') as write_obj:
        #inserer la ligne avec le separateur 
        csv_writer = writer(write_obj, delimiter=';')
        csv_writer.writerow(row_contents)

"""
    Enregistrer une ligne dans answer_free
"""
def insert_free_answer(user, question, answer) :

    row_contents = [user, question, answer]

    with open('data/answers_free.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj, delimiter=';')
        csv_writer.writerow(row_contents)


"""
    Récuperer les reponses possibles 
    d'une question Qcm a partir de son id
"""
def get_qcm(question_id) :
    #on initialise une liste vide
    liste=[]
    #on ouvre le fichier qui contient les reponses du qcm 
    with open( "data/matching_answers_qcm.csv")  as file_user:
        f_csv = csv.reader(file_user) 
        #on saute la premiere ligne
        headers = next(f_csv) 
        
        #on lit chaque ligne du fichier
        for row in f_csv:
            #si la premiere ligne (question_id est egale a la ligne passe en parametre) 
            if (row[0].split(';')[0] == question_id) : 
                #on ajoute a la liste la ligne parce que c'est une reponse possible du qcm
                liste.append(row[0].split(';'))
    #on retourne la liste
    return liste

"""
    Récuperer les utilisateurs  
    lire chaque ligne des utilisateurs et 
    l'ajouter à une liste 
"""
def users() :
    liste=[]
    with open( "data/users.csv")  as file_user:
        f_csv = csv.reader(file_user) 
        headers = next(f_csv) 
        for row in f_csv:
            liste.append(row[0].split(';')[0])
        
    return liste

"""
    Récuperer les réponses possibles de la liste des questions

"""
def questions() :
    liste=[]
    with open( "data/matching_questions.csv")  as file_user:
        #on lit le fichier  essaie de remplacer file_user par file_question

        f_csv = csv.reader(file_user) 
        headers = next(f_csv) 
        #on fait une boucle sur l'ensemble des elements
        for row in f_csv:
            qcm = row[0].split(';')
            #on recupere l'ensemble des réponses avec getqcm qui recupere les réponses
            #avec l'id de la question en parametre (id is qcm[0])
            answers = get_qcm(qcm[0])
            #on ajoute answers à la question
            qcm.append(answers)
            #on ajoute la question à la liste
            liste.append(qcm)
        
    return liste

"""
    Savoir à partir de son id si une question est un qcm 
    ou une question Libre 
"""
def type_qcm(question_id) :
    with open( "data/matching_questions.csv")  as file_user:
        f_csv = csv.reader(file_user) 
        headers = next(f_csv) 
        for row in f_csv:
            if (row[0].split(';')[0] == question_id) : 
                if (row[0].split(';')[1] == 'QCM'):
                    return True;
                
    return False;                
    
"""
    Prend en parametre le formumlaire
    Si QCM insere dans answer_qcm
    Si Libre et reponse non vide insere dans  answer_free
   
"""
def insert_data(data) : 
    #data = liste des reponses du formulaire web

    for k, v in data.items():
        #on fait une interaction key value sur les données 
        #Si ce n'est pas l'utilisateur et le type est qcm
        #on insert  avec la fonction
        if k!='user' and type_qcm(k) :
            insert_qcm_answer(data.get('user'), k, v)
        if k!='user' and v!='' and type_qcm(k)==False :
            insert_free_answer(data.get('user'), k, v)
            




#Accueil Formulaire
@app.route('/')
def index():
    #on envoie le fichier index.html  avec les donnés users et question 
    # users récupere la liste des utilisateurs 
    # questions la liste des question et leur reponse
    return render_template("index.html", users = users(), questions = questions())

#Sauvegarde Formulaire
@app.route('/answer',methods = ['POST'])
def answer():

    #insert les data récuperées avec request.form
    insert_data(request.form)
    return render_template("message.html")