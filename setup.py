import setuptools
import platform

with open("README.md", "r") as fh:
    long_description = fh.read()
    
_platforms = {
        "64": {
                "Darwin": "osx64",
                "Linux": "linux64",
                "Windows": "win64"
                },
        "32": {
                "Windows": "win32"
                }
        }

try:
    _platform = _platforms[platform.architecture()[0][:2]][platform.system()]
except KeyError:
    raise RuntimeError('Platform not supported.')

# Include tkdnd extension files.
package_data = {"tkinterdnd2": [f"tkdnd/{_platform}/*.*"]}

setuptools.setup(
    name="tkinterdnd2",
    version="0.3.0",
    author="petasis\\pmgagne\\eliav2",
    description="TkinterDnD2 is a python wrapper for George Petasis'' tkDnD Tk extension version 2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eliav2/tkinterdnd2",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data=package_data,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)