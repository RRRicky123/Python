import os
import re
import shutil

def mkdir(path):
  
    path = path.strip()
    path = path.rstrip('\\')

    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print (path+' Directory or file created successfully!')
        return True
    else:
        print (path+' Directory or file already exists!')
        return False

count = 0
for file in os.listdir('.'):
	if re.search("json", file):
		file_name = file.split(".")[0]
		with open(file_name + ".json") as f:
			result = f.read()

			print(result)

			try:
				count += 1
				print('count -----', count)
				dir_name = re.findall('"name": "(.*?)"', result)[0]
				print(dir_name)
				mkdir("./" + dir_name)
				shutil.copyfile("./" + file_name + ".jpeg",  "./" + dir_name + "/" + file_name + ".jpg")
			except Exception as e:
				print('error ------', e)
		

