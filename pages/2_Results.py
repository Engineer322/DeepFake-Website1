import streamlit as st
from fpdf import FPDF
from pathlib import Path
from PIL import Image
import tempfile

st.set_page_config(page_title="Results", page_icon="📊", layout="wide")

# ======================
# LOAD CYBER CSS
# ======================
with open("assets/cyber.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📊 Results")

# ======================
# GET RESULT
# ======================
r = st.session_state.get("result")
if not r:
    st.warning("No result found. Go to Detection and run analysis.")
    st.stop()

# Extract metrics
pred = str(r.get("prediction", "UNKNOWN")).upper()
conf = float(r.get("confidence", 0.0)) * 100.0
p_real = float(r.get("prob_real", 0.0)) * 100.0
p_fake = float(r.get("prob_fake", 0.0)) * 100.0
transcript = r.get("transcript", "") or ""
media_type = r.get("media_type", "unknown")
media_path = r.get("media_path")  # We assume Detection page saves temp path

badge_class = "fake" if pred == "FAKE" else "real"

# ======================
# SHOW UPLOADED MEDIA
# ======================
st.subheader("🎞️ Uploaded Media")
if media_type == "image" and media_path and Path(media_path).exists():
    img = Image.open(media_path)
    st.image(img, use_column_width=True)
elif media_type == "video" and media_path and Path(media_path).exists():
    st.video(media_path)
elif media_type == "audio" and media_path and Path(media_path).exists():
    st.audio(media_path)
else:
    st.info("No media preview available.")

# ======================
# VERDICT & METRICS
# ======================
st.markdown(f"""
<div class="df-card">
  <div class="df-badge {badge_class}">VERDICT: {pred}</div>
  <div class="df-kpi">
    <div class="item"><div class="label">Confidence (predicted class)</div><div class="value">{conf:.2f}%</div></div>
    <div class="item"><div class="label">REAL probability</div><div class="value">{p_real:.2f}%</div></div>
    <div class="item"><div class="label">FAKE probability</div><div class="value">{p_fake:.2f}%</div></div>
  </div>
  <div class="df-hr"></div>
  <b>Explanation</b><br>
  <span style="color: rgba(230,230,230,.78);">
    Prediction is computed using your trained models.
    {"For audio/video, features include transcription + MFCC; for images, a CNN/ViT model is applied."}
  </span>
</div>
""", unsafe_allow_html=True)

# ======================
# TRANSCRIPT
# ======================
if transcript.strip():
    st.markdown("")
    st.subheader("📝 Script / Transcription")
    st.markdown(
        f"<div class='df-card-plain df-mono'>{transcript}</div>",
        unsafe_allow_html=True
    )

# ======================
# ACTION BUTTONS
# ======================
st.markdown("")
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("🔁 Analyze another file", use_container_width=True):
        st.session_state["result"] = None
        st.switch_page("pages/1_Detection.py")

with col2:
    # ======================
    # PDF REPORT GENERATION
    # ======================
    pdf_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf_path = Path(pdf_file.name)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Deepfake Detection Report", ln=True, align="C")
    pdf.ln(10)
    
    # Prediction info
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Prediction: {pred}", ln=True)
    pdf.cell(0, 10, f"Confidence (predicted class): {conf:.2f}%", ln=True)
    pdf.cell(0, 10, f"REAL probability: {p_real:.2f}%", ln=True)
    pdf.cell(0, 10, f"FAKE probability: {p_fake:.2f}%", ln=True)
    pdf.ln(5)
    
    # Explanation
    pdf.multi_cell(0, 8, "Explanation:\n" +
                   "Prediction is computed using your trained models. " +
                   "For audio/video, features include transcription + MFCC; " +
                   "for images, a CNN/ViT model is applied.")
    pdf.ln(5)
    
    # Transcript
    if transcript.strip():
        pdf.multi_cell(0, 8, "Transcription:\n" + transcript)
        pdf.ln(5)
    
    # Embed media in PDF
    if media_type == "image" and media_path and Path(media_path).exists():
        pdf.ln(5)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 8, "Uploaded Image:", ln=True)
        pdf.image(str(media_path), w=150)
    elif media_type in ["video", "audio"] and media_path and Path(media_path).exists():
        pdf.ln(5)
        pdf.set_font("Arial", 'B', 12)
        pdf.multi_cell(0, 8, f"Uploaded {media_type.capitalize()}: {Path(media_path).name}\n(Preview not embedded in PDF)")

    # Save PDF
    pdf.output(str(pdf_path))
    
    st.download_button(
        label="⬇️ Download Report (PDF)",
        data=pdf_path.read_bytes(),
        file_name="deepfake_report.pdf",
        mime="application/pdf",
        use_container_width=True
    )
