# 🧠 ScanBuddy – Smart Medical Report & Imaging Analysis Tool

[🔗 Live Demo](https://scanbuddy-smart-medical-report-tool.onrender.com/)

---

## 📌 Overview

**ScanBuddy** is an AI-powered medical assistant designed to **analyze medical images (X-ray, CT, MRI)** and **PDF-based medical reports**, providing structured diagnostics and **easy-to-understand explanations** for patients and healthcare enthusiasts.

This tool leverages **Google's Gemini AI** and **real-time web research** to produce comprehensive, patient-friendly analysis with follow-up conversation capabilities.

---

## ✨ Features

- 🖼️ **Medical Image Analysis** (X-ray, MRI, CT, Ultrasound, etc.)
- 📄 **PDF Medical Report Summarization**
- 💬 **Follow-up Q&A chat interface** based on the uploaded report
- 🔍 Real-time medical literature research using DuckDuckGo
- 🧠 Gemini 2.0 Flash model integration for fast, intelligent answers
- 🌐 Deployed on [Render.com](https://render.com)
- 🔒 No file storage – all files are handled securely in-memory

---

## ⚙️ Technologies Used

| Tech        | Purpose                                    |
|-------------|--------------------------------------------|
| `Streamlit` | Web interface and deployment                |
| `Google Gemini 2.0` | AI model for diagnosis & explanation       |
| `Agno SDK`  | AI agent abstraction and tool integration  |
| `DuckDuckGo Tools` | Web search integration inside the agent     |
| `PyPDF2`    | PDF reading and text extraction             |
| `Pillow (PIL)` | Image resizing and processing              |
| `BytesIO`   | In-memory image handling (no disk write)   |

---

## 🔐 API Keys Used

This app uses the **Google AI Studio API key** for Gemini integration:

- 🔑 `GOOGLE_API_KEY` (required at runtime)
- 📍 Not hardcoded — must be added through sidebar or backend environment

> 🔒 Note: Uploaded files are processed temporarily and **not stored** permanently. Your data is private.




