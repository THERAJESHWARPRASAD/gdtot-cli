<!--
 Copyright (c) 2022 [.shovon]
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

# Gdtot CLI Tools

This is a python script that can generate google drive download link from gdtot urls, download gdtot to specific drive folder and generate worker url for that file if available.

### Requirements:

- Python3

- Gdtot account and the crypt

    - How to get crypt: [Link](https://github.com/anasty17/mirror-leech-telegram-bot/tree/master#gdtot-cookies)

### Optional Requirements:

- Google drive token

    - Getting Google OAuth API credential file and token.pickle: [Link](https://github.com/anasty17/mirror-leech-telegram-bot/tree/master#3-getting-google-oauth-api-credential-file-and-tokenpickle)

- Target google drive folder id

- Worker url


### How to setup and use:

The config for this script is stored in `config.ini`. Make a copy of `config_sample.ini` and rename it to `config.ini`. For a basic setup just put the crypt string in the gdtot section of the config file and save. Run the script by `python main.py` or `python3 main.py`, paste the gdtot url and the link for drive will be shown on the terminal.

For downloading in a target folder, generate a `token.pickle` and paste it in script's folder, put the target download folder id in `config.ini` drive section and run the script by `python main.py` or `python3 main.py`. Rest is same as above.

To generate a worker direct download url, paste the full worker path in the `config.ini` worker section.
