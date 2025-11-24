from flask import Flask
import schedule
import time
import threading

app = Flask(__name__)

def run_agent():
    print("AI Agent Running... (Script, Animation, Upload)")
    # Yaha baad me full automation add hoga

def scheduler_thread():
    schedule.every().day.at("08:00").do(run_agent)
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=scheduler_thread).start()

@app.route("/")
def home():
    return "YT AI Agent is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
