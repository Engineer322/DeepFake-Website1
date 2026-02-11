import streamlit as st

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
# INTRO & NAVIGATION
# ======================
st.subheader("📁 Get Started")

st.write(
    "Welcome to the Deepfake Detection Control Center. "
    "Use the sidebar to navigate through the system modules."
)

st.info(
    "➡️ Open the **Detection** page from the left sidebar to upload media "
    "and perform forensic analysis."
)

st.markdown("---")

st.subheader("📊 System Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎥 Video Analysis")
    st.write("Detect facial, lip-sync, and temporal manipulations.")
    st.caption("Supported: MP4, MOV, AVI, MKV")

with col2:
    st.markdown("### 🎧 Audio Analysis")
    st.write("Analyze voice cloning and audio inconsistencies.")
    st.caption("Supported: WAV, MP3")

with col3:
    st.markdown("### 🖼️ Image Analysis")
    st.write("Inspect visual artifacts and AI-generated patterns.")
    st.caption("Supported: JPG, PNG")

st.markdown("---")

st.subheader("⚡ Quick Info")

st.write(
    "- The Detection page is the main module for uploading and analyzing media.\n"
    "- After running detection, results and AI explanations are available on the Results page.\n"
    "- This system supports multi-modal forensic analysis (video, audio, image).\n"
    "- All explanations are human-readable and explain why media is likely manipulated."
)
