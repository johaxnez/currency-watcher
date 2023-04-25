import requests
import smtplib

MY_EMAIL = "YOUR MAIL"
MY_PASSWORD = "MAIL PASSWORD"
TARGET_MAIL = "TARGET MAIL"

def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="TARGET_MAIL",
            msg="Subject:NOK stronk"
                "\n"
                "\n"
                "NOK in stronger than SEK"
        )


API_ENDPOINT = "https://api.apilayer.com/currency_data/convert"
API_KEY = "YOUR API KEY"


headers = {
    "apikey": API_KEY
}

parameters = {
    "amount": "100",
    "from": "NOK",
    "to": "SEK"
}

response = requests.get(url=API_ENDPOINT, headers=headers, params=parameters)
response.raise_for_status()

exchange = response.json()
target = exchange["result"]


if target > 100.5:
    send_mail()
