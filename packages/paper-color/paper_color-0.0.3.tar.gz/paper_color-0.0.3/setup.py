import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="paper_color",
  version="0.0.3",
  author="Yang Liu",
  author_email="lauyon@tju.edu.cn",
  description="Get colors easily",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/nlply",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)