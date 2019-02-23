@echo off
echo GTA Online Solo Public Lobby Glitch - PC
echo 1 - Apply custom mtu size and run GTA
echo 2 - Apply custom mtu size
echo 3 - Revert changes
set /p Eingabe="Selection: "

if "%Eingabe%"=="1" goto 1
if "%Eingabe%"=="2" goto 2
if "%Eingabe%"=="3" goto 3


:1
cls
echo.
echo Try out different values and find the best for your system
set /p custom="New mtu size (700-900) Recommended 825: "
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
set /p custom="New mtu size (700-900) Recommended 825: "
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
