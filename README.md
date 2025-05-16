# JisooYori

Setup 과정과 실행 방법. 여기서 host는 20.04, client는 22.04를 말한다.

## Ubuntu 20.04 Docker

1. quest_noetic_bridge image file pull하기

   ```bash
   docker pull jisoosong/quest_noetic_bridge:latest
   ```
   
   ```bash
   docker run -it --name meta \
     --net=host \
     --privileged \
     -v /tmp/.X11-unix:/tmp/.X11-unix \
     -e DISPLAY=$DISPLAY \
     jisoosong/quest_noetic_bridge:latest
   ```
   
1. catkin build

   ```bash
   cd workspace/catkin_ws
   catkin build
   ```
   
   ```bash
   source ~/.bashrc
   ```
   
1. Quest2ROS 실행

   1) ROS TCP endpoint 실행

      ```bash
      roslaunch ros_tcp_endpoint endpoint.launch tcp_ip:=<host_ip> tcp_port:=10000
      ```

   1) ros2quest 실행

      ```bash
      rosrun quest2ros ros2quest.py
      ```

   1) ROS Bridge Server 실행

      ```bash
      roslaunch rosbridge_server rosbridge_websocket.launch
      ```

## Ubuntu 22.04 PC

1. [`/ros_bridge/README.md`](https://github.com/KNUYoriRobot/JisooYori/tree/main/ros_bridge)의 step을 따라 초기 설정

1. 수신한 topic을 echo

   ```bash
   rb_echo /robot/<topic_name> --host <host_ip>
   ```
