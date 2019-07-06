import cv2
import numpy as np

if __name__=="__main__":

    #カメラ読み込み
    cap = cv2.VideoCapture(0)

    path = "/Users/k16104kk/MMLAB/研究室セミナー/kivy/"

    while True:
        #カメラ画像の取得
        ret, frame = cap.read()

        #左右反転
        #frame = cv2.flip(frame, 1)

        h = frame.shape[0]
        w = frame.shape[1]
        image_size = h*w

        #カメラサイズの変更
        re_frame = cv2.resize(frame,(15*w//32, 15*h//32))

        #カメラの表示
        cv2.imshow('Back', re_frame)
        cv2.moveWindow('Back', 500, 150)

        k = cv2.waitKey(1)

        #終了
        if k == 27: #escキー
            break

        #背景画像
        if k == 13:
            #画像を保存
            cv2.imwrite(path+"back.jpg",re_frame)

            #cv2.waitKey(0)
            cv2.destroyAllWindows()
