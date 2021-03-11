import pathlib
import setuptools
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setuptools.setup(
    name="sbnltk",
    version="1.0.4",
    description="Bangla NLP toolkit",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Foysal87/sbnltk",
    author="Towhid Ahmed Foysal",
    author_email="towhidfoysal123@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
'gdown>=3.12.2',
'google_trans_new>=1.1.9',
'pandas>=1.2.2',
'scikit-learn==0.22.2.post1',
'transformers>=4.3.2',
'torch>=1.7.1',
'tensorflow>=2.4.1',
'sklearn_crfsuite>=0.3.6',
'pytorch_pretrained_bert>=0.6.2',
'sentence_transformers'
    ],
)
