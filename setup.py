from setuptools import setup

setup(
    name='guisnake',
    version='0.1.0',
    author='Amir Naseredini',
    author_email='amir.naseredini@canonical.com',
    packages=['guisnake'],
    install_requires=[
        'pygame',
    ],
    entry_points={
        "console_scripts": [
            "guisnake = guisnake.__main__:main"
        ]
    },
)
