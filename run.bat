@echo off
setlocal enabledelayedexpansion

echo 正在激活虚拟环境...
call venv\Scripts\activate

:input_loop
set /p "video_path=请将视频文件拖放到这里（或输入视频路径）: "

if "!video_path!"=="" (
    echo 请输入有效的视频路径
    goto input_loop
)

if not exist "!video_path!" (
    echo 错误：找不到视频文件
    goto input_loop
)

echo 正在处理视频...
python extract_subtitle.py "!video_path!"

echo.
echo 处理完成！
echo 字幕文件已生成在视频所在目录

pause