# GemmARIA Quick Start Guide

## ✅ Setup Complete!

The project has been successfully set up with the following:

1. ✅ Repository cloned
2. ✅ Python virtual environment created
3. ✅ Python dependencies installed
4. ✅ Frontend dependencies installed
5. ✅ Cross-platform path fixes applied
6. ✅ Import structure fixed

## 🚀 Running the Application

### Option 1: Using Scripts (Recommended)

#### Windows:

**Backend:**
```cmd
cd application
run_backend.bat
```

**Frontend (in a new terminal):**
```cmd
cd application
run_frontend.bat
```

#### Linux/Mac:

**Backend:**
```bash
cd application
chmod +x run_backend.sh
./run_backend.sh
```

**Frontend (in a new terminal):**
```bash
cd application
chmod +x run_frontend.sh
./run_frontend.sh
```

### Option 2: Manual Start

#### Backend:

```bash
cd application

# Windows
.\venv\Scripts\Activate.ps1
python -m uvicorn back.back:app --host 0.0.0.0 --port 8000 --reload

# Linux/Mac
source venv/bin/activate
python -m uvicorn back.back:app --host 0.0.0.0 --port 8000 --reload
```

#### Frontend:

```bash
cd application/front
npm run dev
```

## 🔧 Configuration Required

Before running, you need to configure your Google Cloud credentials in:

`application/back/back_environment.py`

Update the following values:
- `PROJECT_ID` - Your GCP project ID
- `REGION` - Your GCP region
- `MEDGEMMA_ENDPOINT_ID` - Your MedGemma endpoint ID
- `MEDGEMMA_FT_ENDPOINT_ID` - Your fine-tuned MedGemma endpoint ID
- `NNUNET_ENDPOINT_ID` - Your nnU-Net endpoint ID
- `RAG_CORPUS` - Your RAG corpus path

### GCP Authentication:

```bash
gcloud auth application-default login
gcloud config set project your-gcp-project-id
```

## 📝 Important Notes

### WeasyPrint (PDF Generation)

On Windows, WeasyPrint requires GTK+ runtime to be installed for PDF generation. If you encounter errors when generating PDFs:

1. Download GTK+ runtime from: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer
2. Install it on your system
3. Restart your terminal/IDE

If you don't need PDF generation, you can comment out the weasyprint imports in `back_report.py`.

### MRI Data

Place your MRI files in:
- `application/front/public/mri/0/mri_file.nii` (first scan)
- `application/front/public/mri/1/mri_file.nii` (second scan)

## 🌐 Access the Application

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs (FastAPI automatic documentation)

## 🔍 Verify Installation

Test that everything is working:

1. **Backend Health Check:**
   ```bash
   curl http://localhost:8000/
   ```

2. **Frontend:**
   Open http://localhost:3000 in your browser

## 📚 More Information

See `SETUP.md` for detailed setup instructions and troubleshooting.

---

**Ready to use! 🎉**


