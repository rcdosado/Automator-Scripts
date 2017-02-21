from datetime import datetime

f = open('convert_me4.txt', 'r')
dates = f.readlines()
f.close()

o = open('converted4.txt', 'w')

for d in dates:
	obj= datetime.strptime(d.strip(),'%B %d, %Y')
	nd = obj.strftime('%m/%d/%Y\n')
	o.write(nd)
	print(nd)
o.close()

print("Done...")