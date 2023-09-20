from distutils.core import setup

setup(
  name='Cellcyto',
  packages=['Cellcyto'],
  version='1.8',
  license='Walsh Lab',
  description='This algorithm is designed for cell segmentation post processing to find nucleus and cytoplasm, and evaluation of the segmentation algorithm based on ground truth images',
  author='Nianchao Wang',
  author_email='nwang27@tamu.edu',
  keywords=['Cell Segmentation', 'POSEA', 'Cytoplasmic Post-processing Algorithm (CPPA)'],
  install_requires=[
      'customtkinter',
      'opencv-python',
      'numpy',
      'pillow',
      'pandas',
      'scikit-image',
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
          'Cellcyto=Cellcyto.GUI:run_gui',
      ],
  },
)
