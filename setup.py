from setuptools import setup, find_packages

setup(
    name="sample_project",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Dependências do projeto vão aqui
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    python_requires=">=3.8",
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    description="Um projeto Python de exemplo",
)
