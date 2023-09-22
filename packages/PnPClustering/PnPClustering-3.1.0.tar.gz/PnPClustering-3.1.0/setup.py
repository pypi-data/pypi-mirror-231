from setuptools import setup, find_packages

setup(
    name='PnPClustering',
    version='3.1.0',
    description='Push and Pull algorithm for ARC problem implemented by fun._.alone from GIST DSLab',
    author='fun._.alone',
    author_email='limvictor@naver.com',
    url='https://github.com/teddylee777/teddynote',
    install_requires=['tqdm', 'pandas', 'scikit-learn',],
    packages=find_packages(exclude=[]),
    keywords=['fun._.alone', 'GIST', 'ARC', 'abstraction and reasoning corpus', 'DSLab'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3'
    ],
)
