@echo off
TITLE Python_PE: MCPE Server ::we can edit this whenever
MODE CON: COLS=125 LINES=50 ::this is the size of the command prompt screen
goto start
:start
color 0A ::black on green
cls
echo Python_PE is starting...
python Python_PE.py || goto failed
echo Python_PE has started!
:failed
color 0C
echo Python_PE has failed to start!
pause ::shows the "Press any key to continue button" message
