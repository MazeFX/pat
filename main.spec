# -*- mode: python -*-

block_cipher = None


added_files = [('lumberjack_config.json', '.')]

a = Analysis(['main.py'],
             pathex=['C:\\PDE\\envs\\qt\\pat\\Scripts', 'C:\\PDE\\envs\\qt\\pat\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\PDE\\projects\\qt\\pat'],
             binaries=None,
             datas=added_files,
             hiddenimports=[],
             hookspath=['./pyinstaller-hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')