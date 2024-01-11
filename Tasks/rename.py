import os


def renamer(path=r"C:\Users\herrd\Desktop\example_folder"):
    os.chdir(path)
    print('Files in directory:')
    for i in os.listdir():
        print(i)
    extension = input('Enter the extension to rename: ')
    user_name = input('Enter the new name: ')
    l_dir = os.listdir()
    for i in range(len(l_dir)):
        if l_dir[i].endswith(extension):
            old_name = os.getcwd() + "\\" + l_dir[i]
            new_name = os.getcwd() + "\\" + user_name + f"_{i+1}" + extension
            os.rename(old_name, new_name)


renamer()