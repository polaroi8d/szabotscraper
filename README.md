Szabot scraper :nut_and_bolt:
===================

This is a simple tool, which helps you to get your test results easily with python. If you want to contribute to the project, please read the associated topic in the docs. Feel free to ask questions. :nut_and_bolt:

[![Build Status](https://travis-ci.org/polaroi8d/szabotscraper.svg?branch=master)](https://travis-ci.org/polaroi8d/szabotscraper)
[![License](https://img.shields.io/badge/licence-Apache%202.0-brightgreen.svg?style=flat)](LICENSE)

![szabotscrapcer_gif](http://orbanlevi.hu/szabotscraper_intro.gif)


### Requirements

Use `pip install -r requirements.txt` command to install all the dependencies:

- bs4
- BeautifulSoup
- argparse
- mechanize
- html5lib


### Usage

#### Linux

Clone from the GitHub repository:


    mkdir szabotscraper
    git clone git@github.com:polaroi8d/szabotscraper.git


Simply usage is to add your EHA in the first argumentum:


    cd szabotscraper
    python szabot.py abcdefg.sze


More powerfull:fire: usage if you add the script to your ~/.bashrc file with alias like the gif above. Open your ~/.bashrc file with your favourite text editor. I am using Sublime for it and add the following line in the file
        `alias mumat='python /path/path/szabotscraper/szabot.py orlvaat.sze'`

- **path** is your unique path where you cloned the script
- **mumat** mark the command which you need to use to get your results

    ```
    subl ~/.bashrc
    source ~/.bashrc
    ```

### Tested on

 - macOS Sierra 10.12.3 & python 2.7.13 :cookie:
 - Ubuntu 16.10 & python 2.7.12 :lollipop:


### License

**Szabot scraper** :nut_and_bolt: is open source software under the Apache License 2.0. Complete license and copyright information can be found in the source code.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at  [LICENSE 2.0](http://www.apache.org/licenses/LICENSE-2.0) Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.