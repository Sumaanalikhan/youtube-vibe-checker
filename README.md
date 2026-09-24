# Multilingual YouTube Vibe Checker

A containerized application that analyzes YouTube content and viewer sentiment across multiple languages. This project is fully integrated with a custom Continuous Integration and Continuous Deployment (CI/CD) pipeline built from scratch using Jenkins and Docker.

## 🚀 Tech Stack

*   **Application:** Python, Streamlit
*   **Version Control:** Git & GitHub
*   **Containerization:** Docker, Docker Hub
*   **CI/CD Automation:** Jenkins (Declarative Pipeline)
*   **Networking / Webhooks:** ngrok

## 🏗️ Architecture & CI/CD Pipeline

This repository is connected to a local Jenkins server via GitHub Webhooks and an ngrok tunneling service. The automation workflow ensures that every code push is seamlessly built and delivered:

1.  **Code Commit:** Developer pushes code changes to the `main` branch on GitHub.
2.  **Webhook Trigger:** GitHub sends a JSON payload to the Jenkins server through a secure ngrok tunnel.
3.  **Automated Checkout:** Jenkins receives the signal and automatically clones the latest repository state.
4.  **Container Build:** Jenkins executes `docker build` using the project's `Dockerfile` to create a fresh image.
5.  **Registry Push:** Jenkins securely logs into Docker Hub using encrypted credentials and pushes the newly versioned image (`sumaanalikhan/youtube-vibe-checker:v1.0.0`).

## ⚙️ Prerequisites

To run or develop this project locally, you will need:
*   Python 3.x
*   Docker Desktop / Docker Engine
*   Git

## 💻 Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sumaanalikhan/youtube-vibe-checker.git](https://github.com/sumaanalikhan/youtube-vibe-checker.git)
   cd youtube-vibe-checker
