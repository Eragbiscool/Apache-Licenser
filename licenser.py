import re
import argparse
import datetime
from datetime import datetime

print_counter = 0
functionality_counter = 0
program_number = 0
project_number_error = 0
expection = 0
language_counter = 0

argparser = argparse.ArgumentParser(description='Description:\n This script adds **license initials** all the files mentioned in the **file_list path**. It takes some of the information from the user to make the initials more informative. But most of the arguments are optional. Required argument is the **-filelist_path** where you will have to put the path of the filelist and **-language** where you will have to put the languages for each of the files. For the license itself, please open LICENSE file came with this script.')


argparser.add_argument("-filelist_path",type=str,help="Put the path of the filelist here",required=True)
argparser.add_argument("-company_name",type=str,help="Put the company or organization name here in quotation, if nothing is put, then a default company name will be written",default="<Your Company Name>")
argparser.add_argument("-project_name",type=str,help="Put the project name here in quotation, if nothing is put, then a default project name will be written", nargs='*')
argparser.add_argument("-developer_name",type=str,help="Put the Developer's name here in quotation one by one, if nothing is inserted, then **None** will be shown",nargs='*')
argparser.add_argument("-functionality",type=str,help="Write something about this in a very gist form",nargs='*')
argparser.add_argument('-project_name_norepeat',action='store_false',help="If you want this switch to work, then just mention this switch as **-project_name_norepeat** with other switches")
argparser.add_argument('-language',type=str,help="Consists of coding language used in the file. For each files, write the relevant language in a quotation "" using comma between all the languages. Use it something like this: -language 'python,java' 'verilog,system-verilog'",nargs='+',required=True)

args = argparser.parse_args()



def license_write(f):
    global print_counter
    global functionality_counter
    global program_number
    global file_lines
    global project_number_error
    global language_counter
    
    
   
    
    try:
        import pyfiglet
        if(args.project_name_norepeat==True):
            T = args.project_name[0]
            ASCII_art_1 = pyfiglet.figlet_format(T)
            lines = ASCII_art_1.split("\n")
            longest_line = max(lines, key=len)
            f.write("\n/*"+'*' * len(longest_line)+"\n")
            f.write(ASCII_art_1+"\n")
            f.write('*' * len(longest_line)+"*/")
        else:
            T = args.project_name[program_number]
            ASCII_art_1 = pyfiglet.figlet_format(T)
            lines = ASCII_art_1.split("\n")
            longest_line = max(lines, key=len)
            f.write("\n/*"+'*' * len(longest_line)+"\n")
            f.write(ASCII_art_1+"\n")
            f.write('*' * len(longest_line)+"*/")
            program_number = program_number + 1
    except:
            if(args.project_name_norepeat==True):
                T=args.project_name[0]
                f.write("\n/*"+'*' * len(T)+"\n")
                f.write(T)
                f.write("\n"+'*' * len(T)+"*/")
            else:
                T=args.project_name[program_number]
                f.write("\n/*"+'*' * len(T)+"\n")
                f.write(T)
                f.write("\n"+'*' * len(T)+"*/")
                program_number = program_number + 1
            if(print_counter == 0):
                print("For magic, run this command in your terminal *pip install pyfiglet*. This will install a package which will help you with a better visuals")
            print_counter = 1


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
    limitations under the License\n
*/\n\n'''.format(datetime.now().year, args.company_name)



    lines = lic.split("\n")
    longest_line = max(lines, key=len)
    f.write(lic)
    f.write("/*********************************************************\n")
    if(args.functionality):
        f.write('''functionality:\n
        {}'''.format(args.functionality[functionality_counter]+"\n\n"))
        functionality_counter = functionality_counter +1
    else:
        f.write("functionality:\n\n\t\t***None***\n\n")

    f.write("Developers :"+"\n")
    if(args.developer_name):
        for i in range(len(args.developer_name)):
            f.write('''
        {}'''.format(args.developer_name[i]+"\n"))
    else:
        f.write("\n\n\t\t***None***\n\n")

    f.write("\nLanguages Used:"+"\n")

    

    if(args.language):
        f.write('''
        {}'''.format(args.language[language_counter]+"\n"))
        language_counter = language_counter + 1
    else:
        f.write("\n\n\t\t***None***\n\n")

    f.write("\n*********************************************************/\n\n")





f=open(args.filelist_path,'r')
file_lines= f.readlines()



try:
    project_number_zero = 0
    project_number_big = 0
    project_number_big_norepeat = 0
    project_number_small = 0
    functionality_number_big = 0
    functionality_number_less = 0
    language_number_big = 0
    language_number_less = 0

    
    
        
    if args.project_name is None:
        project_number_zero = 1
        raise Exception
    else:
        
        if(args.project_name_norepeat==True):
            if(len(args.project_name)>1):
                project_number_big_norepeat = 1
                raise Exception
        else:
            
            if(len(args.project_name)>len(file_lines)):
                project_number_big = 1
                raise Exception
            elif(len(args.project_name)<len(file_lines)):
                project_number_small = 1
                raise Exception
        if(len(args.functionality)>len(file_lines)):
            functionality_number_big = 1
            raise Exception
        elif(len(args.functionality)<len(file_lines)):
            functionality_number_less = 1
            raise Exception
        elif(len(args.language)>len(file_lines)):
            language_number_big = 1
            raise Exception
        elif(len(args.language)<len(file_lines)):
            language_number_less = 1
            raise Exception
            
except:
        expection = 1
        if(project_number_zero == 1):
            print("Error: You have not inserted any project name")
        else:
            if(project_number_big == 1):
                print("Error: You might have inserted more project name than expected")
            elif(project_number_small ==1):
                print("Error: You might have inserted less number of project names than expected")
            elif(functionality_number_big==1):
                print("Error: You have inserted more functionality than expected, please remove unnecessary functionality that you have defined through arguments and Run again")
            elif(functionality_number_less==1):
                print("Error: You have inserted less functionality than expected")
            elif(language_number_less==1):
                print("Error: You have not inserted languages for all the files in the filelist.")
            elif(language_number_big==1):
                print("Error: You have inserted more languages than the number of files in the filelist.")
            elif(project_number_big_norepeat==1):
                print("Error: You have inserted more than one project for no_repeat operation. If you want repeat operation for project name, then keep only one project name. If you dont want repeat operation then use '-project_name_norepeat' as switch in the argument")   


try:
    if(expection==0):
        for i in file_lines:
            j=re.split("[\n]",i)[0]
            files = open(j, 'r+')
            read_line = files.readlines()
            files.seek(0) 
            license_write(files)
            for line in read_line:
                files.write(line)
            files.close()
    else:
        raise Exception
except:
    pass
    


f.close()
