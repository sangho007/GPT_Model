import openai
import json


class GPT_Model:
    input_msg = ''
    response_content = ''
    history = []
    gpt_messages = []

    def __init__(self, OPENAI_API_KEY):
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)

    def input_read(self):
        with open("./input.txt", "r", encoding="utf-8") as file:
            self.input_msg = file.read()

    def make_markdown(self, txt):
        with open("./output.md", "w", encoding="utf-8") as file:
            file.write(txt)

    def add_to_history(self, role, txt):
        # 딕셔너리를 생성하여 role과 txt 값을 저장
        history_item = {
            "role": role,
            "content": txt
        }

        # 파일을 추가 모드로 열기
        with open("./history.txt", "a", encoding="utf-8") as file:
            # 딕셔너리를 JSON 문자열로 변환하여 파일에 쓰기
            file.write(json.dumps(history_item, ensure_ascii=False) + '\n')

    def request_gpt(self):

        if self.input_msg:
            try:
                with open("./history.txt", "r", encoding="utf-8") as file:
                    for line in file:
                        history_item = json.loads(line.strip())
                        self.history.append(history_item)
            except FileNotFoundError:
                pass

            self.add_to_history('user', self.input_msg)

            self.gpt_messages = self.history.copy()
            self.gpt_messages += [
                {"role": "system", "content": "You are a professional professor"},
                {"role": "user", "content": [
                    {
                        "type": "text",
                        "text": f'{self.input_msg}.  Please answer in as much detail as possible in Korean. Use English only when necessary. Since you have to do your homework, please answer as accurately as possible. However, there should not be a lot of unnecessary and non-technical information.',
                    },
                ]
                 }
            ]

            response = self.client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=self.gpt_messages,
                max_tokens=4096,
                temperature=0.5,
                top_p=1,
                presence_penalty=0,
                frequency_penalty=0,
                n=1,
                stream=True,
            )
            self.response_content += '\n\n'

            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content, end="")
                    self.response_content += chunk.choices[0].delta.content
                    self.make_markdown(str(self.response_content))

            self.add_to_history('assistant', self.response_content)

    def clear(self):
        self.input_msg = ''
        self.response_content = ''
        self.history = []
        self.gpt_messages = []
        with open("./history.txt", "w", encoding="utf-8") as file:
            file.write('')


if __name__ == "__main__":
    pass
