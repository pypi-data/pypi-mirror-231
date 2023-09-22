from setuptools import setup, find_packages
import os

scriptFolder = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptFolder)

version = '0.45'

print('version: ', version)
setup(
    name='swmonkey',
    version=version,
    packages=find_packages(),
    package_data={
        'swmonkey': ['pyarmor_runtime_000000/*.so'],
    },
    author='Li Saifei',
    author_email='waltermitty121906@gmail.com',
    description='A tool for monkey test on Linux GUI',
    entry_points={
        'console_scripts': [
            'swmonkey = swmonkey.main:swmonkey',
            'swmonkey_runner = swmonkey.runner:main'
        ]
    },
    install_requires=[
        'pyautogui',
        'psutil',
        'pywinctl'
    ]
)
