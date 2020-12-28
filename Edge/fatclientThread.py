import os
import socket
import threading
import cv2
import numpy
import time
import detect

# TCP소켓 열고 수신 대기
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 생성
server_socket.bind(('127.0.0.1', 8989))  # 서버의 IP와 포트 연결
server_socket.listen(0)  # 서버의 포트를 LISTNING 상태로 변경
client_socket, addr = server_socket.accept()


# socket 수신 버퍼를 읽어서 반환하는 함수
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def recv_data():
    while True:

        # String형의 이미지를 수신받아서 이미지로 변환 하고 화면에 출력
        length = recvall(client_socket, 16)  # 길이 16의 데이터를 먼저 수신하는 것은 여기에 이미지의 길이를 먼저 받아서 이미지를 받을 때 편리하려고 하는 것이다.
        stringData = recvall(client_socket, int(length))
        img = numpy.frombuffer(stringData, dtype='uint8')
        imgNumber = recvall(client_socket, 1)

        # 이미지 변수명
        saveImagePath = './in'
        inFileName = saveImagePath + imgNumber.decode('utf-8') + '.jpg'
        outFileName = 'out' + imgNumber.decode('utf-8') + '.jpg'

        # 이미지 디코딩후 현제 디렉토리 아래 .jpg로 저장
        decimg = cv2.imdecode(img, 1)
        cv2.imwrite(inFileName, decimg)


        #분석 모델로 이미지 전송 및 실행
        time.sleep(1)
        if os.path.isfile(inFileName):
            detect.activator(inFileName, 'weights.npz', outFileName)
            # inFileName, weights.npz, outFileName
        else:
            pass

        # print(saveImagePath + imgNumber.decode('utf-8') + '.jpg')

        # decimg = cv2.imdecode(img, 1)
        # cv2.imshow('SERVER', decimg)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    client_socket.close()


# def send_data():
#     while True:
#         data = input("보낼 데이터 입력 : ")
#         client_socket.send(data.encode("utf-8"))
#     client_socket.close()

# def imageDataSave():


recv_thread = threading.Thread(target=recv_data)
recv_thread.start()
# send_thread = threading.Thread(target=send_data)
# send_thread.start()

while True:
    pass
