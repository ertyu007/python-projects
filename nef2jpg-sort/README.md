# 📷 NEF to JPG Batch Converter (Hacker Mode Edition)

โปรเจกต์ Python สำหรับแปลงไฟล์ `.NEF` (RAW จากกล้อง Nikon) และคัดลอก `.JPG` เดิมไปยังโฟลเดอร์ใหม่  
พร้อมตั้งชื่อใหม่เรียงลำดับ เช่น `image1.jpg`, `image2.jpg`, ..., `image350.jpg`

> ✨ พร้อมแสดงผลแบบ "Terminal Hacker Style" สนุกเวลารัน 😎

---

## 🚀 Features

- 🔄 แปลงไฟล์ `.NEF` เป็น `.JPG` โดยใช้ `rawpy`
- 📁 คัดลอกไฟล์ `.JPG` เดิมไปยังโฟลเดอร์ปลายทาง
- 🔢 ตั้งชื่อเรียงลำดับอัตโนมัติ `image1.jpg`, `image2.jpg`, ...
- 📏 แสดงขนาดไฟล์ ต้นทาง/ปลายทาง
- 🎞️ Animation เท่ ๆ แบบ Terminal Hacker (typing effect + loading bar)
- 📸 รองรับไฟล์จำนวนมาก (เช่น 350 รูปขึ้นไป)

---

## 📂 โครงสร้างโปรเจกต์

- ตัวอย่างที่ตั้งโฟล์เดอร์รูปภาพ `C:\Users\ชื่อคุณ\Pictures\camera`

```
📁 camera/               # โฟลเดอร์ต้นทาง (รวม .nef และ .jpg)
├── DSC_0001.NEF
├── DSC_0002.JPG
└── ...

📁 converted_jpg/        # โฟลเดอร์ปลายทาง (ระบบจะสร้างให้)
├── image1.jpg
├── image2.jpg
└── ...

📄 convert_images.py     # สคริปต์หลัก
```

---

## ⚙️ วิธีใช้งาน

### 1. ติดตั้ง Python + ไลบรารีที่จำเป็น

```bash
pip install rawpy imageio
```

---

### 2. ตั้งค่าเส้นทางโฟลเดอร์ใน `convert_images.py`

```python
input_folder = r'C:\Users\ชื่อคุณ\Pictures\camera'
output_folder = r'C:\Users\ชื่อคุณ\Pictures\converted_jpg'
```

---

### 3. วางไฟล์ `.nef` และ `.jpg` ในโฟลเดอร์ต้นทาง แล้วรัน:

```bash
python convert_images.py
```

---

### 4. ดูผลลัพธ์ใน Terminal + ไฟล์ JPG ใหม่ใน `converted_jpg/`

---

## 🖥️ ตัวอย่างผลลัพธ์ (Terminal)

```
Processing file #1
 - Original filename : DSC_0001.NEF
 - File size         : 24.6 MB
 - Action            : Converting RAW (.nef) to JPG...
 - Result            : ✔ Converted → image1.jpg

Processing file #2
 - Original filename : DSC_0002.JPG
 - File size         : 2.4 MB
 - Action            : Copying existing JPG...
 - Result            : ✔ Copied → image2.jpg
```

---

## 📘 License

Free to use and modify (MIT License).  
ถ้าชอบสามารถแชร์ต่อหรือให้เครดิตได้เลยครับ 🤍

---

## 👨‍💻 ผู้พัฒนา

โดย [คุณ](https://github.com/yourname)  
Python-based image tools with style 😎
