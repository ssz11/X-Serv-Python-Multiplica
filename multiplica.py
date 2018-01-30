#1/usr/bin/python3

listadenum = list(range(1,11)); #PODEMOS PONER RANGE SOLO

for i in listadenum:
	print("TABLA DEL: " + str(i));
	for j in listadenum:
		mult = i*j;
		print(str(i) + " * " + str(j) + " = " + str(mult));
		if j == 10 :
			print('\n');

		
