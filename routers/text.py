from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel
from utils.ai_client import qwen_summary, deepseek_reason

router = APIRouter()

# ------------------- 数据模型 -------------------
class TaskRequest(BaseModel):
    text: str
    task: str  # summary / reason / translate / explain

# ------------------- 统一任务接口 -------------------
@router.post("/task")
def handle_task(req: TaskRequest):
    if req.task == "summary":
        return {"result": qwen_summary(req.text)}

    elif req.task == "reason":
        return {"result": deepseek_reason(req.text)}

    elif req.task == "translate":
        return {"result": f"（占位）翻译功能稍后实现：{req.text}"}

    elif req.task == "explain":
        return {"result": f"（占位）解释功能稍后实现：{req.text}"}

    else:
        return {"error": "未知任务类型"}

# ------------------- 文件上传接口（保留） -------------------
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    cleaned = text.replace("\r\n", " ").replace("\n", " ").replace("\r", " ").strip()
    summary = qwen_summary(cleaned)

    return {
        "filename": file.filename,
        "cleaned_text": cleaned,
        "summary": summary
    }
