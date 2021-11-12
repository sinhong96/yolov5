import os 
# D:\hong\ReSearch\object_detection\project11\fooddata\images\train
# D:\hong\ReSearch\object_detection\project11\fooddata\images\valid
data_path = 'D:\\hong\\ReSearch\\object_detection\\project11\\fooddata\\images\\valid\\'
img_names = os.listdir(data_path)

list_file = open(f'valid.txt', 'w')
for img_name in img_names:
    list_file.write('../fooddata/images/valid/%s\n'%img_name)

list_file.close()