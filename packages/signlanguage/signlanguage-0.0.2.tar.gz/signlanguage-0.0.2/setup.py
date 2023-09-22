from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name="signlanguage",
    version="0.0.2",
    long_description=readme(),
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "pandas",
        "mediapipe",
        "scikit-learn",
        "tensorflow",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows :: Windows 11",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
    ],
    keywords='sign_recognition',
    author="Jose Orlando Wannan Escobar",
    author_email="jwannan13@gmail.com",
    description="Paquete para administracion de la informacion de datos para reconocer señales realizadas con las manos - (model-3)",
    url="https://github.com/JoWan1998/signlanguage",
    license='GPLv3+',
     zip_safe=False
)
