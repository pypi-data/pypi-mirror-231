from setuptools import setup, find_packages
setup(
    name='researchpal',
    packages=find_packages(include=['literature_review', 'literature_review.generate_literature_review']),
    version='0.0.1',
    description='Python library for generating literature review',
    author='Dr.Ali Chaudhry',
    author_email='ali@naseem.education',
    license='MIT',
    keywords=['researchpal', 'literature review', 'generate literature review', 'python literature'],
    install_requires=[
        'arxiv',
        'beautifulsoup4',
        'openai',
        'python-dotenv',
        'Requests',
        'setuptools',
        'setuptools',
        'termcolor',
        'tiktoken',
        ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows"

    ]
)