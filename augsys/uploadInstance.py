import os
import zipfile

def uploadInstance(file):
    head_path = '/Users/zhangshijie/Desktop/SegTest-Data/InstancePool'
    zip_file = zipfile.ZipFile(file)
    if not os.path.exists(head_path):
        os.mkdir((head_path))
    zip_file.extractall(path=head_path)
    return True