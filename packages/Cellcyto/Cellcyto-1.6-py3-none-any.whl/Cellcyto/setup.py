from distutils.core import setup

setup(
  name='Cellcyto',
  packages=['Cellcyto'],
  version='1.6',
  license='Walsh Lab',
  description='This algorithm is designed for cell segmentation post processing to find nucleus and cytoplasm, and evaluation of the segmentation algorithm based on ground truth images',
  author='Nianchao Wang',
  author_email='nwang27@tamu.edu',
  keywords=['Cell Segmentation', 'POSEA', 'Cytoplasmic Post-processing Algorithm (CPPA)'],
  install_requires=[
      'customtkinter==5.2.0',
      'opencv-python==4.8.0.76',
      'numpy==1.25.2',
      'pillow==10.0.0',
      'pandas==2.1.0',
      'scikit-image==0.21.0',
  ],
  classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: BSD License',
      'Programming Language :: Python :: 3',
  ],
  entry_points={
      'console_scripts': [
          'CellCyto=CellCyto.GUI:run_gui'
      ],
  },
)
