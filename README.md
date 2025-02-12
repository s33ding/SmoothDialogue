# SmoothDialogue

SmoothDialogue is a web app built with Flask to improve written communication in **Portuguese**. It helps refine messages to be clearer, more professional, and friendly. This is designed to help me communicate better with my work team in **Brazil**.

## 🚀 Features
- Enhances text clarity, professionalism, and tone.
- Maintains technical terms in **English**.
- Allows optional context for better adjustments.
- Utilizes the **OpenAI API** for text refinement.

## 🛠️ Tech Stack
- **Python 3**
- **Flask**
- **OpenAI API**
- **HTML, CSS, JavaScript**
- **Docker**

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/smoothdialogue.git
cd smoothdialogue
```

### 2️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add:
```bash
OPENAI_API_KEY=your_openai_api_key
FLASK_SECRET_KEY=your_secret_key
```

### 3️⃣ Running with Docker
#### Build and Start the Container
```bash
docker-compose up --build
```
The app will be running in a containerized environment at `http://127.0.0.1:5000/`.

#### Stopping the Container
```bash
docker-compose down
```

## 🔧 How to Use
1. Enter your message in **Portuguese**.
2. Click **Improve Communication**.
3. Review the enhanced version of your message.
4. Copy and use it in your work interactions.

## 🤝 Acknowledgments
Thanks to everyone contributing to making communication clearer and more effective! 😊

