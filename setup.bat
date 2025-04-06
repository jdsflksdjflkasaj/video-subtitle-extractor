@echo off
setlocal enabledelayedexpansion

echo 正在检查 Python 环境...
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo 错误：未找到 Python，请先安装 Python 3.8 或更高版本
    pause
    exit /b 1
)

echo 正在创建虚拟环境...
python -m venv venv

echo 正在激活虚拟环境...
call venv\Scripts\activate

echo 正在安装依赖...

if exist torch-2.1.0+cpu-cp311-cp311-win_amd64.whl (
    echo 正在安装本地 PyTorch...
    pip install torch-2.1.0+cpu-cp311-cp311-win_amd64.whl
) else (
    echo 正在从网络安装 PyTorch...
    pip install torch==2.1.0 --index-url https://download.pytorch.org/whl/cpu
)

echo 正在安装其他依赖...
pip install -r requirements.txt

echo 正在下载模型文件...
python download_model.py

echo 环境配置完成！
echo 请运行 run.bat 来使用程序

pause