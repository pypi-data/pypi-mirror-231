from distutils.core import setup, Extension
setup(
    name="andiDB", 
    version="1.0.0",

    url='https://github.com/AndreasScharf/andiDBClientC',
    author='Andreas Scharf',
    author_email='info@frappgmbh.de',
    license='MIT',
    ext_modules=[
          Extension(
          	"andiDB", 
          	["./src/andiDBValue.c", "./src/andiDBClient.c"], 
          	include_dirs=['./src'],
          )] 
          )
