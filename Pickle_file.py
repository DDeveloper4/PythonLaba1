import pickle
import Model

def load_f():
	try: 
		with open('diary.txt') as file: 
			f = open( 'diary.txt', "r" )
			Model.diary = pickle.load(f)
	except IOError: 
		print ("Error! File not found or don`t read") 
	f.close()

def return_file():
	f = open('diary.txt','w')
	pickle.dump(Model.diary,f)
	f.close()