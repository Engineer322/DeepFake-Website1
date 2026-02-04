import streamlit as st
import tempfile
from pathlib import Path
from src.app_predict import predict_media  

st.set_page_config(page_title="Detection", page_icon="🔍", layout="wide")


with open("assets/cyber.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.markdown("""
<style>
.upload-box {
    background: linear-gradient(145deg, #0b1020, #0e1530);
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 0 40px rgba(0, 255, 200, 0.08);
}
.upload-title { color: #f2f4ff; font-size: 1.25rem; font-weight: 600; }
.upload-desc { color: rgba(230,230,230,0.75); font-size: 0.9rem; margin-top: 6px; }
.upload-drop { margin-top: 18px; padding: 32px; border-radius: 16px; border: 2px dashed rgba(0, 255, 200, 0.45); text-align: center; background: rgba(0,0,0,0.35); }
.upload-hint { color: rgba(200,255,240,0.8); font-size: 0.85rem; margin-top: 8px; }
.run-btn { margin-top: 22px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="df-card-plain">
  <h2 style="margin:0;">🧪 Detection Lab</h2>
  <p style="color: rgba(230,230,230,.78); margin-top:6px;">
    Upload <b>video, audio, or image</b> evidence.  
    The system applies multimodal forensic analysis to detect manipulation.
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("")

colA, colB = st.columns([1.3, 1])

with colA:
    st.markdown("""
    <div class="upload-box">
        <div class="upload-title">Upload Media for Analysis</div>
        <div class="upload-desc">
            Select a video, audio, or image file.
        </div>
        <div class="upload-drop">
            📁 Drag & drop or choose a file
            <div class="upload-hint">
                Supported: MP4, MP3/WAV, JPG/PNG
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "",
        label_visibility="collapsed",
        type=[
            "mp4", "mov", "m4v", "avi", "mkv",
            "wav", "mp3",
            "jpg", "jpeg", "png"
        ]
    )

    file_bytes = None
    file_type = None

    if uploaded:
        file_bytes = uploaded.getvalue()
        suffix = uploaded.name.split(".")[-1].lower()

        if suffix in ["mp4", "mov", "m4v", "avi", "mkv"]:
            file_type = "video"
            st.video(file_bytes)
        elif suffix in ["wav", "mp3"]:
            file_type = "audio"
            st.audio(file_bytes)
        elif suffix in ["jpg", "jpeg", "png"]:
            file_type = "image"
            st.image(file_bytes, width=700)

with colB:
    st.markdown("""
<div class="df-card-plain">
<b>Analysis Pipeline</b>
<ul style="margin-top:8px;">
  <li>Media intake & validation</li>
  <li>Audio extraction (FFmpeg for video)</li>
  <li>Speech transcription (Whisper for audio/video)</li>
  <li>Text + MFCC forensic features</li>
  <li>AI authenticity prediction</li>
</ul>
<div class="df-hr"></div>
<b>Supported Evidence</b><br>
🎥 Video &nbsp; 🎧 Audio &nbsp; 🖼️ Image
<br><br>
<b>Tip</b><br>
Short clips/images give the fastest results.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="run-btn">', unsafe_allow_html=True)
run = st.button(
    "🔍 Run Detection",
    use_container_width=True,
    disabled=(uploaded is None)
)
st.markdown('</div>', unsafe_allow_html=True)


if run and uploaded:
    with tempfile.TemporaryDirectory() as td:
        temp_path = Path(td) / uploaded.name
        temp_path.write_bytes(file_bytes)

        with st.spinner("Processing media..."):
            result = predict_media(str(temp_path))

        # Save result to session state
        st.session_state["result"] = result


if st.session_state.get("result"):
    if st.button("➡️ Go to Results Page", use_container_width=True):
        st.switch_page("pages/2_Results.py")
