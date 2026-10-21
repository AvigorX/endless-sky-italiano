@echo off
rem Avvia Endless Sky in INGLESE.
rem Il motore 0.11.4 non ha un selettore di lingua per i dati: si sceglie l'insieme
rem di dati prima dell'avvio. Robocopy /MIR rende "data" identica a "data-en".
cd /d "%~dp0"
robocopy "data-en" "data" /MIR /NFL /NDL /NJH /NJS /NP >nul
start "" "build\Endless Sky.exe" --resources .
