import os
import sys
import logging
from dotenv import load_dotenv

# === Load .env FIRST before anything else ===
load_dotenv()

# === Setup logging early ===
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.WARNING)

# === Validate required env vars ===
required_vars = ["TELEGRAM_TOKEN", "OPENROUTER_KEY"]
missing = [v for v in required_vars if not os.getenv(v)]
if missing:
    logger.error(f"❌ Missing environment variables: {', '.join(missing)}")
    logger.error("   Set them in your hosting platform or .env file.")
    sys.exit(1)

logger.info("✅ All required environment variables are set")

try:
    from keep_alive import keep_alive
    import telegram_bot
    
    if __name__ == "__main__":
        logger.info("🚀 Starting WormGPT Bot...")
        keep_alive()
        telegram_bot.run_bot()
        
except ImportError as e:
    logger.error(f"❌ Import error: {e}")
    logger.error("   Make sure all requirements are installed: pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    logger.error(f"❌ Unexpected error: {e}", exc_info=True)
    sys.exit(1)
