@echo off
echo GTA Online Solo Public Lobby Glitch - PC
echo 1 - Anwenden und GTA starten
echo 2 - Anwenden
echo 3 - R�ckg�ngig
set /p Eingabe="Auswahl: "

if "%Eingabe%"=="1" goto 1
if "%Eingabe%"=="2" goto 2
if "%Eingabe%"=="3" goto 3


:1
cls
echo.
set /p custom="Neuer MTU-Wert (700-900) OPTIMAL 825!!: "
cls
netsh interface ipv4 show subinterfaces
netsh interface ipv6 show subinterfaces
timeout /t 2 > NUL
echo.
netsh interface ipv4 set subinterface "Ethernet" mtu="%custom%" store=persistent
netsh interface ipv6 set subinterface "Ethernet" mtu="%custom%" store=persistent
timeout /t 2 > NUL
ipconfig /release
ipconfig /renew
timeout /t 2 > NUL
netsh interface ipv4 show subinterfaces
netsh interface ipv6 show subinterfaces
timeout /t 4 > NUL
echo.
cd "C:\Program Files\internet explorer"
iexplore.exe steam://rungameid/271590
taskkill /f /im iexplore.exe
exit

:2
cls
echo.
set /p custom="Neuer MTU-Wert (700-900) OPTIMAL 825!!: "
cls
netsh interface ipv4 show subinterfaces
netsh interface ipv6 show subinterfaces
timeout /t 2 > NUL
echo.
netsh interface ipv4 set subinterface "Ethernet" mtu="%custom%" store=persistent
netsh interface ipv6 set subinterface "Ethernet" mtu="%custom%" store=persistent
timeout /t 2 > NUL
ipconfig /release
ipconfig /renew
timeout /t 2 > NUL
netsh interface ipv4 show subinterfaces
netsh interface ipv6 show subinterfaces
timeout /t 4 > NUL
echo.
exit

:3
cls
netsh interface ipv4 show subinterfaces
netsh interface ipv6 show subinterfaces
timeout /t 2 > NUL
echo.
netsh interface ipv4 set subinterface "Ethernet" mtu=1500 store=persistent
netsh interface ipv6 set subinterface "Ethernet" mtu=1492 store=persistent
timeout /t 2 > NUL
ipconfig /release
ipconfig /renew
timeout /t 2 > NUL
netsh interface ipv4 show subinterfaces
netsh interface ipv6 show subinterfaces
timeout /t 4 > NUL
echo.
exit
