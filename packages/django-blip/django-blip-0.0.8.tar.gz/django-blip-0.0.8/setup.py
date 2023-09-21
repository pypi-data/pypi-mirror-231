import os
import setuptools

# Get the directory of the current Python script
current_script_directory = os.path.dirname(os.path.abspath(__file__))

# Create the desired path by going up one directory and appending "README.md"
readme_path = os.path.join(os.path.dirname(current_script_directory), "README.md")

setuptools.setup(
    name="django-blip",
    version="0.0.8",
    description="Python package to intercept all external api call during django test.",
    long_description=readme_path,
    long_description_content_type="text/markdown",
    author="Abhinav Prakash",
    author_email="abhinavsp0730@gmail.com",
    license="MIT License",
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    zip_safe=False,
    url="https://github.com/abhinavsp0730/blip/",
    install_requires=["httpretty>=1.1.4"],
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
