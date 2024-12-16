#5(десятичная)
for n in range (100, 1000):
    s = str(n)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    first = str(max(k1, k2))
    second= str(min(k1, k2))
    s1 = first + second
    if s1 == "1412":
        print (n)
        break

for n in range (10000, 1000, -1):
    s = str(n)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[2]) + int(s[3])
    first = str(min(k1, k2))
    second =str(max(k1, k2))
    s1 = first + second
    if s1 == "117":
        print(n)
        break

for n in range (10000, 1000, -1):
    s = str(n)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    k3 = int(s[2]) + int(s[3])
    first = str(k1 + k2 + k3 - max(k1,k2,k3) - min(k1,k2,k3))
    second = str(max(k1,k2,k3))
    s1 = first + second
    if s1 == "1515":
        print (n)
        break

for n in range (10000, 1000, -1):
    s = str(n)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    k3 = int(s[2]) + int(s[3])
    first = str(k1 + k2 + k3 - max(k1, k2, k3) - min(k1, k2, k3))
    second= str(max(k1,k2,k3))
    s1 = first + second
    if s1 == "1517":
        print(n)
        break

#5(двоичная)
for n in range (1,100):
    s = bin(n)[2:]
    s = str(s)
    if n % 2 == 0:
        s = "10" + s
    else:
        s = "1" + s + "01"
    r = int(s, 2)
    if r > 441:
        print (n)
        break

for n in range (1,100):
    r = bin(n)[2:]
    r += str(r.count("1") % 2)
    r += str(r.count("1") % 2)
    if int(r, 2) > 97:
        print (n)
        break

for n in range(50):
    r = bin(n)[2:]
    r += str(r.count('1') % 2)
    r += str(r.count('1') % 2)
    if int(r, 2) > 77:
        print(n)
        break

for n in range(1,100):
    r = bin(n)[2:]
    r += str(r.count('1') % 2)
    r += str(r.count('1') % 2)
    s = int(r, 2)
    if s > 83:
        print(s)
        break

for n in range (1,1000):
    r = bin(n)[2:]
    r = str(r)
    if n / 2 != 0:
        r += "11"
    else:
        r += "00"
    s = int(r,2)
    if s > 114:
        print(s)
        break


