 #映像から特定色を認識し、範囲の外接矩形を取り囲む
import cv2
import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.patches import Polygon

#H1,H2,AND OR,SMAX,V,MAX OR MIN,NUM
#2  >:TRUE  <:FALSE
#5  AND:True  OR:False
class find_rect_of_target():
    #三角(赤)
    h = [];
    s = [];
    v = [];
    def mask_num(self,mask,h):
        return mask;


    def find_rect_of_target(self,image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
        self.h = hsv[:, :, 0]
        self.s = hsv[:, :, 1]
        self.v = hsv[:, :, 2]
        mask = np.zeros(self.h.shape, dtype=np.uint8)

        mask = self.mask_num(mask)

        #輪郭抽出
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #面積が小さい輪郭を削除
        #area = img.shape[0] * img.shape[1]
        #contours = list(filter(lambda cnt: 1 < cv2.contourArea(cnt), contours))
        rects = []
        for contour in contours:
          approx = cv2.convexHull(contour)
          rect = cv2.boundingRect(approx)
          rects.append(np.array(rect))
        return rects

class color1(find_rect_of_target ):
    #赤
    #HSV = 256;1256;256
    def mask_num(self,mask):
        #mask[((self.h < 15) & (self.h > 0)) & (self.s > 220) & (self.v > 120)] = 250
        mask[((self.h > 220) | (self.h < 7)) & (self.s > 180) ] = 250
        return mask;


class color2(find_rect_of_target ):
    #黄色
    def mask_num(self,mask):
        mask[((self.h > 20) & (self.h < 40)) & (self.s > 100) & (self.v > 200)] = 30
        return mask;


class color3(find_rect_of_target ):
    #青
    def mask_num(self,mask):
        mask[((self.h > 150) & (self.h < 180)) & (self.s > 230) & (self.v < 200)] = 165
        return mask;


class color4(find_rect_of_target ):
    #緑
    def mask_num(self,mask):
        #mask[((self.h > 120) & (self.h < 150)) & (self.s > 80) & (self.v < 100)] = 120
        mask[((self.h > 113) & (self.h < 143)) & (self.s > 20)] = 120
        #cv2.imwrite("./data/dst.jpg",mask)
        return mask;


class color5(find_rect_of_target ):
    #茶
    def mask_num(self,mask):
        #mask[((self.h > 0) & (self.h < 15)) & (self.s > 50) & (self.v < 220)] = 8
        mask[((self.h > 0) & (self.h < 15)) & (self.s > 100) & (self.s < 180) ] = 8
        return mask;


class color6(find_rect_of_target ):
    #紫
    def mask_num(self,mask):
        mask[((self.h > 177) & (self.h < 200)) & (self.s > 150) & (self.v < 150)] = 180
        return mask;


class put_result_color():
    def __init__():
        img = cv2.imread('./img.jpg')
        w1 = 0
        h1 = 0
        asp1 = 0
        s1 = 0
        cx1 = 0
        cy1 = 0
        red = 0

#class hantei_pr():
#        #img = cv2.imread('./back.jpg')
#        img = cv2.imread('./data/img.jpg')
#
#        #赤
#        rects = color1().find_rect_of_target(img)
#        if len(rects) > 10:
#            rect = max(rects, key=(lambda x: x[2] * x[3]))
#            cv2.rectangle(img, tuple(rect[0:2]),
#            tuple(rect[0:2] + rect[2:4]), (0, 0, 255), 2)
#                                         # B  G   R
#            w,h = rect[2],rect[3] # 幅と高さ
#            s = w * h   # 面積
#            asp = w / h # アスペクト比
#            cx = rect[0]+(w/2) #中心のx座標
#            cy = rect[1]+(h/2) #中心のy座標
#            red = 1
#
#            print('赤------------')
#            print(str(red) + '個')
#            print('縦 = ' + str(w))
#            print('横 = ' + str(h))
#            print('アスペクト比 = ' + str(asp))
#            print('面積 = ' + str(s))
#            print('中心座標 = (' + str(cx) + ',' + str(cy) + ')')
#
#            cv2.putText(img, "area  : " + str(s),
#            (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
#            cv2.putText(img, "aspect: " + str(asp),
#            (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
#        else: #なかった場合
#            w = 0
#            h = 0
#            asp = 0
#            s = 0
#            cx = 0
#            cy = 0
#            red = 0
#            print('赤------------')
#            print(str(red) + '個')
#            print('縦 = ' + str(w))
#            print('横 = ' + str(h))
#            print('アスペクト比 = ' + str(asp))
#            print('面積 = ' + str(s))
#            print('中心座標 = (' + str(cx) + ',' + str(cy) + ')')


#if __name__ == "__main__":
def hantei():
    img = cv2.imread('./data/img.png')
    #img = cv2.imread('./data/case/3562.jpg')
    #img = cv2.imread('./data/case/4727.jpg')

    #赤
    rects1 = color1().find_rect_of_target(img)
    if len(rects1) > 10:
        rect = max(rects1, key=(lambda x: x[2] * x[3]))
        cv2.rectangle(img, tuple(rect[0:2]),
        tuple(rect[0:2] + rect[2:4]), (0, 0, 255), 2)
                                     # B  G   R
        w1,h1 = rect[2],rect[3] # 幅と高さ
        s1 = w1 * h1   # 面積
        asp1 = w1 / h1 # アスペクト比
        cx1 = rect[0]+(w1/2) #中心のx座標
        cy1 = rect[1]+(h1/2) #中心のy座標
        red = 1

        print('赤------------')
        print(str(red) + '個')
        print('縦 = ' + str(w1))
        print('横 = ' + str(h1))
        print('アスペクト比 = ' + str(asp1))
        print('面積 = ' + str(s1))
        print('中心座標 = (' + str(cx1) + ',' + str(cy1) + ')')

        cv2.putText(img, "area  : " + str(s1),
        (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
        cv2.putText(img, "aspect: " + str(asp1),
        (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
    else: #なかった場合
        w1 = 0
        h1 = 0
        asp1 = 0
        s1 = 0
        cx1 = 0
        cy1 = 0
        red = 0
        print('赤------------')
        print(str(red) + '個')
        print('縦 = ' + str(w1))
        print('横 = ' + str(h1))
        print('アスペクト比 = ' + str(asp1))
        print('面積 = ' + str(s1))
        print('中心座標 = (' + str(cx1) + ',' + str(cy1) + ')')


    #黄
    rects2 = color2().find_rect_of_target(img)
    if len(rects2) > 10:
        rect = max(rects2, key=(lambda x: x[2] * x[3]))
        cv2.rectangle(img, tuple(rect[0:2]),
        tuple(rect[0:2] + rect[2:4]), (0, 255, 255), 2)

        w2,h2 = rect[2],rect[3] # 幅と高さ
        s2 = w2 * h2   # 面積
        asp2 = w2 / h2 # アスペクト比
        cx2 = rect[0]+(w2/2) #中心のx座標
        cy2 = rect[1]+(h2/2) #中心のy座標
        yellow = 1

        print('黄------------')
        print(str(yellow) + '個')
        print('縦 = ' + str(w2))
        print('横 = ' + str(h2))
        print('アスペクト比 = ' + str(asp2))
        print('面積 = ' + str(s2))
        print('中心座標 = (' + str(cx2) + ',' + str(cy2) + ')')

        cv2.putText(img, "area  : " + str(s2),
        (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255))
        cv2.putText(img, "aspect: " + str(asp2),
        (0, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255))
    else: #なかった場合
        w2 = 0
        h2 = 0
        asp2 = 0
        s2 = 0
        cx2 = 0
        cy2 = 0
        yellow = 0
        print('黄------------')
        print(str(yellow) + '個')
        print('縦 = ' + str(w2))
        print('横 = ' + str(h2))
        print('アスペクト比 = ' + str(asp2))
        print('面積 = ' + str(s2))
        print('中心座標 = (' + str(cx2) + ',' + str(cy2) + ')')

    #青
    rects3 = color3().find_rect_of_target(img)
    if len(rects3) > 100:
        rect = max(rects3, key=(lambda x: x[2] * x[3]))
        cv2.rectangle(img, tuple(rect[0:2]),
        tuple(rect[0:2] + rect[2:4]), (255, 0, 0), 2)

        w3,h3 = rect[2],rect[3] # 幅と高さ
        s3 = w3 * h3   # 面積
        asp3 = w3 / h3 # アスペクト比
        cx3 = rect[0]+(w3/2) #中心のx座標
        cy3 = rect[1]+(h3/2) #中心のy座標
        blue = 1

        print('青------------')
        print(str(blue) + '個')
        print('縦 = ' + str(w3))
        print('横 = ' + str(h3))
        print('アスペクト比 = ' + str(asp3))
        print('面積 = ' + str(s3))
        print('中心座標 = (' + str(cx3) + ',' + str(cy3) + ')')

        cv2.putText(img, "area  : " + str(s3),
        (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
        cv2.putText(img, "aspect: " + str(asp3),
        (0, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
    else: #なかった場合
        w3 = 0
        h3 = 0
        asp3 = 0
        s3 = 0
        cx3 = 0
        cy3 = 0
        blue = 0
        print('青------------')
        print(str(blue) + '個')
        print('縦 = ' + str(w3))
        print('横 = ' + str(h3))
        print('アスペクト比 = ' + str(asp3))
        print('面積 = ' + str(s3))
        print('中心座標 = (' + str(cx3) + ',' + str(cy3) + ')')

    #緑
    rects4 = color4().find_rect_of_target(img)
    if len(rects4) > 10:
        rect = max(rects4, key=(lambda x: x[2] * x[3]))
        cv2.rectangle(img, tuple(rect[0:2]),
        tuple(rect[0:2] + rect[2:4]), (0, 255, 0), 2)

        w4,h4 = rect[2],rect[3] # 幅と高さ
        s4 = w4 * h4   # 面積
        asp4 = w4 / h4 # アスペクト比
        cx4 = rect[0]+(w4/2) #中心のx座標
        cy4 = rect[1]+(h4/2) #中心のy座標
        green = 1

        print('緑------------')
        print(str(green) + '個')
        print('縦 = ' + str(w4))
        print('横 = ' + str(h4))
        print('アスペクト比 = ' + str(asp4))
        print('面積 = ' + str(s4))
        print('中心座標 = (' + str(cx4) + ',' + str(cy4) + ')')

        cv2.putText(img, "area  : " + str(s4),
        (0, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
        cv2.putText(img, "aspect: " + str(asp4),
        (0, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    else: #なかった場合
        w4 = 0
        h4 = 0
        asp4 = 0
        s4 = 0
        cx4 = 0
        cy4 = 0
        green = 0
        print('緑------------')
        print(str(green) + '個')
        print('縦 = ' + str(w4))
        print('横 = ' + str(h4))
        print('アスペクト比 = ' + str(asp4))
        print('面積 = ' + str(s4))
        print('中心座標 = (' + str(cx4) + ',' + str(cy4) + ')')

    #茶
    rects5 = color5().find_rect_of_target(img)
    if len(rects5) > 10:
        rect = max(rects5, key=(lambda x: x[2] * x[3]))
        cv2.rectangle(img, tuple(rect[0:2]),
        tuple(rect[0:2] + rect[2:4]), (41, 66, 115), 2)

        w5,h5 = rect[2],rect[3] # 幅と高さ
        s5 = w5 * h5   # 面積
        asp5 = w5 / h5 # アスペクト比
        cx5 = rect[0]+(w5/2) #中心のx座標
        cy5 = rect[1]+(h5/2) #中心のy座標
        brown = 1

        print('茶------------')
        print(str(brown) + '個')
        print('縦 = ' + str(w5))
        print('横 = ' + str(h5))
        print('アスペクト比 = ' + str(asp5))
        print('面積 = ' + str(s5))
        print('中心座標 = (' + str(cx5) + ',' + str(cy5) + ')')

        cv2.putText(img, "area  : " + str(s5),
        (0, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (41, 66, 115))
        cv2.putText(img, "aspect: " + str(asp5),
        (0, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (41, 66, 115))
    else: #なかった場合
        w5 = 0
        h5 = 0
        asp5 = 0
        s5 = 0
        cx5 = 0
        cy5 = 0
        brown = 0
        print('茶------------')
        print(str(brown) + '個')
        print('縦 = ' + str(w5))
        print('横 = ' + str(h5))
        print('アスペクト比 = ' + str(asp5))
        print('面積 = ' + str(s5))
        print('中心座標 = (' + str(cx5) + ',' + str(cy5) + ')')

    #紫
    rects6 = color6().find_rect_of_target(img)
    if len(rects6) > 10:
        rect = max(rects6, key=(lambda x: x[2] * x[3]))
        cv2.rectangle(img, tuple(rect[0:2]),
        tuple(rect[0:2] + rect[2:4]), (153, 0, 102), 2)

        w6,h6 = rect[2],rect[3] # 幅と高さ
        s6 = w6 * h6   # 面積
        asp6 = w6 / h6 # アスペクト比
        cx6 = rect[0]+(w6/2) #中心のx座標
        cy6 = rect[1]+(h6/2) #中心のy座標
        purple = 1

        print('紫------------')
        print(str(purple) + '個')
        print('縦 = ' + str(w6))
        print('横 = ' + str(h6))
        print('アスペクト比 = ' + str(asp6))
        print('面積 = ' + str(s6))
        print('中心座標 = (' + str(cx6) + ',' + str(cy6) + ')')

        cv2.putText(img, "area  : " + str(s6),
        (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (153, 0, 102))
        cv2.putText(img, "aspect: " + str(asp6),
        (0, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (153, 0, 102))
    else:  #なかった場合
        w6 = 0
        h6 = 0
        asp6 = 0
        s6 = 0
        cx6 = 0
        cy6 = 0
        purple = 0
        print('紫------------')
        print(str(purple) + '個')
        print('縦 = ' + str(w6))
        print('横 = ' + str(h6))
        print('アスペクト比 = ' + str(asp6))
        print('面積 = ' + str(s6))
        print('中心座標 = (' + str(cx6) + ',' + str(cy6) + ')')

    if s1 == 0:
        s1 = s1+0.1


    count = 0
    #比の計算
    hi = s1 / 26904
    print(hi)

    #比を用いて問題の値に合わせる
    his1 = s1 / hi
    his2 = s2 / hi
    his3 = s3 / hi
    his4 = s4 / hi
    his5 = s5 / hi
    his6 = s6 / hi




    #積み木間の計算と比の計算(x座標)
    if cx2 == 0:
        sax1 = 0
        hisax1 = 0
    else:
        sax1 = cx1 - cx2
        hisax1 = sax1 / hi

    if cx3 == 0:
        sax2 = 0
        hisax2 = 0
    else:
        sax2 = cx1 - cx3
        hisax2 = sax2 / hi

    if cx4 == 0:
        sax3 = 0
        hisax3 = 0
    else:
        sax3 = cx1 - cx4
        hisax3 = sax3 / hi

    if cx5 == 0:
        sax4 = 0
        hisax4 = 0
    else:
        sax4 = cx1 - cx5
        hisax4 = sax4 / hi

    if cx6 == 0:
        sax5 = 0
        hisax5 = 0
    else:
        sax5 = cx1 - cx4
        hisax5 = sax5 / hi

    #積み木間の計算と比の計算(y座標)
    if cy2 == 0:
        say1 = 0
        hisay1 = 0
    else:
        say1 = cy1 - cy2
        hisay1 = say1 / hi

    if cy3 == 0:
        say2 = 0
        hisay2 = 0
    else:
        say2 = cy1 - cy3
        hisay2 = say2 / hi

    if cy4 == 0:
        say3 = 0
        hisay3 = 0
    else:
        say3 = cy1 - cy4
        hisay3 = say3 / hi

    if cy5 == 0:
        say4 = 0
        hisay4 = 0
    else:
        say4 = cy1 - cy5
        hisay4 = say4 / hi

    if cy6 == 0:
        say5 = 0
        hisay5 = 0
    else:
        say5 = cy1 - cy4
        hisay5 = say5 / hi

    print('x座標------------')
    print(sax1)
    print(sax2)
    print(sax3)
    print(sax4)
    print(sax5)
    print('y座標------------')
    print(say1)
    print(say2)
    print(say3)
    print(say4)
    print(say5)


    print('x座標------------')
    print(hisax1)
    print(hisax2)
    print(hisax3)
    print(hisax4)
    print(hisax5)
    print('y座標------------')
    print(hisay1)
    print(hisay2)
    print(hisay3)
    print(hisay4)
    print(hisay5)


    #判定(デモ実装だけのため値は固定値になっている)
    #色の数
    #if (red == 1 and  blue == 0 and green == 1 and
    #    purple == 0 and yellow  == 0 and brown == 1):
    if (red == 1 and   green == 1 and brown == 1):
        count = count + 3
    print(count)
    #アスペクト比
    #if (asp1 >= 1.8 and asp1<=2.2 and asp2 == 0.0 and asp3 == 0 and
    #    asp4 >= 0.87 and asp4<=1.2 and asp5 >= 3. and asp5 <= 4.70 and asp6 == 0):
    if (asp1 >= 1.8 and asp1<=2.2 and
        asp4 >= 0.87 and asp4<=1.2 and asp5 >= 3. and asp5 <= 5.00):
        count = count + 2
    print(count)
    #面積
    #if (his1 >= 26000 and his1 <= 28000 and his2 == 0 and his3 == 0 and
    #    his4 >= 14000 and his4 <= 18000 and his5 >= 15500 and his5 <= 18000 and his6 == 0):
    if (his1 >= 26000 and his1 <= 28000 and his4 >= 14000 and his4 <= 18000 and his5 >= 15500 and his5 <= 18000):
        count = count + 1
    print(count)
    #距離
    #if (hisax1 == 0 and hisax2 == 0 and hisax3 >= -49 and hisax3 <= 51 and
    #    hisax4 >= -47 and hisax4<= 53 and hisax5 == 0 and
    #    hisay1 == 0 and hisay2 == 0 and hisay3 >= -238.5 and hisay3 <= -138.5 and
    #    hisay4 >= -142.5 and hisay4 <= -42.5 and hisay5 == 0):
    if (hisax3 >= -49 and hisax3 <= 51 and
        hisax4 >= -47 and hisax4<= 53 and
        hisay3 >= -238.5 and hisay3 <= -138.5 and
        hisay4 >= -142.5 and hisay4 <= -42.5):
        count = count + 1
    print(count)

    #cv2.imshow('findrect', img)
    #cv2.moveWindow('findrect', 500, -100)
    #k = cv2.waitKey(0)
    #if k == ord('q'):
    #    cv2.destroyAllWindows()
    #if k == ord('s'):
    cv2.imwrite('./findrect.jpg', img)
    #    cv2.destroyAllWindows()

    return(count)
