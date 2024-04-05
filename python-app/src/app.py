from flask import Flask, request
import time
import stomp
import os

app = Flask(__name__)


@app.route("/send_message", methods=["POST"])
def send_message():
    message = request.json["message"]
    conn.send(body=message, destination="/queue/test")
    return "Message sent: " + message


class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('Received an error "%s"' % message)

    def on_message(self, headers, message):
        print('Received a message "%s"' % message)


conn = stomp.Connection()
conn.set_listener("", MyListener())
stomp_host = os.getenv("STOMP_HOST")
stomp_port = os.getenv("STOMP_PORT")
# conn.start()
conn.connect("admin", "admin", wait=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
