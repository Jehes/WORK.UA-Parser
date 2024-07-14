@echo off

:: Check if pip is installed
python -c "import pip" > nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Installing pip...
    python -m ensurepip
)

:: Check if required libraries are installed
python -c "import requests; import beautifulsoup4" > nul 2>&1
if %errorlevel% neq 0 (
    echo Required libraries are not installed. Installing...
    pip install requests 
    pip install beautifulsoup4
)

:: Run main.py
echo Running main.py...
python main.py