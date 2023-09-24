from setuptools import setup


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(name='jsthon',
      version='0.4.1',
      author='terribleMOTHMAN',
      description='Easy to use, fast, productive json database for python',
      long_description=readme(),
      long_description_content_type='text/markdown',
      packages=['jsthon'],
      licence='MIT License',
      install_requires=['uuid>=1.30', 'ujson>=5.6.0'],
      author_email='paradox.smirnoff@gmail.com',
      url="https://github.com/terribleMOTHMAN/JsthonDb",
      zip_safe=False)