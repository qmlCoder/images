from pathlib import Path
import shutil

def sync_imgs():
    raw_imgs=Path('lab220/heads/students')
    for each in raw_imgs.iterdir():
        print(each.stem)
        lifes=Path(f'lab220/lifeImgs/{each.stem}') # 生活照文件
        if not lifes.exists():lifes.mkdir()

sync_imgs()