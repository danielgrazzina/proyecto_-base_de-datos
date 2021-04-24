# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['index_modulos.py'],
             pathex=['C:\\Users\\RicardoGlod\\Desktop\\AppPyhtonDB'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [("inventario.db", "./inventario.db", "DATA"), ("archivo.ico", "archivo.ico", "DATA"), 
("principal.png", "./principal.png", "DATA"), ("cliente.png", "cliente.png", "DATA"), ("pedidos.png", "./pedidos.png", "DATA"),
("buscar.png", "./buscar.png", "DATA"), ("sumar_inventario.png", "./sumar_inventario.png", "DATA"), 
("restar_inventario.png", "./restar_inventario.png", "DATA"), ("actualizar_tree.png", "./actualizar_tree.png", "DATA"), 
("abono_deuda.png", "./abono_deuda.png", "DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='index_modulos',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='archivo.ico')
