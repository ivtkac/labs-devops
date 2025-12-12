from setuptools import setup, find_packages
import os

requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
requires = []
with open(requirements_path, "r") as f:
    requires = [line.strip() for line in f if line.strip() and not line.startswith("#")]


setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={"console_scripts": ["snapshot = snapshot.snapshot:main"]},
    install_requires=requires,
    version="0.1",
    author="Ivan Tkachuk",
    author_email="ivktac@gmail.com",
    description="Monitor your system/server",
    license="MIT",
)
