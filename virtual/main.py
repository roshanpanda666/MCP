from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from routes.route import router


app = FastAPI()

# 💡 Enable CORS  cross-origin resource sharing 

app.add_middleware(

CORSMiddleware,

allow_origins=["*"], # universal acceptance 

allow_credentials=True,

allow_methods=["*"],

allow_headers=["*"],

)

  

# 🚀 Include your routers

app.include_router(router)