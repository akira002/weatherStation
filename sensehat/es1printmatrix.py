from sense_hat import SenseHat
sense = SenseHat()

# Definisco il colore blu
blue = (0, 0, 100)

while True:
    message = "Nome Cognome"
    # Mostro il messaggio a scorrimento
    sense.show_message(message, scroll_speed=0.05, back_colour=blue)
