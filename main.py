import os
from groq import Groq

api_key = os.environ["MY_GROQ_API_KEY"]

client = Groq(api_key=api_key)

chats = client.chat.completions.create(
    messages=[
        {
            "role": "User",
            "content": "what jobs can a phd in geomatics engineering with focus on geospatial vision get you?"
        }
    ],
    model="llama3-70b-8192"
)

print(chats.choices[0].message.content)