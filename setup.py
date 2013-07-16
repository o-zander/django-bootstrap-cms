import bootstrap
from setuptools import setup, find_packages

CLASSIFIERS = [

]

setup(
    author = 'Oliver Zander',
    author_email = 'oliver.zander@gmail.com',
    name = 'django-bootstrap-cms',
    version = bootstrap.__version__,
    description = 'django-bootstrap-cms brings the bootstrap framework from twitter to the django-cms from divio.',
    packages = find_packages(),
    package_data = {'': ['*.html', '*.css', '*.js', '*.png']},
    include_package_data=True,
    zip_safe=False,
    install_requires = [
        'Pillow>=2.0',
        'django-filer>=0.9',
    ],
    url=r'https://github.com/o-zander/django-bootstrap-cms',
    classifiers=CLASSIFIERS
)