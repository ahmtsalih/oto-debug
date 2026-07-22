from google import genai
from .config import get_api_key

def analyze_error(command: str, stderr: str) -> str:
    api_key = get_api_key()
    if not api_key:
        return "API_KEY_MISSING"

    client = genai.Client(api_key=api_key)
    prompt = f"Komut:\n{command}\n\nHata Çıktısı:\n{stderr}\n\nBu hatanın nedenini ve doğrudan çözümünü Türkçe olarak kısaca açıkla."

    try:
        modeller = [m.name.replace("models/", "") for m in client.models.list() if "gemini" in m.name]
        
        for model_adi in modeller:
            try:
                response = client.models.generate_content(
                    model=model_adi,
                    contents=prompt,
                )
                return response.text
            except Exception:
                continue
                
        return "AI_ERROR: Kota veya yetki sorunu. Calisan bir model bulunamadi."
    except Exception as e:
        return f"AI_ERROR: {str(e)}"