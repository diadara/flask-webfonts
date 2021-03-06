"""
Flask-Webfonts
--------------

Description goes here...

Links
`````

* `documentation <http://packages.python.org/Flask-Webfonts>`_
* `development version
  <http://github.com/USERNAME/REPOSITORY/zipball/master#egg=Flask-Webfonts-dev>`_

"""
from setuptools import setup, find_packages


setup(
    name='Flask-Webfonts',
    version='0.1',
    url='<enter URL here>',
    license='BSD',
    author='Nithin Saji',
    author_email='your-email-here@example.com',
    description='<enter short description here>',
    long_description=__doc__,
    packages = find_packages(),
    include_package_data=True,
    namespace_packages=['flaskext'],
    zip_safe=False,
    setup_requires=['setuptools-git'],
    platforms='any',
    install_requires=[
        'Flask',"PyYAML"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
