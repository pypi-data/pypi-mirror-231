# -*- coding = utf-8 -*-  
# @Time: 2023/9/22 15:25 
# @Author: Dylan 
# @File: setup.py.py 
# @software: PyCharm

from setuptools import setup, find_packages

setup(
    name = "chengsheng_data_tool",
    version = "0.1",
    packages = find_packages(),
    install_requires=[
        "openai",
        "json" 
        "tqdm" 
        "subprocess" 
        "argparse"
    ]
)
