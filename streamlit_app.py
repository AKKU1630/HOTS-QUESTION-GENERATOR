import streamlit as st
import os
from utils.file_parser import extract_text
from utils.topic_extractor import extract_topics
from utils.question_generator import generate_hots_questions

# Page configuration
st.set_page_config(
    page_title="HOTS Question Generator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to match Flask UI exactly
st.markdown("""
    <style>
    /* Root and body styling */
    :root {
        --primary: #00ffff;
        --secondary: #b537f2;
        --accent: #00ff41;
    }
    
    * {
        margin: 0;
        padding: 0;
    }
    
    /* Main app background - Vibrant gradient */
    .stApp {
        background: linear-gradient(135deg, #1dd1a1 0%, #a29bfe 40%, #fd79a8 100%) !important;
        background-attachment: fixed !important;
    }
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1dd1a1 0%, #a29bfe 40%, #fd79a8 100%) !important;
        background-attachment: fixed !important;
    }
    
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.95) !important;
    }
    
    .main {
        background: transparent !important;
    }
    
    /* Header styling - WHITE TEXT WITH SHADOW */
    .header-container {
        text-align: center;
        padding: 40px 20px 30px;
        background: transparent !important;
    }
    
    .header-title {
        color: #ffffff !important;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .header-subtitle {
        color: #ffffff !important;
        font-size: 1.2rem !important;
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
        margin-top: 10px !important;
        opacity: 0.98;
    }
    
    /* Upload box styling */
    .upload-section {
        background: white !important;
        border-radius: 15px !important;
        padding: 40px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2) !important;
        margin: 40px auto !important;
        max-width: 600px !important;
    }
    
    .upload-section h2 {
        color: #0066ff !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        margin-bottom: 30px !important;
    }
    
    /* Button styling - CYAN TO PURPLE GRADIENT */
    .stButton > button {
        background: linear-gradient(135deg, #00ffff 0%, #b537f2 100%) !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 15px 20px !important;
        box-shadow: 0 4px 15px rgba(0, 255, 255, 0.4) !important;
        text-transform: none !important;
        font-size: 1rem !important;
    }
    
    .stButton > button:hover {
        box-shadow: 0 6px 20px rgba(181, 55, 242, 0.5) !important;
        transform: translateY(-2px);
    }
    
    /* Results container */
    .results-container {
        max-width: 1000px !important;
        margin: 0 auto !important;
        padding: 0 20px !important;
    }
    
    /* Topic section - WHITE CARDS */
    .topic-section {
        background: white !important;
        border-radius: 15px !important;
        padding: 35px !important;
        margin-bottom: 30px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15) !important;
        border-top: 5px solid #0066ff !important;
    }
    
    .topic-title {
        color: #0066ff !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
        margin-bottom: 30px !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        display: flex !important;
        align-items: center !important;
    }
    
    .topic-title i {
        margin-right: 15px !important;
        font-size: 2.5rem !important;
    }
    
    /* Marker section background */
    .marker-section {
        margin-bottom: 35px !important;
        padding: 20px !important;
        background: linear-gradient(135deg, #f0ffff 0%, #f5f0ff 100%) !important;
        border-radius: 12px !important;
        border-left: 4px solid #00ff41 !important;
    }
    
    .marker-title {
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        color: #0066ff !important;
        margin-bottom: 20px !important;
        display: flex !important;
        align-items: center !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    .marker-badge {
        background: linear-gradient(135deg, #00ffff 0%, #b537f2 100%) !important;
        color: #000000 !important;
        padding: 5px 12px !important;
        border-radius: 20px !important;
        font-size: 0.9rem !important;
        margin-right: 12px !important;
        font-weight: 600 !important;
        display: inline-block !important;
    }
    
    /* Question item styling */
    .question-item {
        background: white !important;
        border-radius: 10px !important;
        margin-bottom: 15px !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08) !important;
        transition: all 0.3s ease;
    }
    
    .question-item:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12) !important;
        transform: translateY(-2px);
    }
    
    /* Expander header */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(0, 255, 255, 0.12) 0%, rgba(181, 55, 242, 0.12) 100%) !important;
        border-radius: 10px !important;
        color: #0a0e27 !important;
    }
    
    /* Question text */
    .question-text {
        color: #0a0e27 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    
    /* Answer styling */
    .answer-label {
        background: linear-gradient(135deg, #00ffff 0%, #b537f2 100%) !important;
        color: #000000 !important;
        padding: 8px 15px !important;
        border-radius: 20px !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        display: inline-block !important;
        margin-bottom: 15px !important;
    }
    
    .answer-text {
        color: #0a0e27 !important;
        line-height: 1.8 !important;
        font-size: 0.95rem !important;
    }
    
    /* Message boxes */
    .stInfo {
        background-color: rgba(0, 255, 255, 0.1) !important;
        color: #0a0e27 !important;
    }
    
    .stSuccess {
        background-color: rgba(0, 255, 65, 0.1) !important;
        color: #0a0e27 !important;
    }
    
    .stWarning {
        background-color: rgba(255, 193, 7, 0.1) !important;
        color: #0a0e27 !important;
    }
    
    .stError {
        background-color: rgba(255, 0, 0, 0.1) !important;
        color: #0a0e27 !important;
    }
    
    /* Text colors */
    p, span, div {
        color: #0a0e27 !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #0066ff !important;
    }
    
    /* Divider */
    .stDivider {
        border-top: 2px solid #00ffff !important;
    }
    
    /* File uploader */
    .stFileUploader {
        background-color: white !important;
        border-radius: 15px !important;
    }
    
    /* Spinner */
    .stSpinner {
        color: #00ffff !important;
    }
    
    /* Reset button custom style */
    .reset-btn {
        background: linear-gradient(135deg, #00ffff 0%, #b537f2 100%) !important;
        color: #000000 !important;
        border: none !important;
        padding: 10px 18px !important;
        border-radius: 25px !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        box-shadow: 0 4px 15px rgba(0, 255, 255, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Header
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="header-title">🧠 HOTS Question Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="header-subtitle">Generate Higher Order Thinking Skills Questions from Your Learning Materials</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Create upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Upload section
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
st.markdown('<h2>📤 Upload Your Document</h2>', unsafe_allow_html=True)

col_upload, col_reset = st.columns([3, 1])

with col_upload:
    uploaded_file = st.file_uploader(
        "Upload Your Document",
        type=["pdf", "txt", "docx"],
        label_visibility="collapsed"
    )

with col_reset:
    if st.button("🔄 Reset", use_container_width=True, key="reset_btn"):
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Process uploaded file
if uploaded_file is not None:
    # Save file
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Process
    with st.spinner("🔍 Analyzing your document..."):
        try:
            text = extract_text(file_path)
            topics = extract_topics(text)
            
            if topics:
                st.success(f"✅ Found {len(topics)} topic(s)!")
                
                # Results container
                st.markdown('<div class="results-container">', unsafe_allow_html=True)
                
                for topic in topics:
                    # Topic section
                    st.markdown('<div class="topic-section">', unsafe_allow_html=True)
                    st.markdown(f'<h2 class="topic-title">💡 {topic.upper()}</h2>', unsafe_allow_html=True)
                    
                    questions_data = generate_hots_questions(topic)
                    
                    # 2 Markers
                    if questions_data.get('2_markers'):
                        st.markdown(f'''
                        <div class="marker-section">
                            <div class="marker-title">
                                <span class="marker-badge">📍 2 MARKS</span>
                                Understanding & Comprehension
                            </div>
                        </div>
                        ''', unsafe_allow_html=True)
                        
                        for idx, item in enumerate(questions_data['2_markers'], 1):
                            with st.expander(f"Q{idx}: {item['question'][:70]}...", expanded=False):
                                st.markdown(f'<div class="question-text"><b>Question:</b> {item["question"]}</div>', unsafe_allow_html=True)
                                st.markdown('<br>', unsafe_allow_html=True)
                                st.markdown(f'<span class="answer-label">💡 Answer</span>', unsafe_allow_html=True)
                                st.markdown(f'<div class="answer-text">{item["answer"]}</div>', unsafe_allow_html=True)
                    
                    # 5 Markers
                    if questions_data.get('5_markers'):
                        st.markdown(f'''
                        <div class="marker-section">
                            <div class="marker-title">
                                <span class="marker-badge">📍 5 MARKS</span>
                                Analysis & Evaluation
                            </div>
                        </div>
                        ''', unsafe_allow_html=True)
                        
                        for idx, item in enumerate(questions_data['5_markers'], 1):
                            with st.expander(f"Q{idx}: {item['question'][:70]}...", expanded=False):
                                st.markdown(f'<div class="question-text"><b>Question:</b> {item["question"]}</div>', unsafe_allow_html=True)
                                st.markdown('<br>', unsafe_allow_html=True)
                                st.markdown(f'<span class="answer-label">💡 Answer</span>', unsafe_allow_html=True)
                                st.markdown(f'<div class="answer-text">{item["answer"]}</div>', unsafe_allow_html=True)
                    
                    # 10 Markers
                    if questions_data.get('10_markers'):
                        st.markdown(f'''
                        <div class="marker-section">
                            <div class="marker-title">
                                <span class="marker-badge">📍 10 MARKS</span>
                                Synthesis & Creation
                            </div>
                        </div>
                        ''', unsafe_allow_html=True)
                        
                        for idx, item in enumerate(questions_data['10_markers'], 1):
                            with st.expander(f"Q{idx}: {item['question'][:70]}...", expanded=False):
                                st.markdown(f'<div class="question-text"><b>Question:</b> {item["question"]}</div>', unsafe_allow_html=True)
                                st.markdown('<br>', unsafe_allow_html=True)
                                st.markdown(f'<span class="answer-label">💡 Answer</span>', unsafe_allow_html=True)
                                st.markdown(f'<div class="answer-text">{item["answer"]}</div>', unsafe_allow_html=True)
                    
                    st.divider()
                    st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("⚠️ No topics found. Try another file.")
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

else:
    st.info("👆 Upload a document to generate HOTS questions!")

