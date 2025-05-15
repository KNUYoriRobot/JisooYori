# ROS Bridge
ROS와 비-ROS 시스템 간의 통신을 가능하게 해주는 인터페이스이다. 처음에는 뭔가 오해가 있었는데, 후술할 내용을 보면 꼭 ROS끼리만의 통신이 아니라는 것을 확실히 알 수 있다.

## 주요 역할:
1. 웹소켓 기반 통신: ROS 메시지를 WebSocket 프로토콜을 통해 JSON 형식으로 변환합니다
2. 비-ROS 클라이언트 지원: 웹 브라우저, JavaScript 애플리케이션, Python 등 ROS가 설치되지 않은 환경에서도 ROS와 통신 가능
3. 원격 인터페이스: 로봇과 원격 클라이언트 간의 통신 브리지 역할
4. 크로스 플랫폼 지원: 다양한 운영 체제와 플랫폼에서 ROS 시스템에 접근 가능

아래의 코드는 ROS Bridge를 통해 수신한 Topic을 rostopic을 받아서 echo 하듯이 출력할 수 있게 하는 코드이다.

## 실행 방법
1. 우선 `rosbridge_echo.py`를 원하는 위치에 저장한다.

2. 스크립트를 사용 가능하게 만든다:

    ```bash
    chmod +x rosbridge_echo.py
    ```

3. 이걸 실행하고 나면 다음과 같이 사용 가능하다:

    ```bash
    # 기본 사용법 (ROS Bridge 서버가 localhost:9090에 있는 경우)
    ./rosbridge_echo.py /robot/{토픽_이름}

    # 원격 서버와 특정 메시지 타입 지정
    ./rosbridge_echo.py /robot/{토픽_이름} --host 100.83.142.42 --msg-type {토픽_type}
    ```

### 배쉬 별칭으로 편하게 사용하기

더 편리하게 사용하기 위해 배쉬 별칭을 설정:

```bash
# ~/.bashrc 파일에 추가
alias rb_echo='python3 {script_저장_위치}rosbridge_echo.py'
```

그런 다음 터미널에서 다음과 같이 사용하면 된다:

```bash
source ~/.bashrc
rb_echo /robot/end_effector_pose --host {host_ip}
```

## 다양한 토픽과 메시지 타입 지원

이 스크립트는 기본적으로 모든 ROS 토픽과 메시지 타입을 지원한다. 메시지 타입을 지정하지 않으면 자동으로 발견하려고 시도한다. 만약 자동 발견이 실패하면 `--msg-type` 인자로 직접 지정해야 한다.

## 참고

1. 이 스크립트는 ROS Bridge 서버의 WebSocket 인터페이스를 통해 통신한다.
2. ROS Bridge 서버는 Ubuntu 20.04(ROS Noetic)에서 실행 중이어야 한다.
3. 네트워크 방화벽 설정으로 인해 연결 문제가 발생할 수 있다. 이 경우 방화벽 설정을 확인하기.
4. 이 스크립트는 `rostopic echo`와 유사하지만 완전히 동일한 출력 형식을 제공하지는 않는다. 대신 JSON 형식으로 출력한다.

## 실행 영상
![alt text](ROSBridgeEcho.mp4)