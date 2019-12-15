import random 
import string 
import json
import csv
import os.path
from os import path


	

def ran_gen(size, chars=string.ascii_uppercase + string.digits): 
	""" fonction pour generer un code 
	"""
	return ''.join(random.choice(chars) for x in range(size)) 



def creation_de_code(nbreDeCode, nbreDeCaractere):
	""" nbre de code = est le nbre  
	"""
	for i in range(nbreDeCode):
		print (ran_gen(nbreDeCaractere)) 



def numero_destinataire(num_expediteur):
	"""fonction pour afficher 
	le numero du destinataire du message
	"""
	with open('correspondance_id.json') as myfile:
		obj = json.loads(myfile.read())



	if os.path.isfile("output.json")  :
		with open("output.json", "r") as json_file:
			score_dict = json.load(json_file)
		print("le fichier existe voici le dictionnaire ",score_dict)
		score_dict[num_expediteur]+= 1

		with open("output.json", "w") as json_file:
			json.dump(score_dict,json_file)



	else:
		score_dict = {}
		score = 0
		for cle in (obj[0]):
			score_dict[cle] = score
		print("first table: ", score_dict)


		with open("output.json", "w") as json_file:
			json.dump(score_dict, json_file)
		# w = csv.writer(open("output.csv", "w"))
		# for key, val in score_dict.items():
		# 	w.writerow([key, val])



	# print("second table : ", score_dict)


	return  obj[0][num_expediteur]

print(numero_destinataire("U30G8LW7"))
# # import json
# # with open('path_to_file/person.json') as f:
# #   data = json.load(f)
# # # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
# # print(data)
# # show values
# # print("usd: " + str(obj['usd']))
# # print("eur: " + str(obj['eur']))
# # print("gbp: " + str(obj['gbp

# print(numero_destinataire("AI6Y9BTG"))