
from setuptools import setup

# Define una función que se ejecutará durante la instalación
def custom_install_code():
    print("Ejecutando código personalizado durante la instalación.")

setup(
    name='paraty_commit_jlvillada',
    version='0.1.0',
    description='Una biblioteca personalizada',
    author='José Luis Villada',
    author_email='jlvillada@paratytech.com',
    packages=[],
    install_requires=[
        # Dependencias requeridas aquí
    ]
)