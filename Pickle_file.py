def load_f():
try: 
with open('file.txt') as file: 
f = open( 'file.txt', "r" ) 
BASE = pickle.load(f) 
except IOError: 
print ("Error! File not found or don`t read") 
f.close()

def return_file():
f = open( ‘file_out.txt’, ‘w’ )
f.write( ‘??????’ )
f.close()