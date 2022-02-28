from setuptools import setup, find_packages

setup(
    name="seawarfare",
    version="0.0.1",
    description="Seawarfare Simulation in Python",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
