
from setuptools import setup
from setuptools.command.install import install

# Define una función que se ejecutará durante la instalación
class custom_install_code(install):
    def run(self):
        print("Here is where I would be running my code...")
        install.run(self)

    def _post_install():
        print("Here is where I would be running my code post install...")

setup(
    name='paraty_commit_jlvillada',
    version='0.1.3',
    description='Una biblioteca personalizada',
    author='José Luis Villada',
    author_email='jlvillada@paratytech.com',
    cmdclass={
        'install': custom_install_code
      },
    packages=[],
    install_requires=[
        # Dependencias requeridas aquí
    ]
)