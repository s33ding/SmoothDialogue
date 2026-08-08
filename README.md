# SmoothDialogue

SmoothDialogue is a web app built with Flask to improve written communication in **Portuguese**. It helps refine messages to be clearer, more professional, and friendly — designed to help communicate better with work teams in **Brazil**.

## 🚀 Features
- Enhances text clarity, professionalism, and tone
- Maintains technical terms in **English**
- Uses emojis to reinforce the message
- Powered by **AWS Bedrock** (Claude Haiku 4.5)
- Modern dark-mode UI with glassmorphism
- Keyboard shortcut: `Ctrl+Enter` to submit

## 🛠️ Tech Stack
- **Python 3** + **Flask**
- **AWS Bedrock** (Anthropic Claude)
- **HTML, CSS, JavaScript**
- **Docker**

## 📦 Setup

### 1. Clone
```bash
git clone https://github.com/s33ding/SmoothDialogue.git
cd SmoothDialogue
```

### 2. Environment
Create a `.env` file:
```bash
FLASK_SECRET_KEY=your_secret_key
```

AWS credentials are mounted from `~/.aws` using the `iesb` profile.

### 3. Run
```bash
docker compose up --build -d
```

Access at **http://smooth.com.br** (requires `/etc/hosts` entry).

### 4. Local DNS (optional)
```bash
echo "127.0.0.1   smooth.com.br" | sudo tee -a /etc/hosts
echo "127.0.0.1   smooth.com" | sudo tee -a /etc/hosts
```

## 🔧 How to Use
1. Enter your message in **Portuguese**
2. Click **Melhorar Comunicação** (or `Ctrl+Enter`)
3. Review the enhanced version
4. Copy and use it in your work interactions
