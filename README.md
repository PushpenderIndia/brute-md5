<h1 align="center">Brute.MD5.#</h1>
<p align="center">
    <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.7-green.svg">
  </a>
  <a href="https://github.com/Technowlogy-Pushpender/technowhorse/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203-lightgrey.svg">
  </a>
  <a href="https://github.com/Technowlogy-Pushpender/technowhorse/releases">
    <img src="https://img.shields.io/badge/Release-1.0-blue.svg">
  </a>
    <a href="https://github.com/Technowlogy-Pushpender/technowhorse">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a>
</p>


<p align="center">
  Advanced, Light Weight &amp; Extremely Fast MD5 Cracker/Decoder/Decryptor written in Python 3
</p>
              
                        This small python script can do really awesome work.

## Disclaimer
<p align="center">
  :computer: This project was created only for good purposes and personal use.
</p>

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.

## Features
- [x] Works on Windows/Linux/OSx etc which supports Python 3
- [x] Advanced, Lightweight, Easy to use
- [x] Based on BruteForce Technique
- [x] Saves the Result in .txt file
- [x] Shows total attempts made by Cracker
- [x] Automatically Stops the Script When Correct Password is Found
- [x] Zero Dependencies (Except Working Python & Good Wordlist)
- [x] Cracks with 200 word/sec Speed with 2GB Ram & Ordinary Pentium Processor 
- [x] Codes are easy to read & understand

## Tested On
[![Kali)](https://www.google.com/s2/favicons?domain=https://www.kali.org/)](https://www.kali.org) **Kali Linux - ROLLING EDITION**

[![Windows)](https://www.google.com/s2/favicons?domain=https://www.microsoft.com/en-in/windows/)](https://www.microsoft.com/en-in/windows/) **Windows 8.1 - Pro**

[![Windows)](https://www.google.com/s2/favicons?domain=https://www.microsoft.com/en-in/windows/)](https://www.microsoft.com/en-in/windows/) **Windows 7 - Ultimate**

## Prerequisite
- [x] Python 3.X  
  #### Recommended 3.7.3 because I'm Using that version

## How To Use in Linux
```bash
# Install dependencies 
$ Install latest python 3.x

# Clone this repository
$ git clone https://github.com/Technowlogy-Pushpender/brute-md5.git

# Go into the repository
$ cd brute-md5

# Installing dependencies
$ python -m pip install pyfiglet argparse

# Getting Help Menu
$ python brute_md5.py --help

# Cracking MD5 Hash Without saving Result
$ python brute_md5.py -p <Hash> -w <Wordlist.txt>
$ Note: Wordlist.txt must be in same place where cracker is stored

# Cracking Example
$ python brute_md5.py -p cb814ff9b375e089e2e5e39d8a41e047 -w passwd.txt

# Cracking MD5 Hash & saving Result
$ python brute_md5.py -p <Hash> -w <Wordlist.txt> -o <File_name.txt>
$ Note: Wordlist.txt must be in same place where cracker is stored

# Cracking Example
$ python brute_md5.py -p cb814ff9b375e089e2e5e39d8a41e047 -w passwd.txt -o result.txt
```

## How To Use in Windows
```bash
# Install dependencies 
$ Install latest python 3.x

# Clone this repository
$ git clone https://github.com/Technowlogy-Pushpender/brute-md5.git

# Go into the repository
$ cd brute-md5

# Installing dependencies
$ python -m pip install pyfiglet argparse

# Getting Help Menu
$ python brute_md5.py --help

# Cracking MD5 Hash Without saving Result
$ python brute_md5.py -p <Hash> -w <Wordlist.txt>
$ Note: Wordlist.txt must be in same place where cracker is stored

# Cracking Example
$ python brute_md5.py -p cb814ff9b375e089e2e5e39d8a41e047 -w passwd.txt

# Cracking MD5 Hash & saving Result
$ python brute_md5.py -p <Hash> -w <Wordlist.txt> -o <File_name.txt>
$ Note: Wordlist.txt must be in same place where cracker is stored

# Cracking Example
$ python brute_md5.py -p cb814ff9b375e089e2e5e39d8a41e047 -w passwd.txt -o result.txt
```

### Note : Procedure for cracking is same in all OS

## Screenshots:
#### Getting Help
![](/img/1.getting_help.PNG)

#### Cracking Hash Without Saving Result 
![](/img/2.cracking_hash.PNG)

#### Cracking Hash & Saving Result 
![](/img/3.cracking_hash_saving_result.PNG)

#### Result Got Saved in .txt file 
![](/img/4.saved_result_txt.PNG)

## Contributors:
Currently this repo is maintained by me (Pushpender Singh). Owner of https://www.technowlogy.tk Website.

All contributor's pull request will be accepted if their pull request is worthy for this repo.

## TODO
- [ ] Add new features
- [ ] Contribute GUI
- [ ] Add New Hash Cracking Function

## Contact 
singhpushpender250@gmail.com or [Contact Us](https://technowlogy.tk/contact-us)
