import os

def rename_multiple_files(path, obj):

    i=0
    for filename in os.listdir(path):
        try:
            f,extension = os.path.splitext(path+filename)
            src=path+filename
            dst=path+obj+str(i)+extension
            os.rename(src,dst)
            i+=1
        except:
            i+=1

path='/home/ssn/Documents/dhana/datasetpreprocessingcode/code/clip8/'
obj='algae'
rename_multiple_files(path,obj)