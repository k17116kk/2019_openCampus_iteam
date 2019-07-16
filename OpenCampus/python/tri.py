import cv2
import numpy as np

if __name__=="__main__":

    path = "./data/"

    tsumiki = cv2.imread(path + "tsumiki.png",1)

    #トリミング
    tri = tsumiki[0:220,100:300]

    #保存
    cv2.imwrite(path+"tri.png",tri)
