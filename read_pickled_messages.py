#!/Library/Frameworks/Python.framework/Versions/3.2/bin/python3.2
import pickle

infile = open('/Users/kevin/Library/Jarvis/JarvisMail/jmail_new_messages.dat','rb')
pickled_messages = pickle.load(infile)
infile.close()

for y in pickled_messages:
    print(y.B)
    break
    
