from setuptools import setup, find_packages

setup(
    name="ft_package_chanwjeo",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],  # 필요한 경우, 이곳에 의존성 패키지들을 나열합니다.
    # 메타데이터
    author="chanwjeo",
    author_email="chanwjeo@student.42seoul.kr",
    description="A sample test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/chanwoong1",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 패키지에 포함되는 데이터 파일을 지정하는 부분 (예: .txt, .md 등의 파일)
    package_data={
        "ft_package": ["*.txt", "*.md"],
    },
)
