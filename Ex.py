import random
def Saisir():
	n = int(input("Saisir n: "))
	while n<=2 or n>=10:
		n = int(input("n = "))
	return n

def Remplir(n):
	T=[]
	for i in range(n):
		f=[]
		for j in range(n):
			f.append(chr(random.randint(65,90)))
		T.append(f)
	return T

def Line(T,n):
	print("Ligne:")
	for i in range(n):
		for j in range(n):
			print(T[i][j],end="")
		print()

def Column(T,n):
	print("Colonne:")
	for i in range(n):
		for j in range(n):
			print(T[j][i],end="")
		print()

def Diago(T,n):
	print("Diag:")
	for i in range(n):
		for j in range(n):
			if (i==j):
				print(T[i][j],end="")
	print()
def AntiDiago(T,n):
	print("AntiDiag:")
	for i in range(n):
		for j in range(n):
			if (i+j == n-1):
				print(T[i][j],end="")

def Affiche(T,n):
	Line(T,n)
	Column(T,n)
	Diago(T,n)
	AntiDiago(T,n)

n = Saisir()
T = Remplir(n)
Affiche(T,n)