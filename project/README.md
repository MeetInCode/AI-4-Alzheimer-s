# AI-4-Alzheimer-s: AI-Powered Alzheimer's Disease Analysis Platform

A comprehensive platform for Alzheimer's disease analysis using advanced AI models including fine-tuned MedGemma, nnU-Net segmentation, and RAG-powered medical knowledge systems.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Key Components](#key-components)
- [Installation](#installation)
- [Usage](#usage)
- [Model Information](#model-information)
- [License](#license)

## 🎯 Overview

This project provides a complete solution for Alzheimer's disease analysis, combining:

- **Medical Image Segmentation**: Automated brain lesion segmentation using nnU-Net
- **AI-Powered Analysis**: Fine-tuned MedGemma models for medical text understanding
- **Knowledge Retrieval**: RAG system for accessing latest medical research
- **Report Generation**: Automated medical report generation from MRI scans
- **Web Application**: User-friendly interface for clinicians and researchers

## 📁 Project Structure

```
├── application/          # Main web application (Frontend + Backend)
│   ├── back/            # FastAPI backend server
│   ├── front/           # Next.js frontend application
│   └── requirements.txt # Python dependencies
│
├── finetuning/          # MedGemma fine-tuning scripts and code
│   ├── main.py         # Main fine-tuning script
│   ├── eval.py         # Model evaluation script
│   └── dataset_functions.py  # Dataset processing utilities
│
├── medgemma/            # RAG (Retrieval-Augmented Generation) system
│   ├── main.py         # RAG main implementation
│   ├── complete_rag_db.py  # Database creation script
│   └── get_references_from_rag_db.py  # Reference retrieval
│
├── nnunet-inference/    # nnU-Net inference pipeline
│   ├── app.py          # Inference API
│   └── data/           # Sample data
│
├── nnunet-train/        # nnU-Net training scripts
│   ├── dataset_to_nnunet.py  # Dataset conversion
│   └── analyze.py      # Analysis utilities
│
├── rapport/             # Medical report generation
│   ├── main.py         # Report generation main script
│   └── generate_report.py  # Report utilities
│
├── README.md            # This file
├── SETUP.md             # Detailed setup instructions
├── QUICKSTART.md        # Quick start guide
└── PRESENTATION_GEMMARIA.pdf  # Project presentation
```

## 🔧 Key Components

### 1. Application (`application/`)

Full-stack web application for medical image analysis and report generation.

**Backend (FastAPI):**
- MRI segmentation API
- Report generation endpoints
- Chat API with RAG integration
- Medical image analysis

**Frontend (Next.js):**
- Patient data visualization
- MRI scan viewer
- Interactive chat interface
- Report display and export

**Setup:**
```bash
cd application
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Run Backend:**
```bash
cd application
python -m uvicorn back.back:app --host 0.0.0.0 --port 8000 --reload
```

**Run Frontend:**
```bash
cd application/front
npm install
npm run dev
```

### 2. Fine-tuning (`finetuning/`)

Fine-tuned MedGemma model for Alzheimer's disease analysis.

**Features:**
- LoRA-based efficient fine-tuning
- Custom dataset processing
- Model evaluation scripts
- Hugging Face integration

**Model:** Available on [Hugging Face](https://huggingface.co/meet12341234/medgemma_finetuned_for_Alzheimers)

**Usage:**
```bash
cd finetuning
pip install -r requirements.txt
python main.py  # Start fine-tuning
python eval.py  # Evaluate model
```

### 3. RAG System (`medgemma/`)

Retrieval-Augmented Generation system for medical knowledge retrieval.

**Features:**
- Vector database for medical papers
- Semantic search capabilities
- Reference extraction
- Knowledge base management

**Setup:**
```bash
cd medgemma
python complete_rag_db.py  # Build knowledge base
python main.py             # Run RAG system
```

### 4. nnU-Net Inference (`nnunet-inference/`)

Medical image segmentation using nnU-Net.

**Features:**
- Brain lesion segmentation
- Docker containerization
- API endpoints for inference
- Model deployment utilities

**Usage:**
```bash
cd nnunet-inference
python app.py  # Start inference server
```

### 5. nnU-Net Training (`nnunet-train/`)

Training scripts and utilities for nnU-Net model.

**Features:**
- Dataset preparation
- Model training pipeline
- Quantitative analysis
- Longitudinal analysis tools

### 6. Report Generation (`rapport/`)

Automated medical report generation from MRI analysis.

**Features:**
- HTML/PDF report generation
- Comparative analysis
- Clinical formatting
- Export utilities

## 🚀 Installation

### Prerequisites

- **Python 3.8+** (Python 3.12+ recommended)
- **Node.js 18+** and npm
- **Google Cloud Platform** account (for cloud deployment)
- **Git** for version control

### Quick Setup

1. **Clone the repository:**
```bash
git clone https://github.com/MeetInCode/AI-4-Alzheimer-s.git
cd AI-4-Alzheimer-s
```

2. **Set up Python environment:**
```bash
cd application
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Set up Frontend:**
```bash
cd application/front
npm install
```

4. **Configure environment:**
   - Update `application/back/back_environment.py` with your GCP credentials
   - Set up Google Cloud authentication:
   ```bash
   gcloud auth application-default login
   gcloud config set project your-gcp-project-id
   ```

For detailed setup instructions, see [SETUP.md](./SETUP.md) or [QUICKSTART.md](./QUICKSTART.md).

## 💻 Usage

### Running the Application

**Start Backend:**
```bash
cd application
python -m uvicorn back.back:app --host 0.0.0.0 --port 8000 --reload
```

**Start Frontend (in a new terminal):**
```bash
cd application/front
npm run dev
```

Access the application at:
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs

### Using the Fine-tuned Model

The fine-tuned MedGemma model is available on Hugging Face:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "meet12341234/medgemma_finetuned_for_Alzheimers"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = "Explain the early symptoms of Alzheimer's disease."
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

**Model Card:** [View on Hugging Face](https://huggingface.co/meet12341234/medgemma_finetuned_for_Alzheimers)

## 🤖 Model Information

### Fine-tuned MedGemma Model

- **Model Name:** `meet12341234/medgemma_finetuned_for_Alzheimers`
- **Base Model:** MedGemma
- **Fine-tuning Method:** LoRA (Low-Rank Adaptation)
- **Domain:** Alzheimer's Disease Analysis
- **License:** Apache 2.0

**Capabilities:**
- Understanding Alzheimer's disease concepts
- Interpreting clinical notes and medical text
- Answering Alzheimer's-focused medical questions
- Supporting research and educational use cases

**⚠️ Important:** This model is not intended for direct clinical diagnosis or medical decision-making. Always consult qualified medical professionals for clinical decisions.

## 📚 Documentation

- **[SETUP.md](./SETUP.md)** - Detailed setup and configuration guide
- **[QUICKSTART.md](./QUICKSTART.md)** - Quick start guide for running the application
- **[application/README.md](./application/README.md)** - Application-specific documentation
- **[finetuning/README.md](./finetuning/README.md)** - Fine-tuning documentation
- **[medgemma/README.md](./medgemma/README.md)** - RAG system documentation
- **[nnunet-inference/README.md](./nnunet-inference/README.md)** - Inference documentation
- **[nnunet-train/README.md](./nnunet-train/README.md)** - Training documentation

## 📄 License

This project is licensed under the Apache 2.0 License.

MedGemma is governed by the [Health AI Developer Foundations terms of use](https://developers.google.com/health-ai-developer-foundations/terms).

## 🔗 Links

- **GitHub Repository:** https://github.com/MeetInCode/AI-4-Alzheimer-s
- **Fine-tuned Model:** https://huggingface.co/meet12341234/medgemma_finetuned_for_Alzheimers
- **Project Presentation:** [PRESENTATION_GEMMARIA.pdf](./PRESENTATION_GEMMARIA.pdf)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚠️ Disclaimer

This project is for research and educational purposes only. It is not intended for clinical diagnosis or medical decision-making. Always consult qualified medical professionals for clinical decisions.

---

**🧠 Empowering Alzheimer's research with AI-driven insights! ✨**
