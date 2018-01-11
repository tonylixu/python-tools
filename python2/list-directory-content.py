def list_directory_contents(source_path):
    '''This function takes the name of a directory and prints out
    the paths files within that directory as well as any files contained in
    sub-directories

    This function is a simulation of os.walk.
    '''
    import os
    for item in os.listdir(source_path):
        item_path = os.path.join(source_path, item)
        if os.path.isdir(item_path):
            list_directory_contents(item_path)
        else:
            print item_path

list_directory_contents('/tmp')
