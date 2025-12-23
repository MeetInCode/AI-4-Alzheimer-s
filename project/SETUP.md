# GemmARIA Project Setup Guide

This guide will help you set up the entire GemmARIA project on your local machine.

## Prerequisites

- **Python 3.12+** (Python 3.13 is recommended)
- **Node.js 18+** and npm
- **Google Cloud Platform** account with Vertex AI enabled (for production use)
- **Git** for version control

## 🚀 Quick Setup

### 1. Clone the Repository

The repository has already been cloned to your workspace.

### 2. Backend Setup (Python/FastAPI)

#### 2.1 Navigate to Application Directory

```bash
cd application
```

#### 2.2 Create Virtual Environment

```bash
# Windows (PowerShell)
python -m venv venv

# Linux/Mac
python3 -m venv venv
```

#### 2.3 Activate Virtual Environment

```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (Command Prompt)
venv\Scripts\activate.bat

# Linux/Mac
source venv/bin/activate
```

#### 2.4 Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 2.5 Configure Environment Variables

Edit `back/back_environment.py` with your GCP settings:

```python
# Google Cloud Configuration
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"
MEDGEMMA_ENDPOINT_ID = "your-medgemma-endpoint-id"
MEDGEMMA_FT_ENDPOINT_ID = "your-finetuned-endpoint-id"
# ... other configuration
```

**Note:** If you don't have GCP access, you'll need to set up your GCP credentials:

```bash
# Install gcloud CLI and authenticate
gcloud auth application-default login
gcloud config set project your-gcp-project-id
```

#### 2.6 Run the Backend Server

From the `application` directory:

```bash
# Make sure you're in the application directory
cd application

# Run the FastAPI server
python -m back.back

# Or using uvicorn directly
uvicorn back.back:app --host 0.0.0.0 --port 8000 --reload
```

The backend will be available at: `http://localhost:8000`

### 3. Frontend Setup (Next.js)

#### 3.1 Navigate to Frontend Directory

```bash
cd application/front
```

#### 3.2 Install Node.js Dependencies

```bash
npm install
```

#### 3.3 Run the Development Server

```bash
npm run dev
```

The frontend will be available at: `http://localhost:3000`

## 📁 Project Structure

```
├── application/
│   ├── back/                    # Backend (FastAPI)
│   │   ├── back.py             # Main FastAPI application
│   │   ├── back_segmentation.py
│   │   ├── back_report.py
│   │   ├── back_chat.py
│   │   ├── back_irm_analysis.py
│   │   └── back_environment.py # GCP configuration
│   ├── front/                   # Frontend (Next.js)
│   │   ├── app/                # Next.js app directory
│   │   ├── public/             # Static assets and MRI data
│   │   └── package.json
│   ├── requirements.txt        # Python dependencies
│   └── venv/                   # Python virtual environment
├── nnunet-inference/           # nnU-Net inference module
├── finetuning/                 # MedGemma fine-tuning module
├── medgemma/                   # RAG system module
├── nnunet-train/               # nnU-Net training module
└── rapport/                    # Report generation module
```

## 🔧 Configuration Notes

### MRI Data Structure

The application expects MRI data in the following structure:

```
application/front/public/mri/
├── 0/                     # Patient scan 1
│   └── mri_file.nii      # Original MRI file
├── 1/                     # Patient scan 2
│   └── mri_file.nii      # Original MRI file
├── 0.seg/                # Segmentation results for scan 1
│   └── mri_file.nii      # Segmented MRI file
└── 1.seg/                # Segmentation results for scan 2
    └── mri_file.nii      # Segmented MRI file
```

### Path Fixes

The following files have been updated to use cross-platform paths:

- `application/front/public/mri/slice.py` - Fixed hardcoded Linux paths to use relative paths
- `application/back/back_segmentation.py` - Updated to use Path objects for cross-platform compatibility

## 🏃 Running the Application

### Start Backend

1. Navigate to `application`
2. Activate virtual environment: `.\venv\Scripts\Activate.ps1` (Windows) or `source venv/bin/activate` (Linux/Mac)
3. Run: `python -m back.back` or `uvicorn back.back:app --reload`

### Start Frontend

1. Navigate to `application/front`
2. Run: `npm run dev`

## 📡 API Endpoints

The backend API provides the following endpoints:

- `GET /` - API information and health check
- `POST /seg` - Run MRI segmentation pipeline
- `POST /report` - Generate medical reports (HTML/JSON/PDF)
- `POST /chat/start` - Initialize chat session with patient data
- `POST /chat/send` - Send message to AI assistant

## 🔍 Troubleshooting

### Backend Issues

1. **Import errors**: Make sure you're running from the `application` directory and the virtual environment is activated
2. **GCP authentication errors**: Run `gcloud auth application-default login`
3. **Port 8000 already in use**: Change the port in `uvicorn` command or stop the process using port 8000

### Frontend Issues

1. **Connection to backend fails**: Verify backend is running on `http://localhost:8000`
2. **CORS errors**: Check CORS configuration in `back/back.py`
3. **Port 3000 already in use**: Change the port in `package.json` or stop the process using port 3000

### Dependencies Issues

1. **weasyprint installation fails**: On Windows, you may need to install GTK+ runtime. On Linux, install system dependencies: `sudo apt-get install python3-dev python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0`
2. **opencv-python issues**: Usually resolves with a fresh virtual environment

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai/docs)
- [nnU-Net Documentation](https://github.com/MIC-DKFZ/nnUNet)

## 📄 License

MedGemma is governed by the Health AI Developer Foundations terms of use.

This integration is licensed under the Apache 2.0 License.

---

**🧠 Empowering neurologists with AI-driven insights for safer Alzheimer's treatment! ✨**


