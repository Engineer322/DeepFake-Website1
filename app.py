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
    st.caption("CNN Models • Explainable AI")

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

    # Preview
    suffix = uploaded_file.name.split(".")[-1].lower()
    if suffix in ["mp4", "mov", "m4v", "avi", "mkv"]:
        st.video(file_path)
    elif suffix in ["wav", "mp3"]:
        st.audio(file_path)
    elif suffix in ["jpg", "jpeg", "png"]:
        st.image(file_path, width=700)

    # Run detection
    if st.button("🔍 Run Detection", use_container_width=True):
        with st.spinner("Processing media..."):
            detection_result = predict_media(file_path)
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
