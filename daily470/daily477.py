
functions = []
for i in range(10):
	functions.append(lambda x=i: x)

for f in functions:
	print(f())

def Fs():
	return functions
	