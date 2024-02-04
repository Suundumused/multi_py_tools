def get_current_directory(args: tuple=()):
    if getattr(sys, 'frozen', False):
        path = os.path.dirname(sys.executable)#get if running as executable (PyInstaller) or any for end user...
    else:
        path = os.path.dirname(os.path.abspath(sys.argv[0]))#else if Running as .py script.
    
    if args:
        return os.path.join(path, *args)
    else:
        return path
    
    
if __name__ == "__main__":
    import os
    import sys
        
    #test any func...
    
    print(get_current_directory(('some_folder', 'text.txt')))
