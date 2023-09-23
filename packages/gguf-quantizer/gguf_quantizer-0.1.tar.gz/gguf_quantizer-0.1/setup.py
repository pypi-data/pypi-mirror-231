from setuptools import setup, find_packages

setup(
   name="gguf_quantizer",
    version="0.1",
    author="Kirouane Ayoub",
    author_email="ayoubkirouane3@email.com",
    description="A Python package for LLAMA gguf quantization",
    packages=find_packages(),
    install_requires=[
        # Add any required dependencies here
    ],
    entry_points={
        'console_scripts': [
            'llama-quantize=llama_quantizer.quantization:main'
        ],
    },
)
