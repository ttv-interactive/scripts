#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#SingleInstance force ; Ensures only one instance of the script is running
Blockinput, On ; Blocks all input

freezeTime = 3000 ; 3000 ms = 3 s

; If any buttons are pressed down while the script is running - the keys will still be held down while the script is running
; Release the movement keys
SendInput {w up}
SendInput {s up}
SendInput {a up}
SendInput {d up}
; You can add move keys if you want to - just like above ^

Sleep, freezeTime ; Sleeps
Blockinput, Off ; Unblocks all input