from setuptools import setup, find_packages

setup(
    name='django-restauth-boilerplate',
    version='0.1',
    packages=find_packages(),
    include_package_data==True,
    install_requires=[
        'Django>=3.2',
        'djangorestframework',
        'dj-rest-auth',
        'djangorestframework-simplejwt>=5.0',
        'django-allauth',
    ],
    description='A Reusable Django app with REST Auth and Google Login as API endpoints',
    author='Farid Seidu',
    author_email='seidufarid206@gmail.com',
    url='https://github.com/Versedcamel153/django-restauth-boilerplate',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
)