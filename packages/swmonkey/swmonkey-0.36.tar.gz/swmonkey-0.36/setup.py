from setuptools import setup, find_packages
import os

with open('swmonkey/main.py', encoding='utf-8') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip("'")
            break


def find_pyc_files():
    pyc_files = []
    for root, _, filenames in os.walk('swmonkey'):
        if '__pycache__' in root:
            for filename in filenames:
                if filename.endswith('.pyc'):
                    pyc_path = os.path.join(root, filename)
                    # Replace backslashes with forward slashes for cross-platform compatibility
                    pyc_path = pyc_path.replace('\\', '/')
                    pyc_files.append(pyc_path)
    return pyc_files


print('version: ', version)
setup(
    name='swmonkey',
    version=version,
    packages=find_packages(),
    package_data={
        '': find_pyc_files()  # Include all found .pyc files
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
