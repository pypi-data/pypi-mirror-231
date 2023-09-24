import os
import pkg_resources
import paraty_commit_jlvillada
import shutil

def main():
    print("hello, this is pre-commit paraty")
    project_path = os.getcwd()
    package_name = 'paraty_commit_jlvillada'
    package_path = pkg_resources.resource_filename(package_name, '')

    files = os.listdir(package_path)
    files = [file for file in files if os.path.isfile(os.path.join(package_path, file))]

    print("project_path: %s", project_path)

    for file in files:
        file_name_path = os.path.join(package_path, file)
        file_name_project_path = os.path.join(project_path, file)
        print("file: %s", file_name_path)
        print("file: %s", file_name_project_path)
        shutil.copy(file_name_path, file_name_project_path)

    print("Ruta del paquete personalizado:", package_path)

if __name__ == '__main__':
   main()