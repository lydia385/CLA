#Read all of the content of the file in one variable
file = open('student-names.txt')
students = file.read()
file.close()
#Write a list of random names to your file.
students = students + "Lydia MESSAOUDENE"  + "\nMEROUANE charou"+ " \nKATIA KAKI"+"\nkarim kiki"
file = open('student-names.txt', 'w')
file.write(students)
file.close()

#Read the first n lines of the file.
file = open('student-names.txt')
n=input("write the number of linens you want to read: ")
for i in range(int(n)+1):
  print(file.readline())

#Read the last n lines of the file.
n=int(input("write the number of the n last linens you want to read: "))
with open('student-names.txt', 'r') as f:
	for line in (f.readlines() [-n:]):
	 print(line)

#Check if the name x is in the file
n=input("write the name you want to check: ")
file=open('student-names.txt') 
if(n in file.readlines()): print("exist")
else : print("don't exist")

#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
alphabet= 65
for i in range(26) :
    caractere = chr(alphabet)
    f= open(caractere+".txt","w+")
    alphabet = ord(caractere) +1
    