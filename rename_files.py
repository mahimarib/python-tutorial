import os


def rename_files():
    file_list = os.listdir(r"C:\Users\Home\Desktop\100D3200")
    current_path = os.getcwd()
    print(current_path)
    os.chdir(r"C:\Users\Home\Desktop\100D3200")
    for file_name in file_list:
        print('current file name: %s | new name: %s' %
              (file_name, file_name.replace('DSC', 'IMG')))
        os.rename(file_name, file_name.replace('DSC', 'IMG'))


rename_files()
