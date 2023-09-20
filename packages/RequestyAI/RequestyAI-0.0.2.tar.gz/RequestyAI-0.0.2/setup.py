from setuptools import setup

setup(
    name='RequestyAI',
    version='0.0.2',
    author='Thibault Jaigu',
    author_email='thibault@requesty.ai',
    description='Requesty Python Library',
    py_modules=["requestyai"],
    package_dir={'': 'src'},
    long_description='Python library to integrate with Requesty',
    url='https://docs.requesty.ai/guides/Integration/Python',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
