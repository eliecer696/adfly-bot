@echo off
title AdFly-Bot installer
color 0a
call :is_installed git , https://git-scm.com/downloads || exit /B %errorlevel%
call :is_installed python , https://www.python.org/ || exit /B %errorlevel%
pip install -Ur requirements.txt
echo Successfully installed AdFly-Bot.
exit /B 0
:is_installed
where %~1 >nul 2>nul
if %errorlevel% neq 0 (
	echo %~1 is not installed or it is not in PATH.
	echo You can install it from %~2
	exit /B 1
)
exit /B 0
