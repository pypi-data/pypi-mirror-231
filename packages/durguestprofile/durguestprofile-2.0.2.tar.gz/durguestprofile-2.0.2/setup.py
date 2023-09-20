from setuptools import setup, find_packages
import os


def read(fname):
    """Utility function to get README.rst into long_description.
    ``long_description`` is what ends up on the PyPI front page.
    """
    with open(os.path.join(os.path.dirname(__file__),fname), encoding="utf8") as f:
        contents = f.read()

    return contents


VERSION = '2.0.2'
DESCRIPTION = 'Dur Guest Data Accuracy Measurement Tool'
LONG_DESCRIPTION = read("README.md")

# Setting up
setup(
    # the name must match the folder name
    name="durguestprofile",
    version=VERSION,
    license='BSD',
    author="ROInsight.com - Muhammad Khlef",
    author_email="<support@roinsight.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.23.5',
        'pandas>=1.5.3',
        'XlsxWriter>=3.0.3',
        "lxml>=4.9.1",
        "pyparsing>=3.0.9",
        "openpyxl>=3.0.10",
        "customtkinter==5.1.2",
        "sparse_dot_topn>=0.3.1",
        "scikit-learn>=1.1.1",
        "scipy>=1.10.0",
        "matplotlib==3.7.1",
        "google-i18n-address==2.5.2",
        "phonenumbers==8.13.8",
        "pysftp==0.2.9"

        # add any additional packages
    ],
    url="",
    keywords=['python', 'dur', 'guest', 'opera', 'profile', 'audit'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Software Development :: Version Control :: Git",
    ]
)


