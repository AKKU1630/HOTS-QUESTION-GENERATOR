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

# Custom CSS for styling
st.markdown("""
    <style>
    :root {
        --primary: #00ffff;
        --secondary: #b537f2;
        --accent: #00ff41;
    }
    
    .stApp {
        background: linear-gradient(135deg, #1dd1a1 0%, #a29bfe 40%, #fd79a8 100%) !important;
        background-attachment: fixed;
    }
    
    div.stApp {
        background: linear-gradient(135deg, #1dd1a1 0%, #a29bfe 40%, #fd79a8 100%) !important;
    }
    
    div[data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1dd1a1 0%, #a29bfe 40%, #fd79a8 100%) !important;
        background-attachment: fixed;
    }
    
    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.95) !important;
    }
    
    /* Header styling */
    .header-title {
        color: #ffffff;
        font-size: 3rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
        text-align: center;
    }
    
    .header-subtitle {
        color: #ffffff;
        font-size: 1.1rem;
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
        text-align: center;
    }
    
    /* Topic title */
    .topic-title {
        color: #0066ff !important;
        font-size: 1.8rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-bottom: 3px solid #00ffff;
        padding-bottom: 10px;
    }
    
    /* Marker section */
    .marker-section {
        background: linear-gradient(135deg, #f0ffff 0%, #f5f0ff 100%) !important;
        border-left: 4px solid #00ff41;
        padding: 20px;
        border-radius: 12px;
        margin: 20px 0;
    }
    
    .marker-title {
        color: #0066ff !important;
        font-size: 1.3rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Question and Answer boxes */
    .question-box {
        background: linear-gradient(135deg, rgba(0, 255, 255, 0.15) 0%, rgba(181, 55, 242, 0.15) 100%) !important;
        border-left: 3px solid #00ffff;
        padding: 15px;
        margin: 10px 0;
        border-radius: 8px;
        color: #0a0e27;
    }
    
    .answer-box {
        background: linear-gradient(135deg, rgba(0, 102, 255, 0.1) 0%, rgba(181, 55, 242, 0.1) 100%) !important;
        border-left: 3px solid #b537f2;
        padding: 15px;
        margin-top: 10px;
        border-radius: 8px;
        color: #0a0e27;
        font-weight: 500;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #00ffff 0%, #b537f2 100%) !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        text-transform: none;
    }
    
    .stButton > button:hover {
        box-shadow: 0 6px 20px rgba(181, 55, 242, 0.4) !important;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background-color: linear-gradient(135deg, rgba(0, 255, 255, 0.1) 0%, rgba(181, 55, 242, 0.1) 100%) !important;
        border: 2px solid #00ffff !important;
        border-radius: 10px !important;
        color: #0a0e27 !important;
    }
    
    /* File uploader */
    .stFileUploader {
        background-color: white !important;
        border-radius: 15px !important;
    }
    
    /* Messages */
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
    
    /* Spinners and loaders */
    .stSpinner {
        color: #00ffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="header-title">🧠 HOTS Question Generator</h1>', unsafe_allow_html=True)
st.markdown('<p class="header-subtitle">Generate Higher Order Thinking Skills Questions from Your Learning Materials</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 About")
st.sidebar.info("""
This application generates HOTS (Higher Order Thinking Skills) questions from your learning materials.

**Features:**
- 2 Marks Questions (Understanding & Comprehension)
- 5 Marks Questions (Analysis & Evaluation)
- 10 Marks Questions (Synthesis & Creation)

Upload PDF, TXT, or DOCX files to get started!
""")

# Create upload folder if it doesn't exist
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Main content
col1, col2 = st.columns([3, 1])

with col1:
    uploaded_file = st.file_uploader(
        "📤 Upload Your Document",
        type=["pdf", "txt", "docx"],
        help="Supported formats: PDF, TXT, DOCX"
    )

with col2:
    if st.button("🔄 Reset", use_container_width=True, key="reset_btn"):
        st.rerun()

# Process the uploaded file
if uploaded_file is not None:
    # Save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Show processing message
    with st.spinner("🔍 Analyzing your document..."):
        try:
            # Extract text and topics
            text = extract_text(file_path)
            topics = extract_topics(text)
            
            if topics:
                st.success(f"✅ Found {len(topics)} topic(s)!")
                
                # Display questions for each topic
                for topic in topics:
                    st.markdown(f'<h2 class="topic-title">💡 {topic.upper()}</h2>', unsafe_allow_html=True)
                    
                    # Generate questions
                    questions_data = generate_hots_questions(topic)
                    
                    # 2 Markers Section
                    if questions_data.get('2_markers'):
                        st.markdown(f'<div class="marker-section"><div class="marker-title">📍 2 Marks - Understanding & Comprehension</div></div>', unsafe_allow_html=True)
                        for idx, item in enumerate(questions_data['2_markers'], 1):
                            with st.expander(f"Q{idx}: {item['question'][:80]}...", expanded=False):
                                st.markdown(f'<div class="question-box">', unsafe_allow_html=True)
                                st.write(f"**Question:** {item['question']}")
                                st.markdown(f'</div>', unsafe_allow_html=True)
                                st.markdown(f'<div class="answer-box">', unsafe_allow_html=True)
                                st.write(f"**Answer:** {item['answer']}")
                                st.markdown(f'</div>', unsafe_allow_html=True)
                    
                    # 5 Markers Section
                    if questions_data.get('5_markers'):
                        st.markdown(f'<div class="marker-section"><div class="marker-title">📍 5 Marks - Analysis & Evaluation</div></div>', unsafe_allow_html=True)
                        for idx, item in enumerate(questions_data['5_markers'], 1):
                            with st.expander(f"Q{idx}: {item['question'][:80]}...", expanded=False):
                                st.markdown(f'<div class="question-box">', unsafe_allow_html=True)
                                st.write(f"**Question:** {item['question']}")
                                st.markdown(f'</div>', unsafe_allow_html=True)
                                st.markdown(f'<div class="answer-box">', unsafe_allow_html=True)
                                st.write(f"**Answer:** {item['answer']}")
                                st.markdown(f'</div>', unsafe_allow_html=True)
                    
                    # 10 Markers Section
                    if questions_data.get('10_markers'):
                        st.markdown(f'<div class="marker-section"><div class="marker-title">📍 10 Marks - Synthesis & Creation</div></div>', unsafe_allow_html=True)
                        for idx, item in enumerate(questions_data['10_markers'], 1):
                            with st.expander(f"Q{idx}: {item['question'][:80]}...", expanded=False):
                                st.markdown(f'<div class="question-box">', unsafe_allow_html=True)
                                st.write(f"**Question:** {item['question']}")
                                st.markdown(f'</div>', unsafe_allow_html=True)
                                st.markdown(f'<div class="answer-box">', unsafe_allow_html=True)
                                st.write(f"**Answer:** {item['answer']}")
                                st.markdown(f'</div>', unsafe_allow_html=True)
                    
                    st.divider()
            else:
                st.warning("⚠️ No topics found in the document. Please try another file.")
        
        except Exception as e:
            st.error(f"❌ Error processing file: {str(e)}")

else:
    st.info("👆 Please upload a document to get started!")
