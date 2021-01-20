from flask import Flask, render_template, request
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/send_sms", methods=["POST"])
def send_sms():
    if request.method == "POST":
        # Strip out form data from request
        phone_number = request.form["phone"]   
        form_message = request.form["message"]

        # Bring in env variables for twilio account  
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")

        # Create the connection to twilio and send message
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body=f"{form_message}",
                            from_="+17193966974",
                            to=f"+1{phone_number}"
                        )

        return render_template("message_sent.html")       
    return home()             

        # print("Acct",account_sid,"TOKEN:", auth_token, "\n\n")
        # return "<h1>Sent!</h1>"
    
if __name__ == "__main__":
    app.run(debug=True)


