
fxin = open("ex4x.dat")
fyin = open("ex4y.dat")

fx1 = []
fx2 = []
fy = []
for line in fxin:
	x1,x2 = line.split()
	fx1.append(float(x1.strip()))
	fx2.append(float(x2.strip()))
#
# Now labels
for line in fyin:
        fy.append(float(line.strip()))

fout = open("combined.csv","w")
fout.write("score1,scor2,admitted\n")
for i in range(len(fy)):
	fout.write(str(fx1[i])+','+str(fx2[i])+','+str(fy[i])+'\n')
fout.close()
