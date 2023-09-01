from yt_dlp import YoutubeDL
import tkinter as tk
import tkinter.ttk as ttk
import threading
import os

root: tk.Tk = tk.Tk()
ydl: YoutubeDL = YoutubeDL()

root.title("Youtube Downloader")
root.geometry("320x80")

url: tk.StringVar = tk.StringVar()

def onClick() -> None:
    def download(url: str) -> None:
        os.makedirs(f"{os.environ['HOME']}/Movies/YouTube", exist_ok=True)
        ydl_opts: dict = {'format': 'best','outtmpl': f"{os.environ['HOME']}/Movies/YouTube/%(title)s.%(ext)s"}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        progress_progressbar.stop()
        progress.destroy()

    progress: tk.Toplevel = tk.Toplevel(root)
    progress.title("Downloading...")
    progress.geometry("500x10")
    progress_progressbar: ttk.Progressbar = ttk.Progressbar(progress, orient="horizontal", length=500, mode="determinate")
    progress_progressbar.pack(anchor=tk.CENTER,expand=True)
    progress_progressbar.start(10)
    threading.Thread(target=download, args=(url.get(),)).start()

ttk.Entry(root, width=50, textvariable=url).pack(anchor=tk.CENTER,expand=True)

ttk.Button(root, text="Download", command=onClick).pack(anchor=tk.CENTER,expand=True)

if __name__ == "__main__":
    root.mainloop()