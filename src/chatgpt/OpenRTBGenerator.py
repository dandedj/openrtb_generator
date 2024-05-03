import json
from openai import OpenAI
import os

class OpenRTBGenerator:
    def __init__(self):
        self.client = OpenAI()
        self.client.api_key = os.environ["OPENAI_API_KEY"]

    def call_chatgpt_api(self, user_content):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "I am building a tester for a new DSP. "
                },
                {
                    "role": "user",
                    "content": user_content
                }
            ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response

    def generate_bid_request(self):
        response = self.call_chatgpt_api("I need to generate a bid request for a publisher. Make up an example request for a random website or app of a random type of ad and publisher and device. The bid request should be generated in the OpenRTB 2.6 format. Only return the raw openrtb body.")
        print(response.choices[0].message.content)
        return json.loads(response.choices[0].message.content)

    def generate_bid_response(self):
        response = self.call_chatgpt_api("I need to generate a bid response from a DSP for a theoretical OpenRTB bid request. Make up an example response for a random website or app of a random type of ad and publisher and device. In some cases, include a theoretical adm parameter with html code that might resemble a real response. The bid response should be generated in the OpenRTB 2.6 format. Only return the raw openrtb body.")
        print(response.choices[0].message.content)
        return json.loads(response.choices[0].message.content)
