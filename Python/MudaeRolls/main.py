#!/bin/python3
import keyboard, sys

if len(sys.argv) > 1:
    try:
        rolls = int(sys.argv[1])
        key = keyboard.key_to_scan_codes('enter')[0]

        print("Ready to roll!")

        keyboard.wait(key)

        for _ in range(rolls):
            keyboard.press_and_release('shift + 4')
            keyboard.write('wa\n', 0.25)

            if keyboard.is_pressed(key): sys.exit()

    except (ValueError, TypeError):
        print("Usage: mudaerolls <number>")
