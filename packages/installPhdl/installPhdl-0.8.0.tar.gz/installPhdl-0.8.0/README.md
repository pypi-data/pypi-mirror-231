# PhotoLibDownloader [![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

A graphical user interface to "iCloud Photos Downloader", a tool to download your iCloud photos into local folders 

## MacOS installation
Installation in 3 simple steps.
Enter the following commands into a Terminal window:

1 - Check and -if prompted- install pip3 and python3 on your machine:

``` sh
$ pip3 -V
```
2 - Download the PhotoLibDownloader installation script from the repository:
``` sh
$ pip3 install installPhdl
```
3 - Create and install the PhotoLibDownloader app on your computer
``` sh
$ python3 -m installPhdl
```

### Windows and Linux

Compatible installation scripts will be provided with a future release

---
### Attribution
PhotoLibDownloader is a Python graphical user interface which hooks into the original code of
* [iCloud Photos Downloader](https://pypi.org/project/icloudpd/) - a command-line tool to download photos and videos from iCloud.

which in turn uses slightly modified code from
* [pyiCloud](https://pypi.org/project/pyicloud/) - a module which allows pythonistas to interact with iCloud webservices.
