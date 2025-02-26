from setuptools import setup
from io import open

setup(
    name='textstat_logistic',
    packages=['textstat_logistic'],
    version='0.7.31',
    description='Calculate statistical features from text. Modify the dale_chall_readability_score and use the logitstic function.',
    author='Hao Li',
    author_email='LiHao.0712@outlook.com',
    url='https://github.com/ZhiXingHeYi-0712/textstat-logistic',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    package_data={'': ['easy_word_list'], '': ['*.txt']},
    include_package_data=True,
    install_requires=['pyphen', 'nltk'],
    license='MIT',
    python_requires=">=3.6",
    classifiers=(
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing",
        ),
)
