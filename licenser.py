import argparse
import datetime
from datetime import datetime

argparser = argparse.ArgumentParser()



argparser.add_argument("-company_name",type=str,help="Put the company or organization name here in quotation, if nothing is put, then a default company name will be written",default="Your Company Name")
argparser.add_argument("-project_name",type=str,help="Put the project name here in quotation, if nothing is put, then a default project name will be written",default="THE SIGNAL PROCESSOR")
argparser.add_argument("-developer_name",type=str,help="Put the Developer's name here in quotation one by one, if nothing is inserted, then **None** will be shown",nargs='*')
argparser.add_argument("-functionality",type=str,help="Write something about this in a very gist form",nargs='*')
args = argparser.parse_args()



f=open('Path of the file you want to license','r+')
file_lines= f.readlines()
f.seek(0) 

try:
    import pyfiglet
    T = args.project_name
    ASCII_art_1 = pyfiglet.figlet_format(T)
    lines = ASCII_art_1.split("\n")
    longest_line = max(lines, key=len)
    f.write("\n/*"+'*' * len(longest_line)+"\n")
    f.write(ASCII_art_1+"\n")
    f.write('*' * len(longest_line)+"*/")
except:
    f.write("\n/*"+'*' * len(longest_line)+"\n")
    f.write("SPU_LEO_8000")
    f.write('*' * len(longest_line)+"*/")


lic ='''\n\n/*
SPDX-License-Identifier: Apache-2.0
Copyright {} {} or its affiliates

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
*/\n\n'''.format(datetime.now().year, args.company_name)



lines = lic.split("\n")
longest_line = max(lines, key=len)
f.write(lic)
f.write("/*********************************************************\n")
f.write('''functionality:\n
    {}'''.format(args.functionality[0]+"\n\n"))
f.write("Developers :"+"\n")
if(args.developer_name):
    for i in range(len(args.developer_name)):
        f.write('''
    {}'''.format("\t"+args.developer_name[i]+"\n"))
else:
    f.write("\n\n\t***None***\n\n")

f.write("\n*********************************************************/\n\n")

for line in file_lines:
    f.write(line)


f.close()
