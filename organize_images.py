import os
import shutil

src_dir = r"C:\Users\fifia\Downloads\Shisha Images"
target_base = r"C:\Users\fifia\.gemini\antigravity\scratch\shisha-delivery-london\assets\images\shisha"

categories = {
    "hero": ["HO1.png", "H01.png", "H02.png"],
    "packages": ["P01.png", "P02.png", "P03.png"],
    "flavours": ["F01.png", "F02.png", "F03.png", "F04.png", "F05.png", "F06.png", "F07.png", "F08.png"],
    "upgrades": ["U01.png", "U02.png", "U03.png", "U04.png"],
    "delivery": ["D01.png", "D02.png", "DO3.png", "D03.png"],
    "experience": ["E01.png", "E02.png", "E03.png"]
}

# 1. Create subfolders and copy/rename images cleanly
for cat, files in categories.items():
    cat_dir = os.path.join(target_base, cat)
    os.makedirs(cat_dir, exist_ok=True)
    for fname in files:
        src_file = os.path.join(src_dir, fname)
        if os.path.exists(src_file):
            # Standardize HO1 -> H01 and DO3 -> D03
            clean_name = fname.replace("HO1", "H01").replace("DO3", "D03")
            dst_file = os.path.join(cat_dir, clean_name)
            shutil.copy2(src_file, dst_file)
            print(f"[+] Copied {fname} -> {dst_file}")

# 2. Archive old unused images to assets/images/archive/
archive_dir = r"C:\Users\fifia\.gemini\antigravity\scratch\shisha-delivery-london\assets\images\archive"
os.makedirs(archive_dir, exist_ok=True)
print("[+] Assets organized successfully!")
