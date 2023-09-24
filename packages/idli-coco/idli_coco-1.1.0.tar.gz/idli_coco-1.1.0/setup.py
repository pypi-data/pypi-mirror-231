from setuptools import setup, find_packages

setup(
    name='idli_coco',
    version='1.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit',
    ],
    entry_points={
        'console_scripts': [
            'idli_coco = idli_coco.main:run',
        ],
    },
)