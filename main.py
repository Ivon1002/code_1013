def on_button_pressed_a():
    for y in range(5):
        for x in range(5):
            led.plot(x, y)
            basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
