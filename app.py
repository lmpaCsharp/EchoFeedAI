import os
from typing import Any

from dotenv import load_dotenv
from flask import Flask, render_template, request

from demo_data import get_demo_payload
from openrouter_client import OpenRouterError, generate_echofeed

load_dotenv()

app = Flask(__name__)

DEFAULT_FORM = {
    "topic": "IA vai substituir empregos?",
    "profile_a": "Otimista tech: pessoa empreendedora, curiosa sobre tecnologia, interessada em produtividade, inovação e vantagem competitiva.",
    "profile_b": "Estudante ansioso: pessoa preocupada com carreira, insegurança financeira, futuro do trabalho e pressão para acompanhar mudanças.",
    "platform": "TikTok",
    "personalization": "Alta",
    "algorithm_goal": "Reter atenção",
}

PLATFORMS = ["TikTok", "Instagram Reels", "YouTube Shorts", "LinkedIn", "Feed misto"]
PERSONALIZATION_LEVELS = ["Baixa", "Média", "Alta"]
ALGORITHM_GOALS = ["Informar", "Reter atenção", "Engajar", "Vender", "Polarizar"]


def normalize_form(form_data: Any) -> dict[str, str]:
    normalized = DEFAULT_FORM.copy()

    for field in normalized:
        value = form_data.get(field, "")
        if isinstance(value, str) and value.strip():
            normalized[field] = value.strip()

    if normalized["platform"] not in PLATFORMS:
        normalized["platform"] = DEFAULT_FORM["platform"]

    if normalized["personalization"] not in PERSONALIZATION_LEVELS:
        normalized["personalization"] = DEFAULT_FORM["personalization"]

    if normalized["algorithm_goal"] not in ALGORITHM_GOALS:
        normalized["algorithm_goal"] = DEFAULT_FORM["algorithm_goal"]

    return normalized


@app.route("/", methods=["GET", "POST"])
def index():
    form = DEFAULT_FORM.copy()
    result = None
    error = None
    mode = None
    model_name = os.getenv("OPENROUTER_MODEL", "openrouter/free")
    prompt_preview = None

    if request.method == "POST":
        form = normalize_form(request.form)
        action = request.form.get("action", "ai")

        if action == "demo":
            result = get_demo_payload()
            mode = "demo"
        else:
            try:
                generated = generate_echofeed(form)
                result = generated["payload"]
                prompt_preview = generated["prompt"]
                model_name = generated["model"]
                mode = "ai"
            except OpenRouterError as exception:
                error = str(exception)
            except Exception as exception:
                error = f"Erro inesperado ao gerar com IA: {exception}"

    return render_template(
        "index.html",
        form=form,
        result=result,
        error=error,
        mode=mode,
        model_name=model_name,
        prompt_preview=prompt_preview,
        platforms=PLATFORMS,
        personalization_levels=PERSONALIZATION_LEVELS,
        algorithm_goals=ALGORITHM_GOALS,
        has_key=bool(os.getenv("OPENROUTER_API_KEY")),
    )


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
