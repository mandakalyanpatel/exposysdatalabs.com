import shutil
import os

base_path = r"C:\Users\manda\.gemini\antigravity-ide\brain\3c924755-e585-4c56-b473-dcf7424d3d15"
dest_path = r"C:\Users\manda\OneDrive\Desktop\New\assets"

files = {
    "media__1784275262018.png": "esecurity.png",
    "media__1784275523166.png": "ai.png",
    "media__1784276219648.jpg": "ml.jpg"
}

for src_name, dst_name in files.items():
    src = f"{base_path}\\{src_name}"
    dst = f"{dest_path}\\{dst_name}"
    shutil.copy(src, dst)
    print(f"Copied {src_name} to {dst_name}")
