from setuptools import setup, find_packages

setup(
    name='blender-rigging-toolkit',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A toolkit for automatically generating rigs for creatures, mechas, and abstract 3D models in Blender.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Add your dependencies here, e.g.:
        # 'bpy',  # Blender Python API
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)