
    


#print multiple lines in line file by loop
f=open("03_print_multiple_line.txt")
line=f.readline()
while(line !=""):
    print(line)
    line=f.readline()
f.close()