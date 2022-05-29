import os
import shutil


def deleteFromFlutter(path: str):
    l1 = [i.name for i in os.scandir(path)]
    if "build" in l1:
        shutil.rmtree(path + "/build")
    l2 = [i.name for i in os.scandir(path+"/android")]
    if ".gradle" in l2:
        shutil.rmtree(path + "/android/.gradle")
    if ".dart_tool" in l1:
        shutil.rmtree(path + "/.dart_tool")


def checkIfFlutterProject(path: str):
    l1 = [i.name for i in os.scandir(path)]
    if "pubspec.yaml" not in l1:
        return 0
    if "android" not in l1:
        return 0
    if "lib" not in l1:
        return 0
    return 1


l2 = [i[0] for i in os.walk(os.path.expanduser('~') + "/")]
l2 = list(filter(checkIfFlutterProject, l2))

for i in l2:
    deleteFromFlutter(i)
