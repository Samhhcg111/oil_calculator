# -*- mode: python ; coding: utf-8 -*-
import tkinter
from tkinter import ttk
import random
import os
import inspect
import matplotlib

block_cipher = None


a = Analysis(
    ['oil_app.py'],
    pathex=['C:\\Users\\user\\OneDrive\\桌面\\essential_oil_ws\\oil_app.py'],
    binaries=[('C:\\Users\\user\\OneDrive\\桌面\essential_oil_ws\\lib','lib')],
    datas=[],
    hiddenimports=['tkinter','matplotlib',"Pillow","numpy"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='oil_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='oil_app',
)
