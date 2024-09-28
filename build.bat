@echo off

@REM 构建前端项目
cd electron-app
call npm install
call npm run build:win
cd ..

@REM 构建后端项目
cd backend
call pdm install
cd ..

@REM 清理现有文件
rd /s /q dist

@REM 移动目标文件
move electron-app\dist dist
copy electron-app\start_bed.bat dist\start_bed.bat
mkdir dist\server
copy backend dist\server
