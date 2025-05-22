from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import google.generativeai as genai

# Initialize FastAPI app
app = FastAPI()

# Enable CORS so frontend (on Vercel) can call this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY is not set.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-001")

# Data model for POST body
class PostRequest(BaseModel):
    user_idea: str
    domain: str

# Route: POST /generate
@app.post("/generate")
def generate_post(data: PostRequest):
    prompt = f'''
You are a LinkedIn strategist helping a tech expert write a post about: {data.domain}.
User input (if any): {data.user_idea}

Generate a post (250–350 words) with:
- Strong hook
- Problem/opportunity
- Solution or analogy
- User expertise & tools
- CTA & relevant hashtags

Make it readable, professional, and engaging.
'''
    response = model.generate_content(prompt)
    return {"post": response.text.strip()}
