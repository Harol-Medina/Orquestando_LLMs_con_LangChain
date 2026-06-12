from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from pathlib import Path
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY
from my_helper import encode_image

PROJECT_ROOT = Path(__file__).resolve().parent

llm = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model=GEMINI_FLASH
)

imagen = encode_image(PROJECT_ROOT / 'datos' / 'ejemplo_grafico.jpg')

pregunta = "Describa la imagen: "

mensaje = HumanMessage(
    content=[
        {
            "type": "text",
            "text": pregunta
        },
        {
            "type": "image_url",
            "image_url": f"data:image/jpeg;base64,{imagen}"
        }
    ]
)

respuesta = llm.invoke([mensaje])

print("\n" + "=" * 60)
print("RESPUESTA DE GEMINI")
print("=" * 60 + "\n")
print(respuesta.content)
