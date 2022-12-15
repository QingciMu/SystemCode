import torch
import glob
from augsys.generalMethod import *
def startSegNet(testCase):
    return 0

test_label_data_path = '/Users/zhangshijie/Desktop/SegTest-Data/Dataset/m/label'
test_img_path = '/Users/zhangshijie/Desktop/SegTest-Data/Dataset/m/image'

test_labels = sorted(glob.glob(test_label_data_path + "/*.png"))
test_inp = sorted(glob.glob(test_img_path + "/*.png"))
test = []
for x in zip(test_inp, test_labels):
    test.append(x)

n = len(test)
test_dataset = []

for i in range(n):
    test_dataset.append(test[i])

test_loader = torch.utils.data.DataLoader(test_dataset,
                                          batch_size=1,
                                          shuffle=True,
                                          num_workers=0)
x,y = next(iter(test_loader))
print(getImgName(x[0],8))
