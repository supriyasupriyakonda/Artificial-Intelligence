currencies = ['Dollar', 'Euro', 'Pound']
currencies2=['USA','AFRICA','ANTARTICA']
currencies.append('Yen')
print("list after append(): " ,currencies)
currencies2.extend(currencies)
print("list after extend(): " ,currencies2)
currencies2.remove('AFRICA')
print("list after remove(): " ,currencies2)
