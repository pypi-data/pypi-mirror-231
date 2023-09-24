from setuptools import setup, find_packages

setup(
    name='idli_coco',
    version='2.1.0',
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
)