"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/

"""
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

# Always prefer setuptools over distutils
import setuptools

keywords = [ "google_scraper", 'news_scraper', 'bs4',
'news-extractor', 'crawler', 'extractor', 'news', 'elasticsearch', 'json', 'python', 'nlp', 'data-gathering',
'news-archive', 'news-articles', 'commoncrawl', 'extract-articles', 'extract-information', 'news-scraper', 'spacy','pytorch','torch','tensorflow','machine learning','question answering','research']

setuptools.setup(
    name="instant-expert",
    version="0.1.4",
    author="Sean Bailey",
    author_email="seanbailey518@gmail.com",
    description="newsripper provides a simple python library which scrapes relevant keyword information from news sites using search engines",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sean-bailey/instant-expert",
    keywords = keywords,
    install_requires=['torch', 'transformers', 'pdfplumber', 'textract',
                      'newsRipper2 @ git+ssh://git@github.com/sean-bailey/newsripper2.git','wrapt_timeout_decorator'],

    packages = setuptools.find_packages(),
    classifiers=['Development Status :: 4 - Beta',
              'Intended Audience :: End Users/Desktop',
              'Intended Audience :: Developers',
              'Intended Audience :: System Administrators',
              'License :: OSI Approved :: GNU AFFERO GENERAL PUBLIC LICENSE V3',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Topic :: Communications :: Email',
              'Topic :: Office/Business',
              'Topic :: Software Development :: Bug Tracking',
              ],
)
