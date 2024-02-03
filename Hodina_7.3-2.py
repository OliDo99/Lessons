from binascii import a2b_base64


a=100
b=200
if a > b:
    print("A je vacsie ako B")
elif a ==b:
    print("A je rovne B")
else:
    print("A je mensie ako B")

a2=300
b2=200
print("A2 je vacsie ako B2") if a2 > b2 else print("A2 je rovne B2") if a2 == b2 else print("A2 je mensie ako B2")