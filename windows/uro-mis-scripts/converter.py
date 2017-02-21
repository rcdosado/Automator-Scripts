from datetime import datetime

f = open('convert_me1.txt', 'r')
dates = f.readlines()
f.close()

o = open('converted.txt', 'w')

for d in dates:
	obj= datetime.strptime(d.strip(),'%m-%d-%Y')
	nd = obj.strftime('%B %d, %Y\n')
	o.write(nd)
	print(nd)
o.close()

print("Done...")