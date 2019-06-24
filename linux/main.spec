# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/home/bulo98/MEGAsync/Projects/media-grabber/linux'],
             binaries=[('./ffmpeg', '.'), ('./ffprobe', '.')],
             datas=[('/home/bulo98/.local/lib/python3.7/site-packages/eel/eel.js', 'eel'), ('web', 'web')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='logo.ico')
