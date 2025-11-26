

from setuptools import setup, find_packages

setup(
    name="supermath666",  # 对外我们模块的名字
    version="1.0",  # 版本号
    description="这是第一个对外发布的模块,测试哦",  # 描述
    author="w66",  # 作者
    author_email="1065092736@qq.com",
    long_description=open("README.md", encoding="utf-8").read(),  # 从 README 读取详细描述
    long_description_content_type="text/markdown",  # 说明 README 是 Markdown 格式
    url="你的项目地址（比如 GitHub 链接）",
    packages=find_packages(),  # 自动找到所有包（比如 mypackage）
    classifiers=[  # 分类标签（帮助别人在 PyPI 上搜到你的包）
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # 支持的 Python 版本
    install_requires=[  # 你的包依赖的其他包（比如需要 requests 就写进去）
        # "requests >= 2.25.0",
    ]
)