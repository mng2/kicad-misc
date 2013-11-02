# proof of concept, very kludgy 
# use case: you have multiple inclusions of a schematic
# say page 2, 3, 4, etc.
# the parts are annotated as R201, R301, R401, etc
# manually lay out page 2
# run script to copy placement to page 3, 4, etc, with appropriate distance in Y
# copy the tracks manually in pcbnew

import sys, string, os, re
from decimal import *

fin = open(sys.argv[1],'r')
fout = open('testout.kicad_pcb','w')

data = []

for line in fin.readlines():
    data.append(line)

fin.close()

# 25.4mm * 1.1 = 27.94 mm
# 25.4mm * 0.5 = 12.70 mm
distance = Decimal('12.70')

for i in range(len(data)):
    if re.findall("fp_text reference [A-Z]31", data[i]):
        ref = re.findall('[A-Z]\d+',data[i])[0]
        type = ref[0]
        subpage = ref[2]
        number = ref[3]
        for x in range(1,5):
            if re.findall('\(at ',data[i-x]):
                place = re.split('([-+]?\d*\.\d+|\d+)',data[i-x])

                
        refline = re.split('(\s+)',data[i])
        for j in range(len(data)):
            if "fp_text reference "+type+"32"+number in data[j]:
                placenew = list(place) #must create new list object
                placenew[1] = str(Decimal(placenew[1])+distance)
                for x in range(1,5):
                    if re.findall('\(at ',data[j-x]):
                        data[j-x] = ''.join(placenew)
                
                
                x=4
                while (j+x+1 < len(data)) and (re.findall('\(module ',data[j+x])==[]):
                    x=x+1
                    if re.findall('\(pad ',data[j+x]):
                        data[j+x] = data[i+x]
                        print ref, i+x, j+x
                        
                
                currefline = re.split('(\s+)',data[j])
                data[j] = (''.join(currefline[:7]))+(''.join(refline[7:]))
                data[j+1] = data[i+1] # ref font
                data[j+3] = data[i+3] # value
                data[j+4] = data[i+4]
    
            if "fp_text reference "+type+"33"+number in data[j]:
                placenew = list(place)
                placenew[1] = str(Decimal(placenew[1])+2*distance)
                for x in range(1,5):
                    if re.findall('\(at ',data[j-x]):
                        data[j-x] = ''.join(placenew)
                
                
                x=4
                while (j+x+1 < len(data)) and (re.findall('\(module ',data[j+x])==[]):
                    x=x+1
                    if re.findall('\(pad ',data[j+x]):
                        data[j+x] = data[i+x]
                        print ref, i+x, j+x
                        
                
                currefline = re.split('(\s+)',data[j])
                data[j] = (''.join(currefline[:7]))+(''.join(refline[7:]))
                data[j+1] = data[i+1]
                data[j+3] = data[i+3]
                data[j+4] = data[i+4]

            if "fp_text reference "+type+"34"+number in data[j]:
                placenew = list(place)
                placenew[1] = str(Decimal(placenew[1])+3*distance)
                for x in range(1,5):
                    if re.findall('\(at ',data[j-x]):
                        data[j-x] = ''.join(placenew)
                    
                
                x=4
                while (j+x+1 < len(data)) and (re.findall('\(module ',data[j+x])==[]):
                    x=x+1
                    if re.findall('\(pad ',data[j+x]):
                        data[j+x] = data[i+x]
                        print ref, i+x, j+x
                        
                
                currefline = re.split('(\s+)',data[j])
                data[j] = (''.join(currefline[:7]))+(''.join(refline[7:]))
                data[j+1] = data[i+1]
                data[j+3] = data[i+3]
                data[j+4] = data[i+4]

                
                

                
for i in range(len(data)):
    fout.write(data[i])

fout.close()
    
