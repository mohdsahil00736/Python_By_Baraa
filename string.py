
price = "123,58"
print(price.replace(',', '.'))
print(type(price))

phone = "+49 (176) 123-589"
#0049176123589 desired output

print(phone.replace('+','00').replace("(", "").replace(')', '').replace('-',"").replace(" ", ''))

# f string
print(f"{{this is me}}")

print("=" * 10)


data = "968-Maria, (Data@ Engineer) ;; 27y  "

print(data.replace(';', '').replace(',', '').replace('@','').replace('(','').replace(')',''))

x = 4
y = 6
print(complex(x,y))