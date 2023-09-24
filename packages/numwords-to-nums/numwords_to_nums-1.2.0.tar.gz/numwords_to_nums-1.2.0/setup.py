from setuptools import find_packages, setup
setup(
    name='numwords_to_nums',
    packages=find_packages(include=['numwords_to_nums']),
    version='1.2.0',
    description='Python library for converting numerical words (textual numbers) to numbers',
    long_description="README.md",
    long_description_content_type="text/markdown",
    author='Sarthak, Arpit',
    author_email="sarthak6jan16@gmail.com , joshia296@gmail.com",
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
