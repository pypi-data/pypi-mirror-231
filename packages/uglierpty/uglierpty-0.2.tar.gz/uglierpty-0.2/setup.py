from setuptools import setup, find_packages

setup(
    name='uglierpty',
    version='0.2',
    description="UglierPTY a POC for SSH UI in PyQt6",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Scott Peterman",
    author_email="scottpeterman@gmail.com",
    url="https://github.com/scottpeterman/UglierPTY",  # Replace with your repository URL
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=[
        'PyQt6',
        'pyte',
        'paramiko'
        # Add any other dependencies you need
    ],
    entry_points={
        'console_scripts': [
            'uglierpty = uglierpty.UglierPTY:main',
        ],
    },
)
