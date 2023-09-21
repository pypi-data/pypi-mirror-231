from setuptools import setup, find_packages
setup(
    name='jaguardb',
    version='3.3.6',
    author = 'Jonathan Yue',
    description = 'Python3 client for Jaguar vector database',
    url = 'http://www.jaguardb.com',
    license = 'Apache 2.0',
    python_requires = '>=3.0',
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        ('shared_library', ['shared_library/libJaguarClient.so', 'shared_library/jaguarpy.so']),
        ('jaguar_example', ['example/test.sh', 'example/vector_similarity.py', 'example/README.md']),
    ],
)
