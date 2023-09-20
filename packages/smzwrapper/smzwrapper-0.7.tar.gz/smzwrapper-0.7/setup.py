from distutils.core import setup
setup(
  name = 'smzwrapper',
  packages = ['smzwrapper'],
  version = '0.7',
  license='MIT',
  description = 'For data decode',
  author = 'Ra',
  author_email = 'polar.skee@rambler.ua',
  url = 'https://github.com/Arctic-Ra/smzwrapper/',
  download_url = 'https://github.com/Arctic-Ra/smzwrapper/archive/refs/tags/v0.7.tar.gz',
  keywords = ['decode', 'data', 'smz'],
  install_requires=[ 'colorama', ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)