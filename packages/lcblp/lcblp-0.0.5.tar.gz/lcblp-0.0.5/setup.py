from setuptools import setup, find_packages

setup(
    name='lcblp',
    version='0.0.5',
    description='LPLP',
    author='LCB',
    author_email='lcvrjqnr@gmail.com',
    url='https://github.com/halfTaim/lcblp.git',
    install_requires=['tqdm', 'pandas', 'scikit-learn',],
    packages=find_packages(exclude=[]),
    keywords=['lcblp', 'lcb'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)