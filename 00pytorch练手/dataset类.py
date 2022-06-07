from torch.utils.data import  Dataset
from PIL import  Image
import os

class MyData(Dataset):

    def __init__(self,root_dir,label_dir):
        self.root_dir = root_dir ##声明类内函数全局变量、类的属性，相当于C的public：
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir,self.label_dir)
        self.img_path = os.listdir(self.path)
    def __getitem__(self,idx):
        imag_name = self.img_path[idx]
        imag_item_path = os.path.join(self.root_dir,self.label_dir,imag_name)
        imag = Image.open(imag_item_path)
        label  = self.label_dir
        return imag,label
    def __len__(self):
        return len(self.img_path)

