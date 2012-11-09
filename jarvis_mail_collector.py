#!/Library/Frameworks/Python.framework/Versions/3.2/bin/python3.2
import sys
sys.path.append('/Users/kevin/Library/Jarvis/JarvisMail')
import jarvismail_methods
import pickle
import datetime


jarvismessage = jarvismail_methods.jarvismessage
getgmail = jarvismail_methods.getgmail

username = 'antonshipley'
password = 'F=kqq/r2'

new_messages = getgmail(username,password,'UNSEEN')
print(len(new_messages))

infile = open('/Users/kevin/Library/Jarvis/JarvisMail/jmail_new_messages.dat','rb')
pickled_messages = pickle.load(infile)
infile.close()

all_messages = pickled_messages + new_messages
print(len(all_messages))
outfile = open('/Users/kevin/Library/Jarvis/JarvisMail/jmail_new_messages.dat','wb')
pickle.dump(all_messages,outfile)
outfile.close()

#Use this in other modules for reading the messages in jmail_new_messages.dat
def getjmail(querryfilename):
    import pickle
    messages_file_name = '/Users/kevin/Library/Jarvis/JarvisMail/jmail_new_messages.dat'
    messages_file = open(messages_file_name,'rb')
    jmail_messages = pickle.load(messages_file)
    messages_file.close()

    IDlist = []
    for y in jmail_messages:
        IDlist.append(y.ID)

    querry_file_name = querryfilename
    querry_file = open(querry_file_name,'rb')
    pickled_list = pickle.load(querry_file)
    querry_file.close()

    IDlist = list(set(IDlist)-set(pickled_list))

    removelist = []
    for y in jmail_messages:
        alreadycopied = True
        for x in IDlist:
            if x == y.ID:
                alreadycopied = False
        if alreadycopied == True:
            removelist.append(y)
    for y in removelist:
        jmail_messages.remove(y)
    full_list = pickled_list + IDlist
    
    outfile = open(querry_file_name,'wb')
    pickle.dump(full_list,outfile)
    outfile.close()
    
    return(jmail_messages)
