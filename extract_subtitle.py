import os
import ssl
import urllib3
import torch
from faster_whisper import WhisperModel
from moviepy.editor import VideoFileClip

# 禁用SSL验证警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 设置网络超时和重试次数
timeout = urllib3.Timeout(connect=60, read=60)
retries = urllib3.Retry(total=10, backoff_factor=0.5)

# 创建自定义SSL上下文
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# 设置环境变量
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
os.environ['HF_HOME'] = os.path.join(os.getcwd(), 'cache')
os.environ['TRANSFORMERS_CACHE'] = os.path.join(os.getcwd(), 'cache')
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'
os.environ['HF_HUB_ENABLE_HF_TRANSFER'] = '1'

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    msecs = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{msecs:03d}"

def download_progress_callback(progress):
    print(f"下载进度: {progress:.1f}%")

def extract_subtitle(video_path):
    try:
        print("正在初始化模型...")
        model = WhisperModel(
            'base',
            device='cuda' if torch.cuda.is_available() else 'cpu',
            download_root='models',
            local_files_only=False
        )
        
        print("正在提取音频...")
        video = VideoFileClip(video_path)
        audio = video.audio
        
        print("正在识别语音...")
        segments, _ = model.transcribe(
            audio.to_soundarray(),
            language='zh',
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=500)
        )
        
        output_path = os.path.splitext(video_path)[0] + '.srt'
        print(f"正在生成字幕文件: {output_path}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for i, segment in enumerate(segments, 1):
                start_time = format_timestamp(segment.start)
                end_time = format_timestamp(segment.end)
                f.write(f"{i}\n{start_time} --> {end_time}\n{segment.text}\n\n")
        
        print("字幕提取完成！")
        video.close()
        audio.close()
        
    except Exception as e:
        print(f"发生错误: {str(e)}")
        raise

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("使用方法: python extract_subtitle.py <视频文件路径>")
        sys.exit(1)
    
    video_path = sys.argv[1]
    if not os.path.exists(video_path):
        print(f"错误: 找不到视频文件 {video_path}")
        sys.exit(1)
    
    extract_subtitle(video_path)