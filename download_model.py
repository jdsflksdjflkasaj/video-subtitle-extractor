import os
import ssl
import requests
import urllib3
from tqdm import tqdm

# 禁用SSL验证警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 模型文件及其URL
MODEL_FILES = {
    'config.json': 'https://huggingface.co/Systran/faster-whisper-base/resolve/main/config.json',
    'model.bin': 'https://huggingface.co/Systran/faster-whisper-base/resolve/main/model.bin',
    'tokenizer.json': 'https://huggingface.co/Systran/faster-whisper-base/resolve/main/tokenizer.json',
    'vocabulary.txt': 'https://huggingface.co/Systran/faster-whisper-base/resolve/main/vocabulary.txt'
}

def download_file(url, output_path):
    try:
        # 创建输出目录
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # 创建自定义SSL上下文
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        # 设置请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # 发送请求并获取文件大小
        response = requests.get(url, headers=headers, stream=True, verify=False)
        total_size = int(response.headers.get('content-length', 0))
        
        # 使用tqdm显示下载进度
        with open(output_path, 'wb') as f, tqdm(
            desc=os.path.basename(output_path),
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for data in response.iter_content(chunk_size=1024):
                size = f.write(data)
                pbar.update(size)
                
        return True
    except Exception as e:
        print(f"下载 {url} 时发生错误: {str(e)}")
        return False

def main():
    # 设置模型保存目录
    model_dir = os.path.join('models', 'faster-whisper-base')
    
    print("开始下载模型文件...")
    success_count = 0
    
    for filename, url in MODEL_FILES.items():
        output_path = os.path.join(model_dir, filename)
        print(f"\n正在下载: {filename}")
        
        if download_file(url, output_path):
            success_count += 1
            print(f"{filename} 下载成功！")
        else:
            print(f"{filename} 下载失败！")
    
    print(f"\n下载完成！成功: {success_count}/{len(MODEL_FILES)}")

if __name__ == '__main__':
    main()