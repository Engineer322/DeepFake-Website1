from utils.prompt_builder import build_prompt

def generate_explanation(result):
    """
    Lightweight explanation generator (LLM-ready).
    Can be replaced with OpenAI / Ollama / LLaMA.
    """

    prompt = build_prompt(result)

    # Simple deterministic explanation (safe fallback)
    explanation = (
        f"This media was classified as {'FAKE' if result['is_fake'] else 'REAL'} "
        f"with a confidence of {result['confidence']*100:.1f}%. "
        "The system detected multiple forensic inconsistencies, including "
        + ", ".join(result.get("artifacts", []))
        + ". These patterns are commonly associated with manipulated or AI-generated media."
    )

    return explanation
