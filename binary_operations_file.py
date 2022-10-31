'''
Create a binary file with name and roll number. Search for a given roll number and display
the name, if not found display appropriate message.
Create a binary file with roll number, name and marks. Input a roll number and update the marks. 
'''

import pickle,os
#Function to append records to student.dat file
def Append(l):  
    fwb=open("student.dat","ab")
    pickle.dump(l,fwb)
    fwb.close()
    print("Data succsessfully written to binary file")

#Function to display all records stored in student.dat file
def readall():
    if os.path.isfile("student.dat"): #file exists
        frb=open("student.dat","rb")
        print("Contents of student.dat file...")
        while True:
            try:
                l=pickle.load(frb)
                print(l)
            except EOFError:
                break
                frb.close()
    else:
        print("File does not exist")

#Function to search and display the student record roll number wise
def search_rno(r):
    if os.path.isfile("student.dat"): #file exists
        frb=open("student.dat","rb")
        found=0
        while True:
            try:
                l=pickle.load(frb)
                if r==l[0]:
                    print(l)
                    found=1
                    break  #because rno is unique
            except EOFError:
                break
        if found==0:
            print("Roll no",r,"does not exist.")
        frb.close()
    else:
        print("File does not exist")

#Function to search and display the student record name wise
def search_name(n):
    if os.path.isfile("student.dat"): #file exists
        frb=open("student.dat","rb")
        found=0
        while True:
            try:
                l=pickle.load(frb)
                if n==l[1]:   #made changes
                    print(l)
                    found=1
            except EOFError:
                break
        if found==0:
            print("Name",n,"does not exist.")
        frb.close()
    else:
        print("File does not exist")

#Function to search the student record on roll number and update the name and marks as
#required by the user.
def update(r):
    if os.path.isfile("student.dat"): #file exists
        frb=open("student.dat","rb")
        fwb=open("temp.dat","wb")
        found=0
        while True:
            try:
                l=pickle.load(frb)
                if r==l[0]:
                    ans1=input("Update name?")
                    if ans1=='y' or ans1=='Y':
                        l[1]=input("Enter the new name")
                        
                    ans2=input("Update marks?")
                    if ans2=='y' or ans2=='Y':
                        l[2]=int(input("Enter the new marks"))

                    #dump the updated record in temp.dat file
                    pickle.dump(l,fwb)
                    found=1
                else:
                    pickle.dump(l,fwb)
            except EOFError:
                break

        frb.close()
        fwb.close()
        os.remove("student.dat")
        os.rename("temp.dat","student.dat")

        if found==0:
            print("Roll no",r,"does not exist.")
        else:
            print("Record updated....")
            readall()
    else:
        print("File does not exist")

    

def delete(r):
    if os.path.isfile("student.dat"): #file exists
        frb=open("student.dat","rb")
        fwb=open("temp.dat","wb")
        found=0
        while True:
            try:
                l=pickle.load(frb)
                if r!=l[0]: #record not be deleted
                    pickle.dump(l,fwb)
                else:
                    found=1
            except EOFError:
                break
        frb.close()
        fwb.close()
        os.remove("student.dat")
        os.rename("temp.dat","student.dat")

        if found==0:
            print("Roll no",r,"does not exist.")
        else:
            print("Record deleted....")
            readall()
    else:
        print("File does not exist")

def searchmenu():
    while True:
        print("--------------SEARCH MENU----------------")

        print("1. Search by roll no")
        print("2. Search by name")
        print("3. Return to Main Menu")
        ch=int(input("Enter your choice:"))
        if ch==1:
            rno=int(input("Enter the roll no whose record is to be searched:"))
            search_rno(rno)
        elif ch==2:
            nm=input("Enter the name whose record is to be searched:")
            search_name(nm)
        elif ch==3:
            break
        


def mainmenu():
    while True:
        print("--------------BINARY FILE OPERATIONS----------------")
        print("1. Append records")
        print("2. Display all records")
        print("3. Search Records")
        print("4. Update Records")
        print("5. Delete Records")
        print("6. EXIT")
        ch=int(input("Enter your choice:"))
        if ch==1:
            print("Enter the student record")
            rno=int(input("Enter the roll no:"))
            name=input("Enter the name:")
            marks=int(input("Enter the marks:"))
            rec=[rno,name,marks]
            Append(rec)
        elif ch==2:
            readall()
        elif ch==3:
            searchmenu()
        elif ch==4:
            rn=int(input("Enter the roll no whose record is to be updated:"))
            update(rn)
        elif ch==5:
            rn=int(input("Enter the roll no whose record is to be deleted:"))
            delete(rn)
        elif ch==6:
            break


mainmenu()


