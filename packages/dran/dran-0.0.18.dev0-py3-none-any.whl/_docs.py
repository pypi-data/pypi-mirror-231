# =========================================================================== #
# File    : _docs.py                                              #
# Author  : Pfesesani V. van Zyl                                              #
# =========================================================================== #

# Standard library imports
# --------------------------------------------------------------------------- #
import webbrowser
import os, sys
# --------------------------------------------------------------------------- #

import importlib.resources as resources

def main():
    """ 
    Open the source documentation.
    """
    
    # set path to docs
    dir_path = os.path.dirname(os.path.realpath(__file__))
    x=os.path.join(dir_path,'docs/dran-build/index.html')

    print("Opening docs")
    print(resources.contents('docs'))
   
    # with resources.path('docs', "index.html") as p:
    #     package_path = p
    # print(package_path)
    
    sys.exit()
    webbrowser.open_new_tab('file://' + x)
    print('done')


if __name__ == "__main__":
    main()