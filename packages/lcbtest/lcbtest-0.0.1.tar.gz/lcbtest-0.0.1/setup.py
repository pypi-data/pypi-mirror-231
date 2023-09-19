from setuptools import setup, find_packages

setup(
    name='lcbtest',
    version='0.0.1',
    description='LP',
    author='LCB',
    author_email='lcvrjqnr@gmail.com',
    url='https://github.com/halfTaim/lcbtest.git',
    install_requires=['tqdm', 'pandas', 'scikit-learn',],
    packages=find_packages(exclude=[]),
    keywords=['lcbtest', 'lcb'],
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