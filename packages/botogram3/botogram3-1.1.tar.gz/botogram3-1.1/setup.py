from setuptools import setup, find_packages

setup(
    name='botogram3',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'aiogram==3.0.0b4',
        'python-dotenv>=1.0.0',
    ],

    entry_points={
        'console_scripts': [
            'init-bot-project=init_bot_project:main',
        ],
    },

    author='Abraham',
    author_email='abraha111.07@gmail.com',
    description='Botogram is a framework for AIOGRAM3',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
