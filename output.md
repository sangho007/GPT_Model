

라즈베리파이에서 아두이노를 제어하기 위해 Python을 사용하는 예제 코드를 제공하겠습니다. 이 과정에서 가장 일반적인 방법은 시리얼 통신을 사용하는 것입니다. 아두이노와 라즈베리파이 사이의 시리얼 통신을 위해, 먼저 아두이노에 시리얼 통신을 위한 코드를 업로드해야 하고, 그 다음 라즈베리파이에서 Python을 사용하여 아두이노와 통신하는 코드를 작성해야 합니다.

### 1. 아두이노 코드

아두이노 IDE를 열고, 아래의 코드를 아두이노에 업로드합니다. 이 코드는 아두이노가 시리얼 포트를 통해 받은 데이터를 확인하고, 만약 '1'을 받으면 LED를 켜고, '0'을 받으면 LED를 끄는 간단한 예제입니다.

```cpp
int ledPin = 13; // LED를 연결한 핀 번호

void setup() {
  pinMode(ledPin, OUTPUT); // LED 핀을 출력으로 설정
  Serial.begin(9600); // 시리얼 통신 속도를 9600bps로 설정
}

void loop() {
  if (Serial.available() > 0) { // 시리얼 포트를 통해 데이터가 수신됐는지 확인
    char received = Serial.read(); // 데이터 읽기
    if (received == '1') {
      digitalWrite(ledPin, HIGH); // LED 켜기
    } else if (received == '0') {
      digitalWrite(ledPin, LOW); // LED 끄기
    }
  }
}
```

### 2. 라즈베리파이 Python 코드

라즈베리파이에서는 PySerial 라이브러리를 사용하여 시리얼 통신을 구현할 수 있습니다. 먼저 PySerial을 설치해야 합니다. 터미널을 열고 다음 명령어를 입력하여 설치합니다.

```bash
pip install pyserial
```

설치가 완료되면, 아래의 Python 코드를 작성합니다. 이 코드는 시리얼 포트를 통해 아두이노에 '1' 또는 '0'을 보내어 LED를 제어합니다.

```python
import serial
import time

# 아두이노와 연결된 시리얼 포트를 여기에 입력하세요. 예: '/dev/ttyACM0' 또는 'COM3'
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

def led_on():
    ser.write(b'1') # 아두이노에 '1'을 보내 LED를 켭니다.
    print("LED ON")

def led_off():
    ser.write(b'0') # 아두이노에 '0'을 보내 LED를 끕니다.
    print("LED OFF")

try:
    while True:
        command = input("Enter command (on/off): ").lower()
        if command == "on":
            led_on()
        elif command == "off":
            led_off()
        else:
            print("Invalid command")
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated")
```

이 코드와 아두이노 코드를 사용하여 라즈베리파이에서 아두이노의 LED를 제어할 수 있습니다. 시리얼 포트 이름(`/dev/ttyACM0`, `COM3` 등)은 라즈베리파이 또는 컴퓨터에 따라 다를 수 있으니, 자신의 환경에 맞게 수정해야 합니다.