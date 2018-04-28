from model import store_disasters

print('starting server.')
disasters = store_disasters()


disasters_in_1999 = [x for x in disasters if x.year == "1999"]
print(disasters_in_1999)