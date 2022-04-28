#!/usr/bin/env python
import sys
import PySimpleGUI as sg

# Recipe for getting keys, one at a time as they are released
# If want to use the space bar, then be sure and disable the "default focus"

layout = [[sg.Text("Press a key or scroll mouse")],
          [sg.Text("", size=(18, 1), key='text')],
          [sg.Button("OK", key='OK')]]

window = sg.Window("Keyboard Test", layout,
                   return_keyboard_events=True, use_default_focus=False)

# ---===--- Loop taking in user input --- #
while True:
    event, values = window.read()
    text_elem = window['text']
    if event in ("OK", None):
        print(event, "exiting")
        break
    if len(event) == 1:
        text_elem.update(value='%s - %s' % (event, ord(event)))
        
    if event is not None:
        text_elem.update(event)

    if event in ("Left:37", "a"):
        print("izq")
        # Mover un delta hacia adelante
    if event in ("Up:38", "w"):
        print("adelante")
        # Mover un delta hacia adelante
    if event in ("Right:39", "d"):
        print("der")
        # Mover un delta hacia adelante
    if event in ("Down:40", "s"):
        print("atras")
        # Mover un delta hacia adelante        

window.close()