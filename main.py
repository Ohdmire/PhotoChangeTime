
# from PIL import Image
# import piexif

# filename="IMG_20190204_221537.jpg"

# im = Image.open(filename)
# exif_dict = piexif.load(im.info["exif"])
# print (exif_dict['Exif'])

import until
from exif import Image
import os

filepath=input("请拖入文件夹后回车")
for filename in os.listdir(filepath):
    if until.is_img:
        with open(filename, 'rb') as image_file:
            my_image = Image(image_file)
            result=my_image.datetime
            r=until.modifyFileTime(filePath=filename,createTime=result,modifyTime=result,accessTime=result,offset=(0, 1, 2))
            if r:
                print(filename+"成功")
            else:
                print("写入文件失败")
    else:
        print(filename+"不是图片文件")



 
