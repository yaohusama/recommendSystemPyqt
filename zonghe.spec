# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['zonghe.py'],
             pathex=['xingce/mygui.py', 'xingce/neo4j.py', 'xingce/recom.py', 'xingce/recom_view.py', 'shenlun/mygui.py', 'shenlun/neo4j.py', 'shenlun/recom.py', 'shenlun/recom_view.py'],
             binaries=[],
             datas=[],
             hiddenimports=['xingce.mygui', 'xingce.neo4j', 'xingce.recom', 'xingce.recom_view', 'shenlun.mygui', 'shenlun.neo4j', 'shenlun.recom', 'shenlun.recom_view', 'mygui', 'neo4j', 'recom', 'recom_view', 'xingce', 'shenlun'],
             hookspath=[],
             hooksconfig={},
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
          [],
          exclude_binaries=True,
          name='zonghe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='zonghe')
