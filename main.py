import until
from exif import Image
import pathlib

extlist=[".png",".jpg",".jpeg",".bmp"]
success=[]
fail=[]

filedir=input("请拖入文件夹后回车")
path=pathlib.Path(filedir)
for i in path.glob("**/*"):
    if i.suffix in extlist:
        filepath=str(i)
        with open(filepath, 'rb') as image_file:
            try:
                my_image = Image(image_file)
                result=my_image.datetime
            except:
                print("没有找到相关信息")
                result=""
        r=until.modifyFileTime(filePath=filepath,createTime=result,modifyTime=result,accessTime=result,offset=(0, 1, 2))
        if r:
            print(filepath+"成功")
            success.append(filepath)
        else:
            print("写入文件失败"+filepath)
            fail.append(filepath)

print("成功",success)
print("失败",fail)

 
