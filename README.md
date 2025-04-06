# Video Subtitle Extractor

[中文说明](使用说明.md)

A tool for automatically extracting subtitles from videos, particularly suitable for Chinese educational videos and lectures.

## Features

- Fast and accurate speech recognition using faster-whisper
- Optimized for Chinese language
- Generates standard SRT format subtitles
- Local processing, no internet required after model download
- Supports various video formats

## Requirements

- Windows OS
- Python 3.8 or higher
- 4GB RAM minimum
- 2GB free disk space

## Installation

1. Download this repository
2. Double click `setup.bat`
3. Wait for the installation to complete

## Usage

1. Double click `run.bat`
2. Drag and drop your video file into the window
3. Wait for processing to complete
4. Find the generated subtitle file (.srt) in the same directory as your video

## Directory Structure

```
├── extract_subtitle.py    # Main script
├── download_model.py      # Model download script
├── requirements.txt       # Python dependencies
├── setup.bat             # Setup script
├── run.bat               # Run script
├── README.md             # English documentation
└── 使用说明.md            # Chinese documentation
```

## Common Issues

1. First run requires model download (~1GB)
2. Make sure you have stable internet for initial setup
3. Processing time depends on video length
4. Better audio quality leads to better recognition

## Technical Support

If you encounter any issues:
1. Check the documentation
2. Check common issues section
3. Contact developer for support

## License

MIT License

## Acknowledgments

- [faster-whisper](https://github.com/guillaumekln/faster-whisper)
- [moviepy](https://github.com/Zulko/moviepy)