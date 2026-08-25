---
title: Text Summarization
emoji: 📝
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 8080
pinned: false
---

# 📝 End-to-End Text Summarization NLP Pipeline

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/shrutiii04/textsummarization)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- Project UI Demo Image -->
<p align="center">
  <a href="https://huggingface.co/spaces/shrutiii04/textsummarization">
    <img src="docs/ui-demo.png" alt="App Web Interface Demo" width="100%" />
  </a>
</p>

An end-to-end Deep Learning and MLOps pipeline built using **State-of-the-Art Transformer Models (Google Pegasus)** for automated text summarization. This project features a modular architecture covering data ingestion, data validation, model transformation, training, evaluation, and a containerized web deployment via **Docker** on **Hugging Face Spaces**.

---

## 🌟 Key Features

* **Modular MLOps Design**: Standardized enterprise codebase architecture isolating components for Data Ingestion, Data Validation, Transformation, Training, and Evaluation.
* **State-of-the-Art Model**: Utilizes fine-tuned sequence-to-sequence transformer architectures for high-accuracy abstractive summarization.
* **Containerized Deployment**: Completely containerized using **Docker** running on port `8080`.
* **Interactive Web Interface**: Sleek frontend UI allowing real-time text input and automatic summary generation.
* **Cloud Ready**: Configured for continuous integration and automated hosting on Hugging Face Spaces.

---

## ⚡ Pipeline & System Architecture

<!-- Architecture Diagram Image -->
<p align="center">
  <img src="docs/architecture.png" alt="End-to-End Pipeline Architecture" width="90%" />
</p>

1. **Data Ingestion**: Downloads raw text data and extracts artifacts.
2. **Data Validation**: Checks file presence and schema consistency against baseline requirements.
3. **Data Transformation**: Tokenizes raw text inputs into tensor representations.
4. **Model Training**: Fine-tunes the transformer model on GPU/CPU resources configured in `params.yaml`.
5. **Model Evaluation**: Generates ROUGE metric scores to benchmark prediction quality.
6. **Web Inference**: Exposes API endpoints and a web frontend for real-time text summarization.

---

## 🛠️ Tech Stack

| Category | Technologies & Tools |
| :--- | :--- |
| **Language** | Python 3.8+ |
| **Deep Learning** | PyTorch, Hugging Face Transformers, Datasets, Evaluate, ROUGE |
| **Pipeline & Web** | FastAPI / Flask, HTML5/CSS3 |
| **DevOps & MLOps** | Docker, Git, GitHub Actions |
| **Cloud Hosting** | Hugging Face Spaces (Docker SDK) |

---

## 📁 Directory Structure

```text
Text_Summarization-End-To-End-Pipeline/
├── .github/workflows/       # CI/CD deployment pipelines
├── artifacts/               # Processed data, model checkpoints & metrics
├── config/                  # Pipeline parameters and directory path configs
│   └── config.yaml
├── docs/                    # Architectural diagrams and screenshot assets
│   ├── architecture.png
│   └── ui-demo.png
├── research/                # Experimental Jupyter Notebooks (01 to 05)
├── src/textSummarizer/      # Modular Python source package
│   ├── components/          # Ingestion, validation, transformation, trainer modules
│   ├── config/              # Configuration manager setups
│   ├── constants/           # Global constant definitions
│   ├── entity/              # Dataclasses and schemas
│   ├── logging/             # Centralized custom logger
│   ├── pipeline/            # Training and prediction workflow stages
│   └── utils/               # Common helper functions
├── templates/               # UI HTML templates
│   └── index.html
├── app.py                   # Application entry point & web API endpoints
├── Dockerfile               # Container build configuration
├── main.py                  # Pipeline execution runner
├── params.yaml              # Hyperparameters & model configuration
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```
