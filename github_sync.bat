@echo off
cd "G:/My Drive/Methods/ML_Python" 

REM Check if the folder is already a Git repository
if not exist .git (
    git init
    echo Initialized Git repository.
) else (
    echo Git repository already exists.
)

REM Check if the remote origin is already set
git remote | find "origin" >nul
if errorlevel 1 (
    git remote add origin https://github.com/r4miao/ML_python.git
    echo Remote origin added.

    REM Run git pull only at the initiating stage
    git pull origin master --allow-unrelated-histories
    echo Pulled remote repository to link with local folder.
) else (
    echo Remote origin already exists.
)

REM Add and commit changes
git add .
git commit -m "Initial commit" 2>nul || echo Commit already exists.

REM Ensure the branch is named 'master'
git branch -M master

REM Push changes to the remote repository
git push origin master

pause  REM Keeps the Command Prompt open


