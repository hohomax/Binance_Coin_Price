import json
import websocket


def on_message(ws, message):
    data = json.loads(message)
    if data['s'] == 'BTCUSDT':
        print(f"BTC Price: {data['c']}")
    elif data['s'] == 'ETHUSDT':
        print(f"ETH Price: {data['c']}")


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    print("### opened ###")
    params = {
        "method": "SUBSCRIBE",
        "params": [
            "btcusdt@ticker",
            "ethusdt@ticker"
        ],
        "id": 1
    }
    ws.send(json.dumps(params))


if __name__ == "__main__":
    # websocket-client 라이브러리의 트레이스를 활성화
    websocket.enableTrace(True)

    # WebSocketApp 인스턴스 생성
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    # 웹소켓을 실행하여 무한히 데이터를 받음
    ws.run_forever()