# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules

a = Analysis(
    ['app.py'],
    pathex=['.'],  # Ensure PyInstaller looks in the current directory
    binaries=[],
    datas=[
        ('database.db', '.'),  # Include database file
        ('templates', 'templates'),  # Include HTML templates
        ('static', 'static')  # Include CSS, JS, etc.
    ],
    hiddenimports=collect_submodules('flask'),  # Ensure Flask dependencies are included
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='booksage',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Set to False if you want to hide the terminal window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
