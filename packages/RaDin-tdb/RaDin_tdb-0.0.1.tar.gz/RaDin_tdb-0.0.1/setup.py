from setuptools import setup


# Setting up
setup(
    name="RaDin_tdb",
    version="0.0.1",
    author="Abuzar",
    author_email="radinofficial15@gmail.com",
    description="It's a School's Database Trial Manipulator, That is written by Abuzar Alvi.",
    long_description_content_type="text/markdown",
    long_description="It's a School's Database Trial Manipulator, That is written by Abuzar Alvi. They can perform many tasks like insert, check, update, delete, add, sub or many more things.",
    packages=['Trial_Manipulator'],
    install_requires=[''],
    keywords=['school', 'database', 'school database','arithmetic', 'mathematics', 'python', 'RaDin', 'RaDin database', 'database modifier'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)


# python setup.py sdist bdist_wheel
# python -m twine upload dist/*