temperatura = 0
light2 = 0

def on_button_pressed_a():
    basic.show_string("" + str((temperatura)))
    if temperatura >= 10 and temperatura <= 18:
        basic.show_string("Watering the plant")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    if input.light_level() > 120:
        basic.pause(100)
        basic.show_leds("""
            . . # . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
        basic.pause(100)
        basic.clear_screen()
    else:
        if input.light_level() < 120:
            basic.show_string("Stopped watering the plant")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    global temperatura, light2
    temperatura = input.temperature()
    light2 = input.light_level()
basic.forever(on_forever)
