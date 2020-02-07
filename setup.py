import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='xpy',
     version='0.0.1',
     author="Peng Xiong",
     author_email="xiongpengnus@gmail.com",
     description="Exercises for Python coding",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/XiongPengNUS/xpy",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
