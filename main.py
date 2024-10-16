input_data = open('input.txt','r')
data = input_data.read()
output_data = open('output.txt','w')
data = data.split()
a = int(data[0])
if a%3 == 0:
    s = int(a/3)
else:
    s = int(a/3+1)
output_data.write(str(s))
output_data.close()
input_data.close()