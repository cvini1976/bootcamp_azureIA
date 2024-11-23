import requests
from bs4 import BeautifulSoup

# Criando uma função para pegar uma URL.
def extract_text_from_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()
        
        texto = soup.get_text(separator= ' ')
        #Limpar texto
        linhas = (line.strip() for line in texto.splitlines())
        parts = (phrase.strip() for line in linhas for phrase in line.split(" "))
        texto_limpo = '\n'.join(part for part in parts)
        return texto_limpo
    else:
        print("Falha ao acessar a URL...CODE:", {response.status_code})
        return None
    text = soup.get_text()
    return text
# Testando a função
print(extract_text_from_url('https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo'))

from langchain_openai.chat_models.azure import AzureChatOpenAI

client = AzureChatOpenAI(
    azure_endpoint="https://oia-bootcapdio-uksouth01.openai.azure.com/",
    api_key="4huwefhwbfhwbfhrfbrhfherghergve",
    api_version="2024-02-15-preview",
    model_name="gpt-4o-mini",
    max_retries=0
)
def translate_article(text, lang):
    messages = [
        ("system", "Você deve atuar como tradutor de textos"),
        ("user", f"Traduza o {text} para o idioma {lang} e responda em markdown")
    ]

    response = client.invoke(messages)
    print(response.content)
    return response.content

print(translate_article("Let's see if the deployment was succeeded.", "pt-br"))

url = 'https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo'
text = extract_text_from_url(url)
translated_text = translate_article(text, "pt-br")
print(translated_text)
