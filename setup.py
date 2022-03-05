from setuptools import find_packages, setup

setup(
    name="seawarfare",
    version="0.0.1",
    description="Seawarfare Simulation in Python",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points="""
    [console_scripts]
    seawarfare=seawarfare.main:main
    """,
)
