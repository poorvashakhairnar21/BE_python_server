# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['zoroServer.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('backend_request.py', '.'),         # Include local .py files
        ('request_api.py', '.'),
        ('zoroServer.py', '.'),                  # Only if used by imports
        ('assitant_client/*.py', 'assitant_client'),  # Include subpackage
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='zoroServer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Set to False if you want no terminal window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
