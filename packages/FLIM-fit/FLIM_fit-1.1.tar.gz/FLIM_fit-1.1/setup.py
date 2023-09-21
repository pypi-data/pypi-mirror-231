from distutils.core import setup

setup(
  name='FLIM_fit',
  packages=['FLIM_fit'],
  version='1.1',
  license='Walsh Lab',
  description='This GUI performs fluorescence lifetime decay analysis at cellular level.',
  author='Linghao Hu',
  author_email='hulinghao@tamu.edu',
  keywords=['Fluorescence Lifetime', 'Decay Analysis', 'Cell-Level'],
  install_requires=[
      'customtkinter',
      'numpy',
      'pandas',
      'scikit-learn',
      'CTkMessagebox',
      'scipy',
      'matplotlib',
      'tifffile',
      'tensorflow',
      'openpyxl'
  ],
  classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: BSD License',
      'Programming Language :: Python :: 3',
  ],
  package_data={
      'FLIM_fit': ['FLIM_fit/*.h5'],
      },
  entry_points={
      'console_scripts': [
          'flimfit=FLIM_fit.GUI:run_gui',
      ],
  },
)
