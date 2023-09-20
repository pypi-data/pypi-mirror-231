from setuptools import find_packages, setup
#python setup.py bdist_wheel
#https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f
setup(
    name='yuno_sesr',
    packages=find_packages(include=['yuno_sesr']),
    version='0.0.1',
    description='Test upload to pypi',
    author='yunotao',
    license='MIT',
    package_data={'yuno_sesr': ['test.txt','SESR_m5_FP32/*.*','SESR_m5_FP32/assets', 'SESR_m5_FP32/variables/*.*'],
                 
    },
    include_package_data=True,
    install_requires=[],
)


