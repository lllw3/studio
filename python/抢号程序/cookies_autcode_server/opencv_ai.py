import cv2
from PIL import Image
import numpy as np
import random

def open_cv(picId):
#     imgURL = "output/cap.png"
#     im = Image.open(imgScreenShootUrl)
# #     im = im.crop((118,731,950,1189))  # 对浏览器截图进行裁剪
#     im = im.crop((121,869,952,1333))
#     im.save(imgURL)
    ####
    faceCascade = cv2.CascadeClassifier("Resources/mycascade.xml")
    img = cv2.imread('output\captcha{}.png'.format(picId))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    get_X = 0
    temp = 0
    for (x, y, w, h) in faces:
        if w*h > temp:
            xz = x
            yz = y
            wz = w
            hz = h
            temp = w*h
            get_X = x
    cv2.rectangle(img, (xz, yz), (xz + wz, yz + hz), (0, 255, 0), 1)
    # cv2.imshow("img", img)
    # cv2.waitKey(0)
    pointX = get_X*0.36
    return (pointX,get_track(pointX))

def get_track(pointX):
    '''
    拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
    匀变速运动基本公式：
    ①v=v0+at
    ②s=v0t+(1/2)at²
    ③v²-v0²=2as

    :param self.X: 需要移动的距离
    :return: 存放每0.2秒移动的距离
    '''
    # 初速度
    v=0
    # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
    t=0.3
    # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
    tracks=[]
    # 当前的位移
    current=0
    # 到达mid值开始减速
    mid=pointX * 5/8
    pointX += 10  # 先滑过一点，最后再反着滑动回来
    # a = random.randint(1,3)
    while current < pointX:
        if current < mid:
            # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
            a = random.randint(1,3)  # 加速运动
        else:
            a = -random.randint(2,4) # 减速运动
        # 初速度
        v0 = v
        # 0.2秒时间内的位移
        s = v0*t+0.5*a*(t**2)
        # 当前的位置
        current += s
        # 添加到轨迹列表
        tracks.append(round(s))
        # 速度已经达到v,该速度作为下次的初速度
        v= v0+a*t
    # 反着滑动到大概准确位置
    for i in range(4):
        tracks.append(-random.randint(1,3))
    
    random.shuffle(tracks)
    return tracks

if __name__=='__main__':
    pointX,tracks = open_cv(1)
    print(pointX)