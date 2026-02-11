import streamlit as st
import os

from src.app_predict import predict_media
from llm.explanation_llm import generate_explanation

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Deepfake Detector",
    page_icon="🛡️",
    layout="wide"
)

# ======================
# LOAD CYBER CSS
# ======================
with open("assets/cyber.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Extra inline effects
st.markdown("""
<style>
.pulse {
    display: inline-block;
    width: 10px;
    height: 10px;
    background: #2ecc71;
    border-radius: 50%;
    animation: pulse 1.5s infinite;
    margin-right: 8px;
}
@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(46, 204, 113, 0.7); }
    70% { box-shadow: 0 0 0 12px rgba(46, 204, 113, 0); }
    100% { box-shadow: 0 0 0 0 rgba(46, 204, 113, 0); }
}
.scanline {
    height: 2px;
    background: linear-gradient(90deg, transparent, #00ffcc, transparent);
    animation: scan 3s linear infinite;
}
@keyframes scan {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}
</style>
""", unsafe_allow_html=True)

# ======================
# TOP HEADER
# ======================
top_l, top_r = st.columns([3, 1], vertical_alignment="top")

with top_l:
    st.markdown("###### CYBERSECURITY • MEDIA FORENSICS • AI VERIFICATION")
    st.title("🛡️ Deepfake Detection Control Center")
    st.caption(
        "Advanced AI system for detecting manipulated "
        "video, audio, and image content using multimodal forensics."
    )
    st.markdown('<div class="scanline"></div>', unsafe_allow_html=True)

with top_r:
    st.markdown("")
    st.markdown(
        "<span class='pulse'></span><strong>SYSTEM ONLINE</strong>",
        unsafe_allow_html=True
    )
    st.caption("CNN Models • LLM Explainability")

st.markdown("---")

# ======================
# SUPPORTED MEDIA
# ======================
st.subheader("📁 Supported Media Types")

m1, m2, m3 = st.columns(3)

with m1:
    with st.container(border=True):
        st.markdown("### 🎥 Video")
        st.write("Detect facial, lip-sync, and temporal manipulation.")
        st.caption("MP4 • MOV")

with m2:
    with st.container(border=True):
        st.markdown("### 🎧 Audio")
        st.write("Analyze voice cloning and audio inconsistencies.")
        st.caption("WAV • MP3")

with m3:
    with st.container(border=True):
        st.markdown("### 🖼️ Image")
        st.write("Inspect visual artifacts and AI-generated patterns.")
        st.caption("JPG • PNG")

st.markdown("---")

# ======================
# FORENSIC MODULES
# ======================
c1, c2, c3 = st.columns(3, vertical_alignment="top")

with c1:
    with st.container(border=True):
        st.subheader("🔍 Analyze")
        st.write(
            "Upload media to perform AI-based deepfake detection "
            "using forensic signals."
        )

with c2:
    with st.container(border=True):
        st.subheader("🧾 Evidence")
        st.write(
            "Review detected anomalies, confidence scores, "
            "and AI-generated explanations."
        )

with c3:
    with st.container(border=True):
        st.subheader("📤 Export")
        st.write(
            "Generate structured forensic results suitable "
            "for academic reporting."
        )

st.markdown("---")

# ======================
# FILE UPLOAD & ANALYSIS
# ======================
st.subheader("📤 Upload Media for Analysis")

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["mp4", "mov", "wav", "mp3", "jpg", "png"]
)

if uploaded_file:
    os.makedirs("temp", exist_ok=True)
    file_path = os.path.join("temp", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Running deepfake forensic analysis..."):
        # CNN / Vision Detection
       detection_result = predict_media(file_path)

        # LLM Explanation
        explanation = generate_explanation(detection_result)

    st.success("✅ Analysis Complete")

    st.markdown("---")
    st.subheader("📊 Detection Results")

    col_a, col_b = st.columns([2, 1])

    with col_a:
        st.metric(
            label="Verdict",
            value="FAKE" if detection_result["is_fake"] else "REAL"
        )
        st.progress(int(detection_result["confidence"] * 100))
        st.caption(
            f"Confidence Score: {detection_result['confidence']*100:.1f}%"
        )

    with col_b:
        st.markdown("### 🔎 Detected Artifacts")
        for a in detection_result["artifacts"]:
            st.write(f"• {a}")

    st.markdown("---")
    st.subheader("🧠 AI Explanation (Explainable AI)")
    st.write(explanation)

else:
    st.info("⬆️ Upload a media file to begin forensic analysis.")
