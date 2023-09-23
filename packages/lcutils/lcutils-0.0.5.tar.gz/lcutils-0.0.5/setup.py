from setuptools import setup, find_packages

setup(
    name='lcutils',  # 包的名称
    version='0.0.5',  # 包的版本号
    author='lcqbug',  # 作者姓名
    description='some useful python utils',  # 包的描述信息
    packages=find_packages(),  # 包含的子包列表
    install_requires=[  # 依赖项列表
        'faker',
        'requests',
    ],
)
