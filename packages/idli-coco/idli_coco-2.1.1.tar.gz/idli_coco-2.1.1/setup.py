from setuptools import setup, find_packages
# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='idli_coco',
    version='2.1.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'idli_coco': ['idli_coco.jpg'],
    },
    install_requires=[
        'streamlit',
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'idli_coco = idli_coco.main:run',
        ],
    },
    # new arguments
    long_description=long_description,
    long_description_content_type='text/markdown',
)