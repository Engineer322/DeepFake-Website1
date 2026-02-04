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

# Extra inline effects (safe)
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
# TOP CONTROL HEADER
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
    st.caption("FFmpeg • Whisper • Trained Models")

st.markdown("---")

# ======================
# MEDIA SUPPORT OVERVIEW
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
# CORE FORENSIC MODULES
# ======================
c1, c2, c3 = st.columns(3, vertical_alignment="top")

with c1:
    with st.container(border=True):
        st.subheader("🔍 Analyze")
        st.write(
            "Upload **video, audio, or images** to perform "
            "AI-based deepfake detection using forensic signals."
        )
        st.caption("Recommended input length: 5–15 seconds")

with c2:
    with st.container(border=True):
        st.subheader("🧾 Evidence")
        st.write(
            "Review extracted transcripts, detected anomalies, "
            "and probability-based authenticity scoring."
        )
        st.caption("REAL vs FAKE breakdown")

with c3:
    with st.container(border=True):
        st.subheader("📤 Export")
        st.write(
            "Generate a structured forensic report suitable "
            "for academic or official submission."
        )
        st.caption("Downloadable results")

st.markdown("---")

# ======================
# FAKE CONFIDENCE PREVIEW
# ======================
st.subheader("📊 Detection Confidence (Preview)")

p1, p2 = st.columns([3, 1])

with p1:
    st.progress(72)
    st.caption("Example confidence score (UI preview only)")

with p2:
    st.metric(label="Verdict", value="LIKELY FAKE", delta="+72%")

st.markdown("")

# ======================
# CALL TO ACTION
# ======================
st.info("➡️ Open **Detection** from the left sidebar to begin forensic analysis.")
