from pip.req import parse_requirements
from setuptools import setup

setup(name='psc_konvertor',
      version='0.1.0',
      description='PSČ Konvertor',
      long_description='',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: Unix',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
      ],
      keywords='psc konvertor',
      url='https://github.com/petrbel/PscKonvertor',
      author='Petr Bělohlávek',
      author_email='me@petrbel.cz',
      license='MIT',
      packages=['psc_konvertor'],
      package_data={
          '': ['*.csv'],
      },
      include_package_data=True,
      zip_safe=False,
      test_suite='psc_konvertor.tests',
      install_requires=[str(ir.req) for ir in parse_requirements('requirements.txt', session='hack')],
)
