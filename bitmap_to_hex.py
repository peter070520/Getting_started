inp = 0
a = []
b = []
c = []
while inp < 16: 
	x = input()
	a.append(x)
	inp+= 1
print(a)

for i in range(0,16):
	kq ='0x'
	for j in range(0,7,4):
		s = a[i][j] + a[i][j+1] + a[i][j+2] + a[i][j+3]
		if s == '0000':
			kq += '0'
		elif s == '0001':
			kq += '1'
		elif s == '0010':
			kq += '2'
		elif s == '0011':
			kq += '3'
		elif s == '0100':
			kq += '4'
		elif s == '0101':
			kq += '5'
		elif s == '0110':
			kq += '6'
		elif s == '0111':
			kq += '7'
		elif s == '1000':
			kq += '8'
		elif s == '1001':
			kq += '9'
		elif s == '1010':
			kq += 'A'
		elif s == '1011':
			kq += 'B'
		elif s == '1100':
			kq += 'C'
		elif s == '1101':
			kq += 'D'
		elif s == '1110':
			kq += 'E'
		elif s == '1111':
			kq += 'F'
		else:
			kq = kq
	b.append(kq)
	kq ='0x'
	for j in range(8,15,4):
		s = a[i][j] + a[i][j+1] + a[i][j+2] + a[i][j+3]
		if s == '0000':
			kq += '0'
		elif s == '0001':
			kq += '1'
		elif s == '0010':
			kq += '2'
		elif s == '0011':
			kq += '3'
		elif s == '0100':
			kq += '4'
		elif s == '0101':
			kq += '5'
		elif s == '0110':
			kq += '6'
		elif s == '0111':
			kq += '7'
		elif s == '1000':
			kq += '8'
		elif s == '1001':
			kq += '9'
		elif s == '1010':
			kq += 'A'
		elif s == '1011':
			kq += 'B'
		elif s == '1100':
			kq += 'C'
		elif s == '1101':
			kq += 'D'
		elif s == '1110':
			kq += 'E'
		elif s == '1111':
			kq += 'F'
		else:
			kq = kq
	c.append(kq)

print('{', end='')
for i in range(0, 15):
	print(b[i], end=',')
print(b[15], '},', sep ='')
print('{', end='')
for i in range(0, 15):
	print(c[i], end=',')
print(c[15], '},', sep ='')