import csv
from csv import writer


'''''
#with open('answer_free.csv', mode='w') as answer_free:
    answer_freewriter= csv.writer(answer_free, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
   answer_freewriter.writerow(['user_id', 'question_id', 'answer'])


with open('answer_qcm.csv', mode='w') as answer_qcm:
    answer_qcmwriter= csv.writer(answer_qcm, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    answer_qcmwriter.writerow(['user_id', 'question_id', 'answer'])


with open('matching_questions.csv', mode='w') as matching_questions:
    matching_questionswriter= csv.writer(matching_questions, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    matching_questionswriter.writerow(['question_id', 'answer_id', 'answer_title'])
'''
def insert_user(file_name) :
    code_postal = input("code_postal :")
    commune =  input("Commune :")
    type_commune =  input("Type :")
    nom_departement =  input("Nom departement :")
    
    row_contents = [32, code_postal, commune,type_commune, nom_departement]

    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(row_contents)


insert_user("users.csv")
