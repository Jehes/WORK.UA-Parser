@echo off

python -c "import pip" > nul 2>&1
if %errorlevel% neq 0 (
    python -m ensurepip
)
python -c "import requests; import beautifulsoup4" > nul 2>&1
if %errorlevel% neq 0 (
    pip install requests 
    pip install beautifulsoup4
)
