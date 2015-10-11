import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtailpress',
    version='0.1',
    packages=['md_cms'],
    include_package_data=True,
    license='BSD License',
    description='wagtailpress is an Django app which extends the Wagtail CMS to be similar to WordPress.',
    long_description=README,
    long_description=open('README.rst', encoding='utf-8').read(),
    url='https://github.com/FlipperPA/wagtailpress',
    author='Timothy Allen',
    author_email='tim@pyphilly.org',
    install_requires=[
        'wagtail>=1.0,<2.0',
        'Markdown==2.6.2',
        'Pygments==2.0.2',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
