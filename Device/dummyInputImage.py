import socket
import cv2
import numpy
import os
import time
import threading

# 이미지 파일 경로
path = './in.jpg'

# IP , PORT
ip_add = '127.0.0.1'
port_num = 8989

# 서버의 IP와 PORT로 소켓연결을 신청
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip_add, port_num))

def send_data():
    fileNumber = input("Input file Number : ")
    fileName = r"./in" + str(fileNumber) + ".jpg"
    while True:
        # global fileName
        if os.path.isfile(fileName):
            # testText = test + str(n)

            time.sleep(1)

            # 이미지 파일 불러오기
            img_cv = cv2.imread(fileName)
            print(img_cv)

            # 추출한 이미지를 String 형태로 변환(인코딩)시키는 과정
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            result, imgencode = cv2.imencode('.jpg', img_cv, encode_param)
            data = numpy.array(imgencode)
            stringData = data.tobytes()

            # String 형태로 변환한 이미지를 socket을 통해서 전송
            sock.send(str.encode(str(len(stringData))).ljust(16))
            sock.send(stringData)
            sock.send(str(fileNumber).encode("utf-8"))

            # 이미지 삭제
            os.remove(fileName)

        else:
            fileNumber = input("Input file Number : ")
            fileName = r"./in" + str(fileNumber) + ".jpg"
    # 소켓 닫기
    sock.close()


send_thread = threading.Thread(target=send_data)
send_thread.start()

while True:
    pass