# SMS Processor

**SMS Processor** is an effort to create encrypted SMS messages.

## Installers

Check the release page for installers: https://github.com/nexusforgr/sms-processor/releases/

For Android:

https://github.com/nexusforgr/sms-processor/releases/download/beta/smsprocessor-0.1-arm64-v8a_armeabi-v7a-debug.apk


For Windows:

https://github.com/nexusforgr/sms-processor/releases/download/beta/main.exe

## Getting Started

Follow these instructions to set up and run the SMS Processor on your local machine.

### Prerequisites

- **Python 3.8 or higher**
- **Poetry** for managing dependencies

### Installation

#### Debian-based Linux Distributions

Install Poetry using the following command:

```sh
sudo apt install poetry
```

#### Windows
Install Poetry using pip:
```sh
pip install poetry
```

#### Install Packages
Use the following commands in the terminal to install all dependencies:

```sh
poetry install
```

### Running the Program
Enter the Poetry shell and run the software:

```sh
poetry shell
python sms_processor/main.py
```