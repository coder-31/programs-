import pickle
import os

def add_mobile():
    global l
    model = int(input("Enter Mobile Model :"))
    company = input("Enter Mobile Company :")
    price = int(input("Enter Mobile Price :"))

    l = [model, company, price]
    fobj = open("mobile.dat", "ab")
    fwb = pickle.dump(l, fobj)

def show_all():
    if os.path.isfile("Mobile.dat"):  
        fobj = open("mobile.dat", "rb")
        while True:
            try:
                frb = pickle.load(fobj) 
                print(frb)
            except:
                fobj.close()
                
                break
    else:
        print("File not exists")

def show_model(modelno):
    fobj=open("Mobile.dat", "rb")
   
    while True:
        try:
            frb=pickle.load(fobj)
            if frb[0]==n1:
                print(frb[0], frb[1], frb[2])
        except:
            fobj.close()
            break
        
def delete_mobile(modelno):
    if os.path.isfile("Mobile.dat"):
        fobj=open("Mobile.dat", "rb")
        temp=open("temp.dat", "wb")
        found=0
        while True:
            try:
                frb1=pickle.load(fobj)
                if frb1[0] != n2:
                    frb2=pickle.dump(frb1,temp)
                else:
                    found =1
                    
            except:
                break
        fobj.close()
        temp.close()
        os.remove("Mobile.dat")
        os.rename("temp.dat", "Mobile.dat")

        if found == 0:
            print("Model no. not exists")
        else:
            print("Record Deleted")
            show_all()
    else:
        print("File not exists")

def count_company(company):
    if os.path.isfile("Mobile.dat"):
        fobj=open("Mobile.dat", "rb")
        found=0
        
        while True:
            try:
                frb=pickle.load(fobj)
                if frb[1] == n3:
                    print(frb)
                    found+=1
            except:
                break
        print("the number of mobiles given by this company is", found)
        fobj.close()
        if found ==0:
            print("Company not found")
    else:
        print("File not exists")

def update_price(Modelno,price):
    if os.path.isfile("Mobile.dat"):
        fobj=open("Mobile.dat", "rb")
        temp=open("temp.dat", "wb")
        found=0
        while True:
            try:
                frb=pickle.load(fobj)
                if n4 == frb[0]:
                    frb[2] = p
                    pickle.dump(frb, temp)
                    found=1
                    print("price updated")
                    
                else:
                    pickle.dump(frb, temp)
                
            except:
                break
            
        fobj.close()
        temp.close()

        os.remove("Mobile.dat")
        os.rename("temp.dat", "Mobile.dat")
        if found == 0:
            print("record does not exists")
    else:
        print("file does not exists")


#main menu
        
while True:
    print("""

------MENU------""")
    print("""1. Add record
2. Display all records
3. Search a record
4. Delete a record
5. Count no. of Mobiles given by a company
6. Update Price of Mobile
7. Exit Menu""")

    ch=int(input("Enter Your Choice :"))

    if ch == 1:
        add_mobile()

    elif ch  == 2:
        show_all()

    elif ch == 3:
        n1= int(input("Enter Model No. :"))
        show_model(n1)

    elif ch == 4:
        n2= int(input("Enter Model No. :"))
        delete_mobile(n2)

    elif ch == 5:  
        n3=input("Enter Company Name :")
        count_company(n3)

    elif ch == 6:
        n4=int(input("Enter the Model No. :"))
        p=int(input("Enter the new Price :"))
        update_price(n4,p)
        
    elif ch == 7:
        print("Thank You")
        break
    
    else:
        print("Invalid Input !!!")
        break


