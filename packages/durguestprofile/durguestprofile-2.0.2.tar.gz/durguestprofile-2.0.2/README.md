# durguestprofile
## Provides a complete Integrated Development Environment to automate Guest Profile Audit

[![PyPI Latest Release](https://img.shields.io/pypi/v/durguestprofile.svg)](https://pypi.org/project/durguestprofile/)
[![Package Status](https://img.shields.io/pypi/status/durguestprofile.svg)](https://pypi.org/project/durguestprofile/)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://app.gitter.im/#/room/#durguestprofile:gitter.im)

## Main Features
Here are just a few of the things that durguestprofile does well:

### Combine Guest Profile Data
Extract the following reports from Opera PMS, Profile Address for individual guests only.
This Sample code will join the following files into one reusable Excel workbook.

* use osr_landscape.osr to collect the guest profile data.

You can add as many as files and hotels in one folder.
You will be asked to choose the folder where all the above files are saved.
Final output will be 'FINAL_AUDIT_DATE.csv' file in same folder.
Warning: Do not change the csv file data structure.
Use this file to feed the Excel Template and start validating the output and
to update Power BI dashboards.

```
from durguestprofile import properties_score
df = properties_score(files_folder=files_folder, criteria_file=criteria_file)
```

## Where to get it
The source code is currently hosted on GitHub at: 
https://github.com/roinsightsupport/durguestprofile

Binary installers for the latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/durguestprofile).

```
pip install durguestprofile
# or Trusted host PyPI
pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org durguestprofile
```

## Python
Python 32bit is required, you can install it from the following sources.
* [python.org](https://www.python.org/downloads/)
* [Portable Python](https://winpython.github.io/)

## Dependencies
- numpy>=1.23.5
- pandas>=1.5.3
- XlsxWriter>=3.0.3
- lxml>=4.9.1
- pyparsing>=3.0.9
- openpyxl>=3.0.10
- customtkinter==5.1.2
- sparse_dot_topn>=0.3.1
- scikit-learn>=1.1.1
- scipy>=1.10.0
- matplotlib==3.7.1

See the [full installation instructions] for minimum supported versions of required, recommended and optional dependencies.

## License
[ROInsight.com](LICENSE)

## Documentation
The official documentation is hosted on 
https://pypi.org/project/durguestprofile

## Getting Help

Further, general questions and discussions can also take place on the [Gitter](https://app.gitter.im/#/room/#durguestprofile:gitter.im).

## Contributing to durguestprofile

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

If you are simply looking to start working with the durguestprofile codebase, navigate to  start looking through interesting issues.


