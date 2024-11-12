def usun_ostatni_element_listy(lista=[1,1,1,1]):
     lista.pop()
     print(lista)

usun_ostatni_element_listy() # [1, 1, 1]
usun_ostatni_element_listy([5,5,5]) # [5, 5]
usun_ostatni_element_listy() # [1, 1]