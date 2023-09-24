import os
import pkg_resources
import paraty_commit_jlvillada


def main():
    print("hello, this is pre-commit paraty")
    print(os.getcwd())
    package_name = 'paraty_commit_jlvillada'
    package_path = pkg_resources.resource_filename(package_name, '')
    print("Ruta del paquete personalizado:", package_path)

if __name__ == '__main__':
   main()