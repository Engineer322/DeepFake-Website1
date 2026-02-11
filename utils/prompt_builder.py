def build_prompt(result):
    artifacts = ", ".join(result["artifacts"])

    anomalies = "\n".join(
        f"- {k}: {v} abnormal frames"
        for k, v in result["frame_anomalies"].items()
    )

    return f"""
You are a forensic AI assistant.

Explain the following deepfake detection result in simple,
non-technical language for general users.

Confidence Score: {result['confidence']*100:.1f}%

Detected Visual Artifacts:
{artifacts}

Frame-Level Anomalies:
{anomalies}

Explain clearly why the media is likely manipulated.
"""
