import numpy as np, pandas as pd
import cv2
from tqdm import tqdm_notebook, tqdm # Iteration visualization
tqdm.pandas(desc="Loading") # to do progress_apply for pandas

# D:\hong\ReSearch\object_detection\project11\fooddata\labels\train
# D:\hong\ReSearch\object_detection\project11\fooddata\labels\valid
# file_name = '01_011_01011001_160273203821324.txt' # normal file

path = 'D:\\hong\\ReSearch\\object_detection\\project11\\fooddata\\labels\\train'
text_path = 'D:\\hong\\ReSearch\\object_detection\\project11\\fooddata\\labels\\train\\01_011_01011001_160273203821324.txt'
test_text_path = 'D:\\hong\\ReSearch\\object_detection\\project11\\fooddata\\labels\\test_3lines.txt'
##############################################################################
# """
# scan the file and count the number of lines
# """
# from tqdm import tqdm

# num_lines = sum(1 for line in open(test_text_path,'r'))
# with open(test_text_path,'r') as f:
#     for line in tqdm(f, total=num_lines):
#         print(line)


#############################################################################

# """
# Load data from a single text file. and print if line equal of more than 2 
# """
# with open(test_text_path, "r") as f: # with open(path, "r") as f:
#     data = []
#     for itr, line in tqdm_notebook(enumerate(f)):
#         # Because we got annotation in the first two lines
#         if itr >= 2:
#             data.append(line.split())

# print(data)

###############################################################################################
# import os
# """
# Load data from a multiple text file. and print if line equal of more than 2 
# """
# path = 'D:\\hong\\ReSearch\\object_detection\\project11\\fooddata\\labels\\train\\'
# folders = os.listdir(path)

# for folder in folders:
#     bigdata=[]
#     input_path = path +folder

#     with open(input_path, "r") as f: # with open(path, "r") as f:
#         data = []
#         for itr, line in tqdm_notebook(enumerate(f)):
#             # Because we got annotation in the first two lines
#             if itr >= 2:
#                 data.append(line.split())
#     bigdata.append(data)
#     bigdata


###############################################################################################
# """
# detect if 2st line start with zero
# """
# sequence_wrong =  'D:\\hong\\ReSearch\\object_detection\\project11\\fooddata\\labels\\sequence_wrong.txt'
# with open(sequence_wrong, "r") as f: # with open(path, "r") as f:
#     data = []
#     wrong_path = []
#     for itr, line in tqdm_notebook(enumerate(f)):
#         # Because we got annotation in the first two lines
#         if itr >= 1:
#             data.append(line.split())
#             if line.startswith('0'):
#                 print(sequence_wrong)
#                 wrong_path.append(sequence_wrong)
#                 # wrong_path.append(test_text_path.split("_")[3]) # if put loop

# print('lines :', data)
# print(wrong_path)

###############################################################################################
# ### version 1 ####
# import os
# import pandas as pd
# """
# detect if 2st line start with zero (for loop)
# """
# path = 'D:\\hong\\ReSearch\\object_detection\\project11\\fooddata\\labels\\valid\\'
# folders = os.listdir(path)

# for folder in folders:
#     bigdata=[]
#     input_path = path +folder

#     with open(input_path, "r") as f: # with open(path, "r") as f:
#         data = []
#         wrong_path = []
#         lst = []
#         for itr, line in tqdm_notebook(enumerate(f)):
#             if itr == 0: # line 1
#                 if not line.startswith('0'):
#                     # line_exp = [int(line.split())]
#                     data.append(line.split())
#                     file_name = input_path.replace('.','_').split("_")[4] + "_" + input_path.replace('.','_').split("_")[5] + "." +  input_path.replace('.','_').split("_")[6] 
#                     # df_data = pd.DataFrame(line_exp, columns=['class','x_center', 'y_center', 'width', 'height'])
#                     lst.append([file_name])
#                     df_file_name = pd.DataFrame(lst, columns=['text_file_name'])
#                     wrong_path.append(file_name) # if put loop

#     print('lines :', data)
#     print('wrong file : ', wrong_path)
#     df_data = pd.DataFrame(line_exp, columns=['class','x_center', 'y_center', 'width', 'height'])
#     df_file_name = pd.DataFrame(lst, columns=['text_file_name'])



###############################

"""
to assgn variable to line 1 and line and line 3
"""
wrong_path1 =  ['01_012_01012005_161199537775866_0.txt',
 '01_012_01012005_161199741818001_1.txt',
 '01_012_01012005_161200094655743_1.txt',
 '01_012_01012005_161200549036274_0.txt',
 '01_012_01012005_161200650745034_0.txt',
 '01_012_01012005_161200673672022_0.txt',
 '01_012_01012005_161200787038929_0.txt',
 '01_012_01012005_161201840938665_1.txt',
 '01_013_01013001_161018381466700_1.txt',
 '01_013_01013001_161018382929618_1.txt',
 '01_013_01013001_161018384987036_0.txt',
 '01_013_01013001_161023096511483_1.txt']

wrong_path = ['01_011_01011001_160430513519326_0.txt',
'01_011_01011001_160430513519326_1.txt',
'01_011_01011001_160430671841454_0.txt',
'01_011_01011001_160430671841454_1.txt',
'01_011_01011001_160431037481797_1.txt',
'01_011_01011001_160431332598840_1.txt',
'01_011_01011001_160431335059622_0.txt',
'01_011_01011001_160431335059622_1.txt',
'01_011_01011001_160431555336131_0.txt',
'01_011_01011001_160431555336131_1.txt',
'01_011_01011001_160431813146811_1.txt',
'01_011_01011001_160431819659048_1.txt',
'01_011_01011001_160431847144463_0.txt',
'01_011_01011001_160431847144463_1.txt',
'01_011_01011001_160431907094464_0.txt',
'01_011_01011001_160431907094464_1.txt',
'01_011_01011001_160431950925346_0.txt',
'01_011_01011001_160431950925346_1.txt',
'01_011_01011001_160431960591108_0.txt',
'01_011_01011001_160431960591108_1.txt',
'01_011_01011001_160432321975023_0.txt',
'01_011_01011001_160432321975023_1.txt',
'01_011_01011001_160432332278464_0.txt',
'01_011_01011001_160432332278464_1.txt',
'01_011_01011001_160432413380392_0.txt',
'01_011_01011001_160432413380392_1.txt',
'01_011_01011001_160432478115063_0.txt',
'01_011_01011001_160432478115063_1.txt',
'01_011_01011001_160432676372046_0.txt',
'01_011_01011001_160432676372046_1.txt',
'01_012_01012005_161199537775866_0.txt',
'01_012_01012005_161199741818001_1.txt',
'01_012_01012005_161200094655743_1.txt',
'01_012_01012005_161200549036274_0.txt',
'01_012_01012005_161200650745034_0.txt',
'01_012_01012005_161200673672022_0.txt',
'01_012_01012005_161200787038929_0.txt',
'01_012_01012005_161201840938665_1.txt',
'01_013_01013001_161018381466700_1.txt',
'01_013_01013001_161018382929618_1.txt',
'01_013_01013001_161018384987036_0.txt',
'01_013_01013001_161023096511483_1.txt']

datapath = 'D:\\hong\\ReSearch\\object_detection\\project11\\fooddata\\labels\\valid\\'
file_list = wrong_path # path with sequence wrong
for file_name in file_list:
    input_path = datapath + file_name
    with open(input_path, "r") as f:
        # first_line = f.readline() # first line
        outputpath = 'D:\\hong\\ReSearch\\object_detection\\project11\\fooddata\\labels\\valid1\\'
        outputfile_name = file_name
        output_path = outputpath + outputfile_name
        
        lines = f.readlines()
        first_line =  lines[0].rstrip('\n')
        second_line =  lines[1].rstrip('\n')
        with open(output_path, 'w+') as fo:
            if not first_line.startswith('0'): # if 1st line is class zero
                fo.write(second_line  +'\n') # write lastline that start froom zero
                fo.write(first_line) # write 1st line tat start from 1
                print(first_line)
                print(second_line)
            
            

    