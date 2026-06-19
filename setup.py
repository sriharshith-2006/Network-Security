from setuptools import setup,find_packages
from typing import List
req_list:List[str]=[]
def req()->List[str]:
    try:
        with open('requirements.txt','r') as f:
            lines=f.readlines()
            for line in lines:
                req=line.strip()
                if req and req!='-e .':
                    req_list.append(req)
    except FileNotFoundError:
        print("File Not Found")
    return req_list
setup(
    name="Networksecurity",
    version="0.0.1",
    author='sriharshith',
    packages=find_packages(),
    install_requires=req(),
)