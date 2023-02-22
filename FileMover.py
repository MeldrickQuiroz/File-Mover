import shutil

destination = '/This/is/where/the/file/will/go'

filepaths = ["This is the file you want to move using filepaths"]

for i in range(0, len(filepaths)):
    shutil.move(filepaths[i], destination)


