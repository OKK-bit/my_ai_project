# FastAPI：后端框架
# Uvicorn：运行 FastAPI 的服务器
import uvicorn
from fastapi import FastAPI
from routers.text import router as text_router
from fastapi.staticfiles import StaticFiles

# 创建一个 FastAPI 应用实例(创建对象)
app = FastAPI()
# 挂载静态文件目录
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


# 注册 text 子路由
app.include_router(text_router)

# 定义一个接口：Get/
@app.get('/')
def home():
    return{
        'message': 'Hello,AI!'
    }


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)  # 合起来：告诉 uvicorn 去 main.py 里找 app 这个应用来启动。

# https://github.com/OKK-bit/my_ai_project.git