# 🎉 YTMP3 – YouTube to MP3 Downloader

A minimalist, cross-platform **YouTube to MP3** downloader with a **brutalist UI** and emoji integration.  
Built with **PyQt6, yt-dlp, and FFmpeg**, this app provides a **simple** and **fast** way to convert YouTube videos to **high-quality MP3s**.

## 🚀 Features
- **Fast & Simple**: Enter a YouTube URL and click **Download**
- **Max Quality**: Converts audio to **320kbps MP3**
- **Cross-Platform**: Works on **macOS, Windows, and Linux**
- **Minimalist UI**: Modern brutalist design with dark mode and emojis 🎵🔥
- **FFmpeg Bundled**: No need to install FFmpeg manually

## 📚 Installation

### 🏢 1️⃣ Clone the Repository
```bash
git clone https://github.com/jakubvonasek/ytmp3.git
cd ytmp3
```

### 🛠️ 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ 3️⃣ Run the App
```bash
python script.py
```

## 📀 Build the App (for macOS)
To package YTMP3 into a **standalone macOS app**, run:
```bash
./build.sh
```
This will generate `YTMP3.app` inside `/Applications/`.

## 🛢️ Uninstall
To remove YTMP3 from your system:
```bash
./uninstall.sh
```

## 🔧 Requirements
- **Python 3.12+**
- **PyQt6**
- **yt-dlp**
- **FFmpeg (bundled or system-installed)**

## 💡 License
MIT License. Feel free to modify and improve! 🚀
