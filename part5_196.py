import socket

# HOST에는 서버의 IP주소를, PORT에는 서버의 포트번호를 각각 지정
HOST = 'localhost' # 에코 클라이언트가 서버와 동일한 컴퓨터에서 실행되면 HOST의 값으로 'localhost'를 설정
PORT = 9009

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # TCP 소켓을 생성하고 sock로 지정
    sock.connect((HOST, PORT)) # (HOST, PORT)에 해당하는 원격 호스트로 연결을 시도 -> 서버의 accept()에서 수락하면 클라이언트와 서버가 연결됨

    while True:
        msg = input('메시지 입력: ') # 사용자로부터 메시지를 입력받고 msg에 대입
        if msg == '/quit': # 사용자가 '/quit'을 입력하면 반복문을 종료
            sock.sendall(msg.encode())
            break

        sock.sendall(msg.encode()) # 사용자로부터 입력받은 메시지인 msg를 msg.encode()로 바이트 스트림으로 인코딩하고 소켓의 sendall()을 이용해 서버로 전송
        data = sock.recv(1024) # 서버가 전송하는 데이터를 수신
        print('에코 서버로부터 받은 데이터[%s]'%data.decode())
        
print('클라이언트 종료')