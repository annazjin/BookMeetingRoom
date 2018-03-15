# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
limit=5
file_count=0
line_list=[]

with open("resume.txt") as f:
    for line in f:
        line_list.append(line)
        if len(line_list)<limit:
            
            continue
        file_name=str(file_count)+".txt"
        with open(file_name,'w') as file:
            for singleline in line_list[:-1]:
                file.write(singleline)
            file.write(line_list[-1].strip())
            line_list=[]
            file_count+=1
if line_list:
    file_name=str(file_count)+".txt"
    with open(file_name,'w') as file:
        for singleline in line_list:
            file.write(singleline)
print('done')
        
        

