import requests
import smtplib

MY_EMAIL = "YOUR MAIL@mail.com"
MY_PASSWORD = "YOUR PASSWORD"


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="TARGET MAIL@mail.com",
            msg="Subject:NOK stronk"
                "\n"
                "\n"
                "NOK in stronger than SEK"
        )



NEW_ENDPOINT = "https://api.currencyapi.com/v3/latest"
NEW_API_KEY = "YOUR KEY"

headers = {
    "apikey": API_KEY
}

new_parameters = {
    "apikey": NEW_API_KEY,
    "base_currency": "NOK",
    "currencies": ["SEK"]
}

parameters = {
    "amount": "100",
    "from": "NOK",
    "to": "SEK"
}

response = requests.get(url=NEW_ENDPOINT, params=new_parameters)

response.raise_for_status()

exchange = response.json()
target = exchange["data"]["SEK"]["value"]



if target > 1.005:
    send_mail()
