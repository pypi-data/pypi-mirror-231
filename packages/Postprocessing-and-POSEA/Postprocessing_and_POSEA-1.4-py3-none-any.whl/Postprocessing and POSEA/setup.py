from distutils.core import setup
setup(
  name = 'Postprocessing and POSEA',
  packages = ['Postprocessing and POSEA'],
  version = '1.0',
  license='Walsh Lab',
  description = 'This algorithm is designed for cell segmentation post processing to find nucleus and cytoplasm, and evaluation of the segmentation algorithm based on ground truth images',
  author = 'Nianchao Wang',
  author_email = 'nwang27@tamu.edu',
  keywords = ['Cell Segmentation', 'POSEA', 'Post-processing'],
  install_requires=[
          'tkinter',
          'customtkinter',
          'os',
          'cv2',
          'numpy',
          'PIL',
          'math',
          'pandas',
          'skimage',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3',
  ],
)