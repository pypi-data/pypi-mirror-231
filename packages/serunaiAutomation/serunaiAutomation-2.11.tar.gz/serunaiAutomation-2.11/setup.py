from setuptools import setup

setup(
    name='serunaiAutomation',
    version='2.11',
    description='Automation Framework for Seamless Testing and Data Extraction',
    long_description="This is an automation framework for automating test cases and also would be useful for web scrapping.",
    long_description_content_type="text/x-rst",
    author='Maimul',
    author_email='maimulskates@gmail.com',
    packages=['serunaiAutomation'],
    install_requires=['selenium', 'seleniumbase', 'openpyxl', 'hashlib', 'json', 'csv', 'datetime', 'time', 'random'],
    py_modules=['serunaiAutomation.serunaiAutomate'],
    entry_points={
        'console_scripts': [
            'serunaiAutomation = serunaiAutomation.serunaiAutomate:main',
        ],
    },
)
