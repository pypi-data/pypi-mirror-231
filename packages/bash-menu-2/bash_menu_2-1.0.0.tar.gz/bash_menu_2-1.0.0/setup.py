from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='bash_menu_2',
    version='1.0.0',
    author='Oleksii.Popov',
    author_email='popovaleksey1991@gmail.com',
    description='Bash Menu Builder',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/OleksiiPopovDev/Bash-Menu',
    packages=['bash_menu_2'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='bash menu vizual python',
    project_urls={
        'Documentation': 'https://github.com/OleksiiPopovDev/Bash-Menu'
    },
    python_requires='>=3.9'
)
