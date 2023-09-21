# JaguarDB client

The package is for development of AI applications using Jaguar vector database
in Python3 environment.

1.  To use language transformer models, please install:

    pip install -U sentence-transformers


2. When you start a Python program, make sure these two environment variables 
   are set correctly so that they include libJaguarClient.so and jaguarpy.so:

    #!/bin/sh

    export PYTHONPATH=/path/to/shared_library
    export LD_LIBRARY_PATH=/path/to/shared_library

    python3 vector_similarity.py  127.0.0.1 8888


    For example:
    export PYTHONPATH=$HOME/.local/shared_library
    export LD_LIBRARY_PATH=$HOME/.local/shared_library



3. For more information, please visit:

   https://github.com/fserv/jaguar-sdk


