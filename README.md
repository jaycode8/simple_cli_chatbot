
# 🤖 ChatBot CLI (Dockerized)

A simple AI chatbot running via CLI using Docker and OpenAI.

---

## 📦 Prerequisites

Install Docker:

### 🔧 On Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install docker.io
```

### 🪟 On Windows

1. Download Docker Desktop from [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
2. Install and run Docker Desktop
3. Open **Docker CLI**

---

## 🚀 Usage

### Pull the image from Docker Hub

```bash
docker pull jaycode8/chatbot:v1
```

### Run the chatbot (interactive mode)

```bash
docker run -it --name chatbot jaycode8/chatbot:v1
```

> 🗨️ You'll enter an interactive chat. Type messages to the bot. Type `exit` or `quit` to leave.

---

## 🔁 Restarting the chatbot (if container is stopped)

```bash
docker start -ai chatbot
```

---

## 📋 List containers

```bash
docker ps -a
```

---

## 🧹 Remove container (optional)

```bash
docker rm chatbot
```

---

## 📂 Build locally (optional)

If you want to build the image yourself:

```bash
docker build -t my-chatbot .
docker run -it my-chatbot
```

---

## 🔑 Environment Variables

If you're building your own version, be sure to provide your API token in a `.env` file:

```env
API_TOKEN=your_groq_or_openai_token
```

---

Enjoy chatting! 🤖💬
