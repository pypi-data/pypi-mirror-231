from setuptools import setup, find_packages

str_version = '1.0.0'

setup(name='StableDNAm',
      version=str_version,
      description='DNA Methylation Prediction Model',
      url='https://github.com/wrab12/StableDNAm',
      author='wrab12',
      author_email='wangrui66677@gmail.com',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      install_requires= ['pytorch'],
      python_requires='>=3')

