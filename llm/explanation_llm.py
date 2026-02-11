from utils.prompt_builder import build_prompt

def generate_explanation(result):
    """
    Generates a human-readable explanation based on
    predict_media() output.
    """

    # Build prompt (optional, for future LLM)
    _ = build_prompt(result)

    # Create human-friendly explanation
    explanation = f"This media is likely {'FAKE' if result['is_fake'] else 'REAL'} " \
                  f"with a confidence of {result['confidence']*100:.1f}%. "

    if result.get("artifacts"):
        explanation += "The system detected: " + ", ".join(result["artifacts"]) + ". "

    if result.get("frame_anomalies"):
        anomalies_text = ", ".join(f"{k} ({v} frames)" for k, v in result["frame_anomalies"].items())
        explanation += f"Several frames showed anomalies in: {anomalies_text}."

    return explanation
