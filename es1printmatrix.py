from sense_hat import SenseHat
sense = SenseHat()

# Define the colours red and green
blue = (0, 0, 100)

while True:
    message = "Nome Cognome"
    # Display the scrolling message
    sense.show_message(message, scroll_speed=0.05, back_colour=blue)

