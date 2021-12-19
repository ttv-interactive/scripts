#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.

#SingleInstance force ; Ensures only one instance of the script is running
Blockinput, On ; Block user or computer input to prevent messing with the script
SendMode, Event ; Switches to the SendInput method for Event

amount = 100
loop %amount% {
    DllCall("mouse_event", uint, 1, int, 100, int, 0)
    Sleep, 1
}

