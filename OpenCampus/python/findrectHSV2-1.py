#映像から特定色を認識し、範囲の外接矩形を取り囲む
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

#三角(赤)
def find_rect_of_target_color1(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]
    mask = np.zeros(h.shape, dtype=np.uint8)#マスクデータ生成
    mask[((h < 10) | (h > 245)) & (s > 120) & (v > 120)] = 250
    #輪郭抽出
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #面積が小さい輪郭を削除
    #area = img.shape[0] * img.shape[1]
    #contours = list(filter(lambda cnt: 1 < cv2.contourArea(cnt), contours))
    rects1 = []
    for contour in contours:
      approx = cv2.convexHull(contour)
      rect = cv2.boundingRect(approx)
      rects1.append(np.array(rect))
    return rects1

#長方形(茶)
def find_rect_of_target_color5(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]
    mask = np.zeros(h.shape, dtype=np.uint8)
    mask[((h > 0) & (h < 15)) & (s > 50) & (v < 220)] = 8
    #輪郭抽出
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    rects5 = []
    for contour in contours:
        approx = cv2.convexHull(contour)
        rect = cv2.boundingRect(approx)
        rects5.append(np.array(rect))
    return rects5

#半円(黄)
def find_rect_of_target_color2(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]
    mask = np.zeros(h.shape, dtype=np.uint8)
    mask[((h > 20) & (h < 40)) & (s > 100) & (v > 200)] = 30
    #輪郭抽出
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    rects2 = []
    for contour in contours:
        approx = cv2.convexHull(contour)
        rect = cv2.boundingRect(approx)
        rects2.append(np.array(rect))
    return rects2

#長方形(青)
def find_rect_of_target_color3(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]
    mask = np.zeros(h.shape, dtype=np.uint8)
    mask[((h > 150) & (h < 180)) & (s > 230) & (v < 200)] = 165
    #輪郭抽出
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    rects3 = []
    for contour in contours:
        approx = cv2.convexHull(contour)
        rect = cv2.boundingRect(approx)
        rects3.append(np.array(rect))
    return rects3

#正方形(緑)
def find_rect_of_target_color4(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]
    mask = np.zeros(h.shape, dtype=np.uint8)
    mask[((h > 120) & (h < 150)) & (s > 80) & (v < 100)] = 120
    #輪郭抽出
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    rects4 = []
    for contour in contours:
        approx = cv2.convexHull(contour)
        rect = cv2.boundingRect(approx)
        rects4.append(np.array(rect))
    return rects4



#直方体(紫)
def find_rect_of_target_color6(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]
    mask = np.zeros(h.shape, dtype=np.uint8)
    mask[((h > 177) & (h < 200)) & (s > 150) & (v < 150)] = 180
    #輪郭抽出
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    rects6 = []
    for contour in contours:
        approx = cv2.convexHull(contour)
        rect = cv2.boundingRect(approx)
        rects6.append(np.array(rect))
    return rects6

#if __name__ == "__main__":
def hantei():
    #img = cv2.imread('./back.jpg')
    img = cv2.imread('./data/img.png')
    #img = cv2.imread('./odai1.jpg')
    #赤
    rects1 = find_rect_of_target_color1(img)
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
    rects2 = find_rect_of_target_color2(img)
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
    rects3 = find_rect_of_target_color3(img)
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
    rects4 = find_rect_of_target_color4(img)
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
    rects5 = find_rect_of_target_color5(img)
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
    rects6 = find_rect_of_target_color6(img)
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
    if (red == 1 and  blue == 0 and green == 1 and
        purple == 0 and yellow  == 0 and brown == 1):
        count = count + 3
    print(count)
    #アスペクト比
    if (asp1 >= 1.8 and asp1<=2.0 and asp2 == 0.0 and asp3 == 0 and
        asp4 >= 0.87 and asp4<=1.0 and asp5 >= 4 and asp5 <= 4.40 and asp6 == 0):
        count = count + 2
    print(count)
    #面積
    if (his1 >= 26000 and his1 <= 28000 and his2 == 0 and his3 == 0 and
        his4 >= 14000 and his4 <= 18000 and his5 >= 15500 and his5 <= 18000 and his6 == 0):
        count = count + 1
    print(count)
    #距離
    if (hisax1 == 0 and hisax2 == 0 and hisax3 >= -49 and hisax3 <= 51 and
        hisax4 >= -47 and hisax4<= 53 and hisax5 == 0 and
        hisay1 == 0 and hisay2 == 0 and hisay3 >= -238.5 and hisay3 <= -138.5 and
        hisay4 >= -142.5 and hisay4 <= -42.5 and hisay5 == 0):
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
