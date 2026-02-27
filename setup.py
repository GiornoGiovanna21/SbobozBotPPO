from setuptools import setup, find_packages

setup(
    name="sboboz",
    version="0.1.0",
    description="Reinforcement Learning Agent for Sboboz Game",
    author="Your Name",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "gymnasium>=0.29.1",
        "stable-baselines3[extra]>=2.2.1",
        "numpy>=1.24.0",
        "torch>=2.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ]
    },
)
