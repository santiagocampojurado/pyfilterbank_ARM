# -- coding: utf-8 --

from setuptools import setup, Extension

module_sosfilt = Extension(
    name="pyfilterbank.sosfilt",
    sources=["pyfilterbank/sosfilt.c"]
)

settings = {
    'name': 'pyfilterbank',
    ######
    'version': '0.0.1', # from 0.0.0
    ######
    'description': 'Filterbanks and filtering for the acoustician and audiologists in python.',
    'url': 'http://github.com/SiggiGue/pyfilterbank',
    'author': u'Siegfried Gündert',
    'author_email': 'siefried.guendert@gmail.com',
    'license': 'MIT',
    'packages': ['pyfilterbank'],
    'zip_safe': False,

    'package_data': {
        'pyfilterbank': [
            'sosfilt.c',
            # 'sosfilt64.dll',
            # 'sosfilt32.dll',
            # 'sosfilt.so'
        ]
    },
    # extension to setuptools so it will compile it
    'ext_modules': [module_sosfilt],
}
setup(**settings)
