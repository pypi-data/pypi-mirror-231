from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Anomaly Segmentation'
LONG_DESCRIPTION = 'A collection of Anomaly Segmentation methods and an interface for easy use.'

setup(
    name="anoseg",
    version=VERSION,
    author="Hendrik Meininger",
    author_email="H.Meininger@outlook.de",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['matplotlib',
                      'numpy',
                      'opencv-python',
                      'pandas',
                      'pillow',
                      'pytorch',
                      'scipy',
                      'scikit-learn',
                      'scikit-image',
                      'torchvision',
                      ],

    keywords=['python', 'anomaly', 'segmentation', 'anomaly segmentation', 'dfc', 'padim', 'spade'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)
