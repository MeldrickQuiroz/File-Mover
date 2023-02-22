import shutil

destination = '/Volumes/Saturn/MEDIA_VAULT/zPURGE_IT'

filepaths = []

for i in range(0, len(filepaths)):
    shutil.move(filepaths[i], destination)


