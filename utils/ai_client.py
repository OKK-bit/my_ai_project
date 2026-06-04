import requests
import json
import dashscope
from dashscope import Generation
import os
from dotenv import load_dotenv

# 加载.env文件里的环境变量
load_dotenv()

# 从环境变量里读取API Key
dashscope.api_key = os.getenv("QWEN_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
# ---------------- DeepSeek 推理 ----------------
def deepseek_reason(text: str) -> str:
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": text}
        ]
    }

    resp = requests.post(url, headers=headers, data=json.dumps(data))
    result = resp.json()

    # DeepSeek 的 requests 返回结构是 dict
    return result["choices"][0]["message"]["content"]

# ---------------- Qwen 摘要 ----------------
def qwen_summary(text: str, max_length: int = 30) -> str:
    prompt = f"请对下面的文本生成摘要，限制在 {max_length} 字以内：\n{text}"

    response = Generation.call(
        model="qwen-turbo",
        prompt=prompt
    )

    return response["output"]["text"]
