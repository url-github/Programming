A = [1,2,3,3,4,1,2,3]

B = []

for element in A:
	if element not in B:
		B.append(element) # to metoda obiektu typu lista w Pythonie. Metody w Pythonie to funkcje, które są wywoływane na obiektach i mogą zmieniać stan obiektu lub wykonywać operacje z nim związane.
print(B)

##

B = list(set(A))
print(B)

##

A = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7, 5, 43, 4, 6]

def countUniqueElements(user_list):
    print(len(set(A)))


countUniqueElements(A)