car_01 = {
'carBrand':'Seat',
'carModel':'Ibiza',
'carIsAirBagOK':True,
'carIsPaintingOK':True,
'carIsMechanicOK':True
}

car_02 = {
'carBrand':'Opel',
'carModel':'Astra',
'carIsAirBagOK':True,
'carIsPaintingOK':False,
'carIsMechanicOK':True
}

def isCarDamaged(aCar):
	return not (aCar['carIsAirBagOK'] and aCar['carIsPaintingOK'] and aCar['carIsMechanicOK'])


# print(isCarDamaged(car_01))
# print(isCarDamaged(car_02))

cars = [car_01, car_02]
for c in cars:
	print("Samochód {} {} ma status {}".format(c['carBrand'], c['carModel'], isCarDamaged(c)))