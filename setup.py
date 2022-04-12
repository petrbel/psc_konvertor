try: # for pip >= 10
      from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
      from pip.req import parse_requirements

from setuptools import setup

install_reqs = list(parse_requirements('requirements.txt', session='hack'))
try:
      requirements = [str(ir.req) for ir in install_reqs]
except:
      requirements = [str(ir.requirement) for ir in install_reqs]

setup(name='psc_konvertor',
      version='0.3.0',
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
      packages=['psc_konvertor',
                'psc_konvertor.data'],
      package_data={
          # If any package contains *.txt or *.rst files, include them:
          '': ['*.csv'],
      },
      include_package_data=True,
      zip_safe=False,
      test_suite='psc_konvertor.tests',
      install_requires=requirements,
)
