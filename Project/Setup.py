import os
import cx_Freeze

os.environ['TCL_LIBRARY'] = 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tk8.6'
executables = [cx_Freeze.Executable(script='Main.py')]

cx_Freeze.setup(
    name='Drop Da Beat!',
    version = '1.1',
    options={'build_exe': {'packages':['pico2d', 'sdl2'],
                           'include_files':['./Resources/','./SDL2/' ]}},
    executables = executables
)