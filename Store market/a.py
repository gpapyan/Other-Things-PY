import shelve

sh = shelve.open('products.db')

for key in sh:
    print(key)

sh.close()
