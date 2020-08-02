test = {range(0,100):'rest',
    400:'455'
}

x = 40
for key in test:
    if x in key:
        print(test[key])
        break
