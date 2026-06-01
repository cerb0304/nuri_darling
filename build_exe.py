#!/usr/bin/env python
"""
NURI EXE build skripti
PyInstaller orqali standalone exe faylini yaratadi
"""

import PyInstaller.__main__
import os
import shutil
import sys

def build_exe():
    """EXE faylini yaratish"""
    
    # Eski build fayllarni o'chirish
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('NURI.spec'):
        os.remove('NURI.spec')
    
    print("\n" + "="*50)
    print("NURI EXE YASALMOQDA...")
    print("="*50 + "\n")
    
    # PyInstaller parametrlari
    args = [
        'gui.py',  # asosiy entry point
        '--name=NURI',
        '--onefile',  # bitta EXE faylga
        '--windowed',  # oyna shaklida (CLI yo'q)
        '--icon=ICON',  # ikonka (agar bor bo'lsa)
        '--add-data=.env:.',  # .env faylni qo'shish
        '--hidden-import=PyQt5',
        '--hidden-import=aiogram',
        '--hidden-import=aiohttp',
        '--hidden-import=groq',
        '--hidden-import=pydantic',
        '--hidden-import=edge_tts',
        '--hidden-import=yt_dlp',
        '--hidden-import=feedparser',
        '--collect-all=PyQt5',
        '--collect-all=aiogram',
        '--collect-all=aiohttp',
        '--collect-all=groq',
        '--collect-all=pydantic',
        '--collect-all=edge_tts',
        '--collect-all=yt_dlp',
        '--collect-all=feedparser',
        '--distpath=dist',
        '--buildpath=build',
        '--specpath=.',
        '-y',  # hech qanday so'rovlarni bekor qilish
    ]
    
    # PyInstaller ishga tushirish
    try:
        PyInstaller.__main__.run(args)
        print("\n" + "="*50)
        print("✅ EXE MUVAFFAQIYATLI YARATILDI!")
        print(f"📁 Joylashuvi: dist/NURI.exe")
        print("="*50 + "\n")
        return True
    except Exception as e:
        print(f"\n❌ XATOLIK: {e}")
        return False

if __name__ == "__main__":
    success = build_exe()
    sys.exit(0 if success else 1)
