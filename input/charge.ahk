#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#SingleInstance force ; Ensures only one instance of the script is running
SetKeyDelay,40,20 ; Global delay that will occur after each keystroke
Blockinput, On ; Block user or computer input to prevent messing with the script


; Which direction should we charge?
direction = w

; Press key down
SendEvent, {%direction% down}
; Click 20 times and wait 250 ms
; 20 * 250 = 5000ms = 5s
Loop, 20 {
    Click
    Sleep, 250
}
; key up
SendEvent, {%direction% up}

