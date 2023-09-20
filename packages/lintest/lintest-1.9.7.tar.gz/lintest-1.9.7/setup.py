from setuptools import setup

setup(
    name='lintest',
    version='1.9.7',
    author='Wang Lin',
    author_email='think_wl@163.com',
    packages=['lintest'],
    install_requires=[
        "psutil",
        "requests",
        "curlify",
        "selenium",
        "selenium-wire",
        "setuptools",
        "urllib3",
        "PyMySQL",
        "jsoncomparison",
        "chromedriver_autoinstaller"
    ],
)
