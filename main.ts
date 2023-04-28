input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showLeds(`
        . . # . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    `)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
                . . # . .
                . . . . .
                . . . . .
                . . . . .
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
                . . # . .
                . . . . .
                . . . . .
                . . . . .
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
                . . # . .
                . . # . .
                . . . . .
                . . . . .
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . # . .
                . . # . .
                . . . . .
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . # . .
                . . . . .
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . # . .
                . . # . .
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . # # # .
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # # # # #
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # # . # #
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . #
    `)
    basic.pause(100)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    for (let index = 0; index < 12; index++) {
        basic.showIcon(IconNames.Yes)
        basic.pause(10)
        basic.showIcon(IconNames.No)
    }
    basic.showIcon(IconNames.Skull)
})
