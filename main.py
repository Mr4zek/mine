def on_button_pressed_a():
    basic.show_leds("""
        . . # . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
                . . # . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . # . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . # . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . # . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . # . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . # . .
                . . # . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . # # # .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # # # # #
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # # . # #
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . #
    """)
    basic.pause(100)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    for index in range(12):
        basic.show_icon(IconNames.YES)
        basic.pause(10)
        basic.show_icon(IconNames.NO)
    basic.show_icon(IconNames.SKULL)
input.on_button_pressed(Button.B, on_button_pressed_b)
