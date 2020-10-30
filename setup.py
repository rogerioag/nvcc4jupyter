from distutils.core import setup

setup(
    name='ColabPlugin',
    version='0.0.3',
    author='Andrei Nechaev, M. Canesche',
    author_email='lyfaradey@yahoo.com, michael.canesche@gmail.com',
    py_modules=['nvcc_plugin', 'v2.v2', 'v1.v1', 'c.c', 'cpp.cpp', 'verilog.verilog', 'vhdl.vhdl', 'java.java', 'gem5.gem5', 'valgrind.valgrind', 'common.helper'],
    url='htpps://github.com/rogerioag/nvcc4jupyter',
    license='LICENSE',
    description='Jupyter notebook plugin to run CUDA C/C++, GCC code',
    # long_description=open('README.md').read(),
)
