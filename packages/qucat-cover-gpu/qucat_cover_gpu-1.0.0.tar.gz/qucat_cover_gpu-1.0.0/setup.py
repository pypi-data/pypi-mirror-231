import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="qucat_cover_gpu",
    version="1.0.0",
    author="Xinyi Wang",
    author_email="xinyi@simula.no",
    description="QuCAT: A Combinatorial Testing Tool for Quantum Software",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/Simula-COMPLEX/qucat-tool/",
    classifiers= ["Programming Language :: Python :: 3",  # 编程语言
        "License :: OSI Approved :: MIT License",  # license
        "Operating System :: OS Independent"],  # 操作系统
    install_requires=[
        "qiskit",
        "qiskit-aer-gpu"
    ],
    package_data={"pipmodule": ["*.png", ]},
    python_requires=">=3.7",
    entry_points={
        'console_scripts': [
            'qucat = qucat:help'
 ]
    }
)