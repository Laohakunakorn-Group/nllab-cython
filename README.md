# nllab-cython
Example of cythonizing python code

### Installation (local)

Make sure you have a working local python distribution. Install ```pipenv``` using the command ```pip install pipenv```. Navigate to your repository, and run ```pipenv install``` to build the environment, followed by ```pipenv shell``` to activate it.

### Solving the python model

Run ```python3 solve_python.py```.

### Solving the cython model

Navigate to ```./models/cython/``` and compile the cython code by running

	python3 setup.py build_ext --inplace

Then, in the main directory, run ```python3 solve_cython.py```.


