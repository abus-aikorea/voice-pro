import argparse
import os
import sys
import shutil
from pathlib import Path
from one_click import *


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python start-abus.py <app_name>")
        sys.exit(1)

    OneClick.oc_check_env()

    app_name = sys.argv[1]
    print(f"app_name: {app_name}")
    
    is_update = True if len(sys.argv) == 3 and sys.argv[2] == '--update' else False
    is_installed = OneClick.oc_is_installed()

           
    # check start-appname.py    
    python_filename = f'start-{app_name}.py'
    if not os.path.exists(python_filename):
        print(f"File not found - {python_filename}")
        sys.exit(1)
             
   
    
    if not is_installed:
        OneClick.oc_install_webui(app_name, False)   
        # oc_install_extra_packages(app_name)
    elif is_update:
        OneClick.oc_install_webui(app_name, True)   
        # oc_install_extra_packages(app_name)
                

    # ABUS - start 
    if not is_update:
        print("Start the program...")
        OneClick.oc_run_cmd(f"python {python_filename}", environment=True) 
    
