import rawpy
import imageio
import os
import shutil
import time
import sys

def type_effect(text, delay=0.004):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(duration=1.0, length=30):
    for _ in range(length):
        time.sleep(duration / length)
        sys.stdout.write('=')
        sys.stdout.flush()
    print()

def format_size(bytesize):
    if bytesize >= 1024 ** 2:
        return f"{bytesize / (1024 ** 2):.2f} MB"
    else:
        return f"{bytesize / 1024:.1f} KB"

# --- ตั้งค่าโฟลเดอร์ ---
input_folder = r'C:\Users\reall\Pictures\102D7100'
output_folder = r'C:\Users\reall\Pictures\RAW_to_JPG'
os.makedirs(output_folder, exist_ok=True)

# --- รวมไฟล์ .nef และ .jpg ---
all_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.nef', '.jpg'))]
all_files.sort()

# --- เริ่มกระบวนการ ---
type_effect(":: เริ่มประมวลผลภาพทั้งหมด ::")
loading_bar()

for index, filename in enumerate(all_files, start=1):
    input_path = os.path.join(input_folder, filename)
    output_filename = f'image{index}.jpg'
    output_path = os.path.join(output_folder, output_filename)

    try:
        file_size = os.path.getsize(input_path)
        size_str = format_size(file_size)
    except:
        size_str = "Unknown size"

    type_effect(f"\nProcessing file #{index}")
    type_effect(f" - Original filename : {filename}")
    type_effect(f" - File size         : {size_str}")

    if filename.lower().endswith('.nef'):
        try:
            type_effect(f" - Action            : Converting RAW (.nef) to JPG...")
            with rawpy.imread(input_path) as raw:
                rgb = raw.postprocess()
                imageio.imsave(output_path, rgb)
            type_effect(f" - Result            : ✔ Converted → {output_filename}")
        except Exception as e:
            type_effect(f" - Error             : ✖ Failed to convert: {e}")
    elif filename.lower().endswith('.jpg'):
        try:
            type_effect(f" - Action            : Copying existing JPG...")
            shutil.copy2(input_path, output_path)
            type_effect(f" - Result            : ✔ Copied → {output_filename}")
        except Exception as e:
            type_effect(f" - Error             : ✖ Failed to copy: {e}")

# --- เสร็จสิ้น ---
type_effect("\n:: เสร็จสิ้นการแปลง/คัดลอกไฟล์ทั้งหมด ::")
loading_bar()
