#!/usr/bin/python3

#
# -*- coding: utf-8 -*-
# @File  : unionchat.py
# @Date  : 2023/9/14
#
#

import http
import json
from enum import Enum
import requests

class HostAgents(Enum):
    API_REQUEST_CODE_SUCCESS = 200
    API_REQUEST_CODE_FAIL = 201
    API_REQUEST_CODE_TIMEOUT = 408

class OpenChatRequest():
    @staticmethod
    def chatHTTPSRequest(content, apiHost, apiKey):
        payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            { "role" : "user", "content": content }
        ]
        })
        headers = {
        'Authorization': "Bearer {}".format(apiKey),
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json'
        }
        try:
            conn = http.client.HTTPSConnection(apiHost)
            conn.request("POST", "/v1/chat/completions", payload, headers)
            res = conn.getresponse()
            data = res.read()
            return data.decode("utf-8")
        except http.client.HTTPException as e:
            return HostAgents.API_REQUEST_CODE_FAIL.value
    
class UnionChat(object):
    
    def __init__(self):
        self.ak = ''
        self.sk = ''
        self.rhost = ''
        self.type = ''
        self.content = ''
        self.replyLength = 300
        self.prompt = {

        }
        
    def writingHelper(self):
        if self.replyLength < 300:
            self.replyLength = 300
        content = f"你是一名文案创作者，请按照以下要求帮我写一篇文案！{self.content}。要求字数不少于{self.replyLength}字。"
        if self.type == "baiduBce":
            return self.baiduBceChat(content)
        elif self.type == "360ai":
            return self.ai360Chat(content)
        else:
            return self.chatAnyWhere(content)
        

    def chat(self):
        if self.type == "baiduBce":
            return self.baiduBceChat(self.content)
        elif self.type == "360ai":
            return self.ai360Chat(self.content)
        else:
            return self.chatAnyWhere(self.content)

    
    def getAccessToken(self):
        """
        使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
        """
        url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={self.ak}&client_secret={self.sk}"
        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json().get("access_token")
    
    def chatAnyWhere(self, content):
        if not self.rhost:
            self.rhost = "api.chatanywhere.com.cn"
        chatRes = OpenChatRequest.chatHTTPSRequest(content, self.rhost, self.sk)
        contentDict = json.loads(chatRes)
        return contentDict['choices'][0]['message']['content']
    
    def chatOpenAiProxy(self, content):
        return OpenChatRequest.chatHTTPSRequest(content, self.rhost, self.sk)
    
    def baiduBceChat(self, content):
        if self.ak == "" or self.sk == "":
            return 'error, please set ak and sk'
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + self.getAccessToken()
        payload = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": content
                }
            ]
        })
        headers = {
            'Content-Type': 'application/json'
        }
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            response = json.loads(response.text)
            response = response['result']
        except Exception as e:
            response = HostAgents.API_REQUEST_CODE_FAIL.value
        return response
    
    def ai360Chat(self, content):
        if not self.sk:
            return 'error, please set sk'
        url = self.rhost
        if not self.rhost:
            url = "https://api.360.cn/v1/chat/completions"
        payload = json.dumps({
            "model": "360GPT_S2_V9",
            "messages": [
                {
                "role": "user",
                "content": content
                }
            ],
            "stream": False,
            "temperature": 0.9,
            "max_tokens": 2048,
            "top_p": 0.7,
            "top_k": 0,
            "repetition_penalty": 1.1,
            "num_beams": 1,
            "user": "andy"
        })
        headers = {
            'Authorization': f"Bearer {self.sk}",
            'Content-Type': 'application/json'
        }
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            contentDict = json.loads(response.text)
            return contentDict['choices'][0]['message']['content']
        except Exception as e:
            response = HostAgents.API_REQUEST_CODE_FAIL.value
        return response