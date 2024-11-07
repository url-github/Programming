# Pytanie 30 - jaką wartość przyjmie poniższe zdanie logiczne?
# Wyjaśnij proces jego ewaluacji i znaczenie poszczególnych słów: is, not, in.

print(1 is not True in [1,2,3]) # ->
# (1 is not True) and (True in [1,2,3]) # ->
# (True) and (True) -> True

# różne wyniki dla operatorów "is not" oraz "!=" !
print(1 is not True) # True
print(1 != True) # False
print(not (1 is True)) # True
print(1 is True) # False

not 2 is 2.0 in [0,2]
# (not 2) and (2 is 2.0) and (2.0 in [0,2])
# (False) and (Fasle) and (True)
