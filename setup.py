from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="face-recognition-attendance",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A real-time face recognition attendance system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/face-recognition-attendance",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "face-attendance=attendance_system:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.md"],
    },
    keywords="face-recognition attendance opencv python computer-vision",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/face-recognition-attendance/issues",
        "Source": "https://github.com/yourusername/face-recognition-attendance",
        "Documentation": "https://github.com/yourusername/face-recognition-attendance#readme",
    },
)