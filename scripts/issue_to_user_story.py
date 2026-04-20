import os
import requests
import sys

GITHUB_API = "https://api.github.com"
OPENAI_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-4o-mini"

def get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        print(f"Falta variable de entorno: {name}")
        sys.exit(1)
    return value

def get_issue(repo: str, issue_number: str, github_token: str) -> dict:
    url = f"{GITHUB_API}/repos/{repo}/issues/{issue_number}"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json"
    }
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()

def build_prompt(title: str, body: str) -> str:
    return f"""
Convierte el siguiente issue en historia de usuario con formato estricto.

Reglas:
1) Responde SOLO con estas secciones y en este orden exacto:
Story
<texto>

Acceptance Criteria
<lista DADO/CUANDO/ENTONCES>

2) Mantén lenguaje claro, específico y verificable.
3) No inventes tecnología si el issue no la menciona.
4) Si faltan datos, agrega supuestos mínimos y explícitos.
5) Debe parecer redactado para equipo DevSecOps cuando aplique.
6) Usa ESPAÑOL. Prohibido inglés.

Formato de referencia:
Story
Como Ingeniero DevSecOps contribuidor de la SPL,
quiero que exista un script Python (...) que detecte (...) ,
para que (...) .

Acceptance Criteria
DADO que ...
CUANDO se ejecuta ...
ENTONCES el script emite ...
Y retorna ...

Issue:
Título: {title}
Descripción:
{body if body else "(sin descripción)"}
""".strip()

def call_ai(prompt: str, openai_api_key: str) -> str:
    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {{"role": "system", "content": "Eres analista senior de requerimientos DevSecOps. Responde SOLO el formato solicitado sin explicaciones adicionales."}},
            {{"role": "user", "content": prompt}}
        ],
        "temperature": 0.2
    }
    r = requests.post(OPENAI_URL, headers=headers, json=payload, timeout=60)
    r.raise_for_status()
    data = r.json()
    return data["choices"][0]["message"]["content"].strip()

def create_issue(repo: str, github_token: str, title: str, body: str, original_issue: int) -> None:
    url = f"{GITHUB_API}/repos/{repo}/issues"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json"
    }
    full_body = f"{body}\n\n---\n*Generada automáticamente desde issue #{original_issue} por GitHub Copilot*"
    payload = {
        "title": f"HU - {title}",
        "body": full_body,
        "labels": ["historia-usuario", "generada-por-ia"]
    }
    r = requests.post(url, headers=headers, json=payload, timeout=30)
    r.raise_for_status()
    new_issue = r.json()
    print(f"✓ Nueva issue creada: #{new_issue['number']}")
    return new_issue

def main():
    github_token = get_env("GITHUB_TOKEN")
    openai_api_key = get_env("OPENAI_API_KEY")
    repo = get_env("REPO")
    issue_number = get_env("ISSUE_NUMBER")

    print(f"📖 Leyendo issue #{issue_number}...")
    issue = get_issue(repo, issue_number, github_token)
    title = issue.get("title", "Sin título")
    body = issue.get("body", "")

    print(f"🧠 Procesando con IA...")
    prompt = build_prompt(title, body)
    result = call_ai(prompt, openai_api_key)

    print(f"💾 Creando nueva issue con Historia de Usuario...")
    create_issue(repo, github_token, title, result, issue_number)
    print("✅ Proceso completado exitosamente.")

if __name__ == "__main__":
    main()
