from threading import Thread

from flask import Flask

app = Flask("")


@app.route("/")
def home():
    return "Hello. I am alive!"


def keep_alive(host="0.0.0.0", port=8080) -> Thread:
    t = Thread(target=app.run, kwargs={"host": host, "port": port})
    t.start()
    return t
