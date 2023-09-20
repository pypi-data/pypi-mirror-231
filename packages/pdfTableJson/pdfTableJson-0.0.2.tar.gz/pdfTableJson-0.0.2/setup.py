from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pdfTableJson',
    version='0.0.2',
    license = 'GNU AFFERO GPL 3.0',
    description='PDF Table to JSON',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='hielosan',
    author_email='hielosan@naver.com',
    url='https://github.com/yousojeong/pdfTableJson/',
    project_urls={
        "Bug Tracker": "https://github.com/yousojeong/pdfTableJson/issues",
    },
    install_requires=[
        'opencv-python',
        'numpy',
        'PyMuPDF',
        'pdfTableJson',
    ],
    packages=find_packages(exclude=[]),
    keywords=['pdf', 'table', 'json', 'converter', 'cv', 'openCV'],
    python_requires='>=3.8',
    package_data={},
    zip_safe=True,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    ],
)
