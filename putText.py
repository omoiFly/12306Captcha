import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, np.ndarray)):  #判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img)
        fontText = ImageFont.truetype('msyh.ttc', textSize, encoding="utf-8")
        draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
