@echo off
REM QA Testing Project Setup Script for React Application

echo 🚀 Setting up QA Testing Environment for React Project...
echo ==================================================

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo  Node.js is not installed. Please install Node.js first.
    echo Visit: https://nodejs.org/
    pause
    exit /b 1
)

echo  Node.js is installed
echo  npm is available

REM Install project dependencies
echo 📦 Installing project dependencies...
npm install

REM Install testing dependencies
echo 🧪 Installing testing frameworks...
npm install --save-dev @testing-library/react @testing-library/jest-dom @testing-library/user-event
npm install --save-dev cypress
npm install --save-dev jest-environment-jsdom

REM Create test directories
echo 📁 Creating test directories...
if not exist "tests\unit" mkdir tests\unit
if not exist "tests\integration" mkdir tests\integration
if not exist "tests\e2e" mkdir tests\e2e
if not exist "tests\performance" mkdir tests\performance
if not exist "tests\fixtures" mkdir tests\fixtures
if not exist "tests\helpers" mkdir tests\helpers
if not exist "reports" mkdir reports
if not exist "logs" mkdir logs

echo Setup complete!
echo.
echo Next steps:
echo 1. Start the development server: npm start
echo 2. Run tests: npm test
echo 3. Check README.md for detailed instructions
echo.
pause
