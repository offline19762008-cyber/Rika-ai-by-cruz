# 🧬 RIKA AI — Advanced Edition

A high-performance, multi-language Telegram AI chatbot built with Python and `python-telegram-bot` v21+, powered by OpenRouter (DeepSeek-V3).

> ⚠️ Educational & experimental project. Use responsibly.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧠 **AI Powered** | DeepSeek-V3 via OpenRouter — fast & smart |
| 💬 **Conversation Memory** | Bot remembers context (up to 20 messages) |
| 🌐 **Multi-Language** | 🇺🇸 English · 🇮🇩 Indonesian · 🇮🇳 Hindi · 🇵🇰 Urdu |
| ⚡ **Fully Async** | Non-blocking httpx — handles 100+ users |
| 🔐 **Force Join** | Require users to join your channel first |
| 🛡️ **Anti-Flood** | Built-in slowmode (2 sec) per user |
| 📊 **User Stats** | `/stats` command shows usage info |
| 🧹 **Reset Chat** | `/reset` clears conversation history |
| 🏓 **Ping/Latency** | `/ping` for bot latency check |
| 📖 **Help Menu** | `/help` shows all bot commands |
| 🔧 **Easy Deploy** | Railway / VPS / Replit compatible |

---

## 📂 Project Structure

```
RIKA-AI/
├── main.py              # Entry point (loads .env, starts bot)
├── telegram_bot.py      # Core bot logic
├── keep_alive.py        # Flask keep-alive server
├── system-prompt.txt    # Custom system prompt
├── bot_config.json      # Bot configuration
├── requirements.txt     # Dependencies
├── .env.example         # Environment template
├── .gitignore           # Git ignore rules
├── railway.toml         # Railway deployment config
└── README.md            # This file
```

---

## 🔧 Installation

### 1. Clone & Setup

```bash
git clone https://github.com/offline19762008-cyber/Rika-ai-by-cruz.git
cd Rika-ai-by-cruz
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your actual values
```

### 3. Run

```bash
python main.py
```

---

## 🔑 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `TELEGRAM_TOKEN` | ✅ | Bot token from @BotFather |
| `OPENROUTER_KEY` | ✅ | API key from openrouter.ai |
| `MODEL_NAME` | ❌ | AI model (default: `deepseek/deepseek-chat`) |
| `API_BASE_URL` | ❌ | API endpoint (default: OpenRouter) |
| `REQUIRED_CHANNEL` | ❌ | Force-join channel username |

---

## 🤖 Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message + language selection |
| `/help` | Show all available commands |
| `/setlang en\|id\|hi\|ur` | Change response language |
| `/reset` | Clear conversation history |
| `/stats` | View your usage statistics |
| `/ping` | Check bot response latency |

---

## 🚀 Deploy on Railway

1. Push to GitHub
2. Connect repo to Railway
3. Set environment variables
4. Deploy!

---

## 📝 License

Personal/Developer License - Redistribution prohibited.

---

**Powered By:** @the_true_creator  
**Credits:** @rika_updats
