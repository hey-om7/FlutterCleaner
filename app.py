import time
import os
import shutil

from filePicker import pickFile
from progressBar import progressBar


def deleteFromFlutter(path: str):
    l1 = [i.name for i in os.scandir(path)]
    if "build" in l1:
        shutil.rmtree(path + "/build")
    # for android insights deletion
    l2 = [i.name for i in os.scandir(path+"/android")]
    if ".gradle" in l2:
        shutil.rmtree(path + "/android/.gradle")
    if ".dart_tool" in l1:
        shutil.rmtree(path + "/.dart_tool")
    # for ios insights deletion
    l3 = [i.name for i in os.scandir(path+"/ios")]
    if "Pods" in l3:
        shutil.rmtree(path + "/ios/Pods")


def checkIfFlutterProject(path: str):
    l1 = [i.name for i in os.scandir(path)]
    if "pubspec.yaml" not in l1:
        return 0
    if "android" not in l1:
        return 0
    if "lib" not in l1:
        return 0
    return 1


os.system('clear')
# l2 = [i[0] for i in os.walk(os.path.expanduser('~') + "/")]
print("Please select the folder or directory")
pickedFileDir = pickFile()
time.sleep(0.5)
print("Please wait while the data is being fetched...")
l2 = [i[0] for i in os.walk(pickedFileDir + "/")]
print("Data fetched successfully!")
time.sleep(1)
print("Now filtering the data...")
l2 = list(filter(checkIfFlutterProject, l2))
print("Hold tight while we clear the useless data ;)")
for item in progressBar(l2, prefix='Progress:', suffix='Complete', length=50):
    deleteFromFlutter(item)
    time.sleep(0.1)
print("Successfully cleaned all the flutter's junk!")
