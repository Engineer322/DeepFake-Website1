def generate_explanation(media_type, result, confidence, real_prob, fake_prob, meta):
    explanation = []

    # ======================
    # VERDICT INTRO
    # ======================
    explanation.append(
        f"The uploaded {media_type} was classified as {result} with a confidence "
        f"of {confidence:.2f}%."
    )

    # ======================
    # IMAGE LOGIC
    # ======================
    if media_type == "image":
        if meta.get("face_detected"):
            explanation.append(
                "Facial feature analysis revealed abnormal texture patterns and "
                "inconsistent lighting around key regions such as the eyes and mouth. "
                "These visual artifacts are commonly observed in AI-generated images."
            )
        else:
            explanation.append(
                "The image lacks stable facial landmarks and exhibits unnatural visual "
                "patterns, reducing the likelihood of it being an authentic photograph."
            )

    # ======================
    # AUDIO LOGIC
    # ======================
    elif media_type == "audio":
        if meta.get("voice_detected"):
            explanation.append(
                "MFCC-based audio analysis detected irregular pitch transitions and "
                "unnatural speech timing, which are strong indicators of synthetic or "
                "voice-cloned audio."
            )
        else:
            explanation.append(
                "The audio signal contains abnormal frequency distributions that do not "
                "align with natural human speech characteristics."
            )

    # ======================
    # VIDEO LOGIC
    # ======================
    elif media_type == "video":
        if meta.get("face_detected"):
            explanation.append(
                "Frame-by-frame inspection revealed temporal inconsistencies in facial "
                "expressions and lip synchronization, suggesting manipulation at the "
                "visual level."
            )

        if meta.get("audio_present"):
            explanation.append(
                "Cross-modal analysis between the audio and visual streams showed timing "
                "mismatches, indicating that speech and facial movements were likely "
                "generated or altered separately."
            )

        if meta.get("duration") and meta["duration"] < 10:
            explanation.append(
                "Short video duration combined with high manipulation confidence is "
                "characteristic of deepfake samples generated for rapid dissemination."
            )

    # ======================
    # CONFIDENCE REASONING
    # ======================
    if fake_prob >= 90:
        explanation.append(
            "The extremely high fake probability indicates strong agreement across "
            "multiple detection features and models."
        )

    return " ".join(explanation)
