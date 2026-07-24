from flask import Flask
from threading import Thread
import logging

logger = logging.getLogger(__name__)

app = Flask('')

@app.route('/')
def home():
    return "Bot Running... ✅"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

def run():
    try:
        app.run(host='0.0.0.0', port=8080, debug=False, use_reloader=False)
    except Exception as e:
        logger.error(f"Flask error: {e}")

def keep_alive():
    """Start Flask server in a daemon thread."""
    t = Thread(target=run, daemon=True)
    t.start()
    logger.info("✅ Keep-alive server started on port 8080")
