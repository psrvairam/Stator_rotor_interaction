import sys
config = sys.argv[1]

names = ["NZONE", "IZONE"]
with open(config) as f:
    configuration = f.readlines()
    
parameters_tmp = [x.strip().split("=") for x in configuration]
parameters = dict()
for param in parameters_tmp:
    parameters[param[0]]=param[1]


content1=[]
mesh1 = parameters['output8_stator_perio.su2']
with open(mesh1) as f:
    for line in f.readlines():
        if not any(st in line for st in names):
            content1.append(line)  

content2=[]
mesh2 = parameters['output_rotor_perio.su2']
with open(mesh2) as f:
    for line in f.readlines():
        if not any(st in line for st in names):
            content2.append(line)  

combinedmesh = parameters["turbine_axial.su2"]
with open(combinedmesh, 'w') as f:
    f.write("NZONE=  2\n\n")
    f.write("IZONE=  1\n\n")
    for line in content1:
        f.write(line)
    f.write("IZONE=  2\n\n")
    for line in content2:
        f.write(line)
