import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from yt_dlp import YoutubeDL

class YouTubeMP3Downloader(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🎵 YouTube to MP3")
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("background-color: #121212; color: white;")

        # Set font
        font = QFont("Arial", 12, QFont.Weight.Bold)

        # Layout
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # URL Input
        self.url_label = QLabel("🔗 Enter YouTube URL:")
        self.url_label.setFont(font)
        self.url_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.url_input = QLineEdit()
        self.url_input.setStyleSheet("background-color: #1E1E1E; color: white; padding: 10px; border-radius: 5px; text-align: center;")
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)

        # Download Button
        self.download_button = QPushButton("⬇️ Download MP3")
        self.download_button.setFont(font)
        self.download_button.setStyleSheet("background-color: #BB86FC; color: white; padding: 12px; border-radius: 5px;")
        self.download_button.clicked.connect(self.download_audio)
        layout.addWidget(self.download_button)

        # Status Label
        self.status_label = QLabel("")
        self.status_label.setFont(font)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        self.setLayout(layout)
        self.save_dir = os.path.join(os.path.expanduser("~"), "Downloads")

        # Create save directory if it doesn't exist
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        # Determine FFmpeg path
        if getattr(sys, 'frozen', False):
            self.ffmpeg_path = os.path.join(sys._MEIPASS, "ffmpeg")
        else:
            self.ffmpeg_path = "ffmpeg"  # Assume it's installed globally

    def download_audio(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.critical(self, "❌ Error", "Please enter a YouTube URL.")
            return

        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(self.save_dir, '%(title)s.%(ext)s'),
                'ffmpeg_location': self.ffmpeg_path,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }],
                'postprocessor_args': [
                    '-q:a', '0',
                    '-b:a', '320k',
                ],
            }

            self.status_label.setText("⌛ Downloading...")
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.status_label.setText("✅ Download complete!")
            QMessageBox.information(self, "🎉 Success", "MP3 downloaded successfully!")
        except Exception as e:
            QMessageBox.critical(self, "❌ Error", f"Download failed: {e}")
            self.status_label.setText("⚠️ Download failed.")

# Run Application
if __name__ == "__main__":
    app = QApplication([])
    window = YouTubeMP3Downloader()
    window.show()
    app.exec()
