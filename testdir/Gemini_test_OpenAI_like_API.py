from openai import OpenAI 
import os
from dotenv import load_dotenv
load_dotenv()



client = OpenAI(
api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    # model="gemini-2.0-flash",
    model="gemini-2.5-pro-preview-06-05",
    messages=[
        {"role": "system", "content": " spiegare in inglese, scrivi per un testo che verra visualizzato in formato ASCII con la print di python , in manera che  mantenga il layout  "},
        {
            "role": "user",
            "content": "che  differenza ce tra cyber  security e threat intelligence? "
        }
    ]
)

print(response.choices[0].message)
