![vulnblast logo](https://i.postimg.cc/rw7bs4jr/23c7c9e9-0d07-4d57-81a6-e86e5ca5fce0.png)
# VulnBlast

This project is a powerful and versatile password cracking tool, designed for penetration testers, security researchers, and ethical hackers. The tool is capable of performing various types of password attacks, including dictionary attacks, brute force attacks, and hybrid attacks. It supports various attack modes, such as single crack mode, mask mode, and combination mode. It also supports various hash types, including MD5, SHA1, SHA256, and many more. The tool is designed to be highly customizable, allowing users to add their own wordlists, rules, and plugins.

## Acknowledgements

 - [NMAP](https://nmap.org/)
 - [Nikto](https://cirt.net/nikto/)
 - [DirB](https://tools.kali.org/web-applications/dirb)
 - [SQLMap](http://sqlmap.org/)
 - [XSSer](https://www.xsser.com/)
 - [Hashlib](https://docs.python.org/3/library/hashlib.html)
 - [Argparse](https://docs.python.org/3/library/argparse.html)
 - [PyFiglet](https://pypi.org/project/pyfiglet/)
 - [RainbowText](https://pypi.org/project/rainbow-text/)
 


## Authors

- [@cypherdavy](https://github.com/cypherdavy)


## Badges


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
[![Code Quality](https://img.shields.io/codacy/grade/d0e4f58565b0446b933d8b06f3e3437a.svg)](https://app.codacy.com/gh/blackhatGPT/vulnblast/dashboard)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Features

- Syntax highlighting
- Auto-completion
- Code folding
- Bracket matching
- Line numbering
- Command-line access
- Customizable themes
- Plugin support



# Installation


*To get started with VulnBlast, follow these steps*

**Clone the project repository**

```bash
git clone https://github.com/cypherdavy/Vulnblast.git
```
**Navigate to the project directory**
```bash
cd Vulnblast
```
**Install the required dependencies**
```bash
pip install -r requirements.txt
```
**Run the project**
```bash
python vulnblast.py
```



## Run Locally

Clone the project repository:
```bash
git clone <https://github.com/cypherdavy/Vulnblast.git>
```
Navigate to the project directory:
```bash
cd Vulnblast
```
Install the required dependencies:
```bash
pip install -r requirements.txt
```
Run the project:
```bash
python vulnblast.py

```

## Usage/Examples

```python
import subprocess

target_url = 'https://example.com'
wordlist_file = 'wordlist.txt'

command = ['vulnblast', 'scan', '-u', target_url, '-w', wordlist_file]
```
