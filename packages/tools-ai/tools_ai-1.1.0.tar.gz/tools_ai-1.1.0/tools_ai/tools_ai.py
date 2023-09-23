import urllib
import requests
from bs4 import BeautifulSoup
import time
import json
import websocket
import base64


class AI:

  def __init__(self):
    self.chat_id = None
    self.token = None

  def decodeString(self, encodedString, salt):
    encodedString = urllib.parse.unquote(encodedString)
    decodedString = ''

    for i in range(len(encodedString)):
      charCode = ord(encodedString[i]) - salt
      decodedString += chr(charCode)

    return decodedString

  def get_data(self):
    res = requests.get('https://chat.chatgptdemo.net/')
    soup = BeautifulSoup(res.text, 'html.parser')
    element = soup.find(id="TTT").text
    token = self.decodeString(element, 5)
    element2 = soup.find(id="USERID")
    userid = element2.get_text().strip()
    new_chat = requests.post('https://chat.chatgptdemo.net/new_chat',
                             json={
                                 "user_id": userid
                             }).json()['id_']
    return {'token': token, 'chat_id': new_chat}

  def send_message(self, content):
  
    """
        Send a message and get a response from GPT
        **Parameters**
            - **content** : Message content
    """
    
    if not self.token or self.chat_id:
      tokens = self.get_data()
      self.chat_id = tokens['chat_id']
      self.token = tokens['token']

    payload = {
        "question": f"{content}",
        "chat_id": self.chat_id,
        "timestamp": time.time(),
        "token": self.token
    }
    response = requests.post('https://chat.chatgptdemo.net/chat_api_stream',
                             json=payload)
    response_parts = json.loads(
        f"[{response.text.replace('data: ', ',')[1:]}]")
    res = "".join([
        data['choices'][0]['delta']['content'] for data in response_parts[1:-1]
    ])

    return res

  def generate_art(self,prompt,steps: int = 30,scale: int = 9,type: str = "Realistic",negative_prompt: str = "",disable_auto_prompt: bool = True):
    """
        Generate art from Picasso Diffusion
        **Parameters**
            - **promt** : Art details
            - **steps** : Steps amount for art creation
            - **scale** : Scale amount for art creation
            - **type** : Art Type (Realistic, Animelic)
            - **negative_prompt** : Negative prompt for art creatin, example: Color blue
            - **disable_auto_prompt** : Disable auto prompt correction
    """
    print("Generating Art")
    uri = "wss://aipicasso-picasso-diffusion-latest-demo.hf.space/queue/join"
    session_hash = "vvx2rpdvals"
    ws = websocket.WebSocket()
    ws.connect(uri)

    ws.send(json.dumps({"session_hash": session_hash, "fn_index": 1}))
    ws.recv()

    ws.send(
        json.dumps({
            "fn_index":
            1,
            "data": [
                prompt, scale, steps, "Square", 0, None, 0.5, negative_prompt,
                disable_auto_prompt, type
            ],
            "session_hash":
            session_hash
        }))

    while True:
      rs = ws.recv()
      if "process_completed" in str(rs):
        output = json.loads(rs)['output']['data'][0]
        return base64.b64decode(output.replace('data:image/png;base64,', ''))
