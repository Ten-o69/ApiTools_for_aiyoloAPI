from setuptools import setup, find_packages

# Чтение зависимостей из файла requirements.txt
with open('requirements.txt') as f:
    dependencies = f.read().splitlines()

setup(
    name='ApiTools_for_aiyoloAPI',
    version='0.2',
    packages=find_packages(),
    install_requires=dependencies,
    author='Your Name',
    author_email='your@email.com',
    description='Description of your library',
    url='https://github.com/yourusername/yourrepository',
)
