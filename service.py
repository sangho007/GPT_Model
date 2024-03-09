from gpt_model import GPT_Model
import argparse

parser = argparse.ArgumentParser(description='m')
parser.add_argument('message', type=str, help='option')
parser.add_argument('openai_key', type=str, help='option')
args = parser.parse_args()

param = args.message  # 명령줄에서 받은 메시지
key: str = args.openai_key  # 명령줄에서 받은 키

model = GPT_Model(OPENAI_API_KEY=key)

if param == '0':
    model.clear()
else:
    pass

model.input_read()

model.request_gpt()
