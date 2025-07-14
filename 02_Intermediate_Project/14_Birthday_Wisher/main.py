import smtplib

my_email = "aryan07chaudhari@gmail.com"
password = "dvfx hoeg bwvx obpd"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() # starttls make our connection secure
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="bunnys.laptop.00@gmail.com",
                        msg="Subject:hello\n\nJust trying to send email through python smtplib"
    )




