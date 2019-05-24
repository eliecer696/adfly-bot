title AdFly-Bot installer
color 0a
where python >nul 2>nul
if %errorlevel% neq 0 (
	echo Python is not installed or it is not in PATH.
	echo You can install it from https://www.python.org/
	exit 1
)
pip install -r requirements.txt
echo Successfully installed AdFly-Bot.
