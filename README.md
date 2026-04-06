# HOTS Question Generator 🧠

A powerful web application that generates **Higher Order Thinking Skills (HOTS)** questions from learning materials using NLP.

## ✨ Features

- **📤 File Upload Support**: Upload PDF, TXT, or DOCX files
- **🎯 Smart Topic Extraction**: Automatically identifies key topics from your content
- **❓ Multi-Level Questions**: Generates questions at three difficulty levels:
  - **2 Marks**: Understanding & Comprehension
  - **5 Marks**: Analysis & Evaluation
  - **10 Marks**: Synthesis & Creation
- **💡 Answer Generation**: Includes detailed answers for each question
- **🎨 Beautiful UI**: Modern, responsive interface with vibrant colors
- **⚡ Fast Processing**: Quick topic extraction and question generation

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/hots-question-generator.git
   cd hots-question-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**

   **Option A: Using Streamlit (Recommended)**
   ```bash
   streamlit run streamlit_app.py
   ```
   Then open `http://localhost:8501` in your browser

   **Option B: Using Flask**
   ```bash
   python app.py
   ```
   Then open `http://localhost:5000` in your browser

## 📁 Project Structure

```
hots-question-generator/
├── app.py                      # Flask application
├── streamlit_app.py            # Streamlit application
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore file
├── README.md                   # This file
├── STREAMLIT_DEPLOYMENT.md     # Deployment guide
├── templates/
│   └── index.html             # Flask HTML template
├── utils/
│   ├── file_parser.py         # PDF/DOCX/TXT parser
│   ├── topic_extractor.py     # Topic extraction using NLTK
│   └── question_generator.py  # HOTS question generation
└── uploads/                   # Uploaded files storage
```

## 🔧 How It Works

1. **File Upload**: User uploads a document (PDF, TXT, or DOCX)
2. **Text Extraction**: The system extracts text from the file
3. **Topic Identification**: Key topics are extracted using NLP techniques
4. **Question Generation**: HOTS questions are generated for each topic
5. **Display**: Questions and answers are displayed in an organized format

## 📚 Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask, Streamlit
- **NLP**: NLTK (Natural Language Toolkit)
- **File Processing**: PyMuPDF, python-docx, python-pptx
- **Styling**: Custom CSS with Bootstrap

## 🎓 Educational Value

This tool helps teachers create HOTS-based assessments by:
- Automating question generation from textbooks and materials
- Ensuring questions align with Bloom's Taxonomy
- Saving time in question paper preparation
- Creating consistent, high-quality assessment questions

## 🌐 Deployment

### Deploy to Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**

3. **Deploy the app**
   - Select your repository
   - Choose `streamlit_app.py` as the main file
   - Click Deploy

4. **Share the URL** with your teacher!

For detailed instructions, see [STREAMLIT_DEPLOYMENT.md](STREAMLIT_DEPLOYMENT.md)

## 💻 API Endpoints (Flask)

- **GET `/`**: Display the main interface
- **POST `/`**: Process uploaded file and generate questions

## 🛠️ Customization

### Modify Question Levels
Edit `utils/question_generator.py` to customize question templates

### Change Color Scheme
Update CSS in `templates/index.html` or `streamlit_app.py`

### Add File Type Support
Modify `utils/file_parser.py` to support additional file formats

## ⚠️ Limitations

- Maximum file size depends on server (local: ~100MB, Streamlit Cloud: ~200MB)
- Text extraction quality depends on document format
- Works best with well-structured educational content
- Requires internet connection for Streamlit Cloud deployment

## 🔐 Security

- Files are temporarily stored in `uploads/` folder
- No personally identifiable information is collected
- All processing happens locally (in local deployment)

## 📝 License

This project is open source and available for educational use.

## 👨‍💼 About

Created as an educational tool to help teachers generate HOTS questions efficiently.

## 📧 Contact & Support

For issues, questions, or suggestions:
1. Check the [STREAMLIT_DEPLOYMENT.md](STREAMLIT_DEPLOYMENT.md) guide
2. Review the code comments
3. Test with different document formats

## 🙏 Acknowledgments

- NLTK for NLP capabilities
- Streamlit for the web framework
- PyMuPDF for PDF processing

---

**Made with ❤️ for educators and students**
