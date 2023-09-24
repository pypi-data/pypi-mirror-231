# panda-py

![logo](https://github.com/JeanElsner/panda-py/blob/main/logo.jpg?raw=true)

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/JeanElsner/panda-py/test.yml)](https://github.com/JeanElsner/panda-py/actions/workflows/test.yml)
[![GitHub](https://img.shields.io/github/license/JeanElsner/panda-py)](https://www.apache.org/licenses/LICENSE-2.0)
[![PyPI](https://img.shields.io/pypi/v/panda-python)](https://pypi.org/project/panda-python/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/panda-python)
[![Documentation](https://shields.io/badge/-Documentation-informational)](https://jeanelsner.github.io/panda-py/)

Finally, Python bindings for the Panda. These will increase your productivity by 1000%, guaranteed[^1]!

## Getting started

To get started, check out the [tutorial paper](https://arxiv.org/abs/2307.07633), Jupyter [notebooks](https://github.com/JeanElsner/panda-py/tree/main/examples/notebooks) and other examples you can run directly on your robot. For more details on the API, please refer to the [documentation](https://jeanelsner.github.io/panda-py/).

## Install

```
pip install panda-python
```

This will install panda-py and all its requirements. The pip version ships with libfranka 0.9.2, the newest version for the Franka Emika Robot. Please refer to the section below if you use an older system version or the more recent Franka Research 3 robot. 

## libfranka Version

There are currently two robot models available from Franka Emika: the Franka Emika Robot (FER, formerly known as Panda) and the Franka Research 3 (FR3). Depending on the installed firmware, the FER supports version <=0.9 while the FR3 requires version >=0.10. For details, refer to [this](https://frankaemika.github.io/docs/compatibility.html) compatibility matrix. If you need a libfranka version different from the default 0.9.2, download the respective zip archive from the [release page](https://github.com/JeanElsner/panda-py/releases). Extract the archive and install the wheel for your Python version with pip, e.g., run
```
pip install panda_python-*libfranka.0.7.1-cp310*.whl
```
to install the binary wheel for libfranka 0.7.1 and Python 3.10.

# Citation

If you use panda-py in published research, please consider citing the [tutorial paper](https://arxiv.org/abs/2307.07633).

```
@misc{elsner2023taming,
      title={Taming the Panda with Python: A Powerful Duo for Seamless Robotics Programming and Integration}, 
      author={Jean Elsner},
      year={2023},
      eprint={2307.07633},
      archivePrefix={arXiv},
      primaryClass={cs.RO}
}
```

[^1]: Not actually guaranteed. Based on a sample size of one.
