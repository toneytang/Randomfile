# author by LYS 2017/5/24
# for Deep Learning course
'''
1. read the whole files under a certain folder
2. chose 10000 files randomly
3. copy them to another folder and save
'''
import os, random, shutil
 
 
def copyFile(fileDir):
    # 1
    pathDir = os.listdir(fileDir)
    print (pathDir)
 
    # 2
    sample = random.sample(pathDir, 3)
    print (sample)
    
    # 3
    for name in sample:
        shutil.copyfile(fileDir+name, tarDir+name)
def moveFile(fileDir, tarRealDir, randomNumber):
    # 1
    pathDir = os.listdir(fileDir)
 
        # 2
    sample = random.sample(pathDir, randomNumber)
    print (sample)
    if not (os.path.exists(tarRealDir)):
        os.mkdir(tarRealDir)
        # 3
    for name in sample:
        shutil.move(fileDir+name, tarRealDir+name)
if __name__ == '__main__':
    fileDir = './src/'
    tarDir = './tag'
    randomNumber = 3
    i = 0
    #copyFile(fileDir)
    filesNumber = len(os.listdir(fileDir))
    print('File Number : '+str(filesNumber))
    if(filesNumber > 0):
        while( filesNumber > randomNumber):
            tarRealDir = tarDir + str(i).zfill(4) + '/'
            i = i+1
            moveFile(fileDir, tarRealDir, randomNumber)
            filesNumber = len(os.listdir(fileDir))
                
        if(filesNumber > 0):
            tarRealDir = tarDir + str(i).zfill(4) + '/'
            i = i+1
            moveFile(fileDir, tarRealDir, filesNumber) 

