#!/usr/bin/env python3
import roslibpy
import argparse
import json
import signal
import sys

def signal_handler(sig, frame):
    print("\nDisconnecting from ROS Bridge server...")
    if 'listener' in globals() and listener is not None:
        listener.unsubscribe()
    if 'client' in globals() and client is not None and client.is_connected:
        client.terminate()
    sys.exit(0)

# Ctrl+C 핸들링
signal.signal(signal.SIGINT, signal_handler)

# 인자 파싱
parser = argparse.ArgumentParser(description='Subscribe to ROS topic via ROS Bridge')
parser.add_argument('topic', help='Topic name to subscribe')
parser.add_argument('--host', default='localhost', help='ROS Bridge server host (default: localhost)')
parser.add_argument('--port', type=int, default=9090, help='ROS Bridge server port (default: 9090)')
parser.add_argument('--msg-type', default=None, help='Message type (optional, will attempt to auto-discover if not provided)')
args = parser.parse_args()

# ROS Bridge 클라이언트 설정
print(f"Connecting to ROS Bridge server at {args.host}:{args.port}...")
client = roslibpy.Ros(host=args.host, port=args.port)
client.run()
print(f"Connected to ROS Bridge server at {args.host}:{args.port}")

# 메시지 타입이 제공되지 않은 경우 자동 발견 시도
if args.msg_type is None:
    try:
        # 토픽 정보 요청
        service = roslibpy.Service(client, '/rosapi/topic_type', 'rosapi/TopicType')
        request = roslibpy.ServiceRequest({'topic': args.topic})
        result = service.call(request)
        args.msg_type = result['type']
        print(f"Discovered message type: {args.msg_type}")
    except Exception as e:
        print(f"Error discovering message type: {e}")
        print("Please provide message type with --msg-type argument")
        client.terminate()
        sys.exit(1)

# 메시지 콜백
def topic_callback(message):
    # JSON 형식으로 예쁘게 출력
    print(json.dumps(message, indent=2))
    print("---")

# 토픽 구독
print(f"Subscribing to topic: {args.topic} (type: {args.msg_type})")
listener = roslibpy.Topic(client, args.topic, args.msg_type)
listener.subscribe(topic_callback)

print("Listening for messages. Press Ctrl+C to exit.")

# 계속 실행 (Ctrl+C로 종료될 때까지)
signal.pause()