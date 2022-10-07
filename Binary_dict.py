import pickle
def Append(d):
    fab=open("studentdict.dat","ab")
    pickle.dump(d,fab)
    fab.close()


def readall():
    frb=open("studentdict.dat","rb")

    while True:
        try:
            d=pickle.load(frb)
            print(d)
        except EOFError:
            break

    frb.close()

def search_rno(r):
    frb=open("studentdict.dat","rb")
    found=0

    while True:
        try:
            d=pickle.load(frb)
            if d['rno']==r:
                print("record found")
                print(d)
                found=1
        except EOFError:
            break

    frb.close()
    if found==0:
        print("no record exists for roll no",r)

def search_name(n):
    frb=open("studentdict.dat","rb")
    found=0

    while True:
        try:
            d=pickle.load(frb)
            if d['name']==n:
                print("record found")
                print(d)
                found=1
        except EOFError:
            break

    frb.close()
    if found==0:
        print("no record exists for roll no",r)



#d={'rno':1,'name':'Aakarsh','marks':99}
#Append(d)
#d={'rno':2,'name':'Aakriti','marks':98}
#Append(d)
readall()
search_rno(2)
search_name('Aakarsh')




        
    


    
    
