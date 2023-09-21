# setup.py
from setuptools import setup, find_packages

with open('README.md', encoding="utf8") as f:
    # strip the header and badges etc
    readme = f.read().split('--------------------')[-1]

if __name__ == '__main__':
    setup(
        name='trustlib',
        version="0.0.1",
        author="LibrAI",
        description='Unified framework for assessing and improving performance, safety, and reliability.',
        long_description=readme,
        long_description_content_type='text/markdown',
        url='https://github.com/Libr-AI',
        python_requires='>=3.7',
        packages=find_packages(),
        install_requires=[],
        include_package_data=True,
        package_data={'': ['*.txt', '*.md', '*.opt']},
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Natural Language :: English",
        ],
    )