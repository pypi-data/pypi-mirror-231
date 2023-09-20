from setuptools import setup

setup(
    name="niva_package",
    version="0.4",
    packages=["niva"],
    python_requires=">=3.6",  # Python sürümünü belirtin
    install_requires=[
        "opencv-python",  # eksik veya yanlış bağımlılığı düzeltin
    ],
    entry_points={
        "console_scripts": [
            "niva = niva.niva:main",
        ],
    },
)

