# Introduction
Transceiver is a lightweight program designed for use with ARM M class CPUs. It is able to transmit database entries through low frequency transmissions devices.

# Installation
Product installation is straightforward. Once downloaded and extracted from the .tar.gz file stored on GitHub, look for an INSTALLATION.sh or INSTALLAtION.exe file depending on what operating system you plan to run on your ARM CPU. Once the file is opened an installation script will begin. On both platforms, some information will be required for first-time setup and installation, such as preferred encryption methods and your antenna setup. Once installation is finished, you may be required to reboot your device. After a reboot, Transceiver will automatically search for antennas that match your criteria. Once an antenna is found, a terminal window may appear on your monitor or SSH client asking to define a database schema for transfer. Databases that are compliant with Transceiver are MongoDB, Oracle, and Postgre SQL.

# Usage
Transceiver is a database-specific transfer protocol for ARM CPUs. Most SQL formats will work with it, meaning you have versatility working with whatever format works best for you. When a database or specific schema of your database is defined, Transceiver will automatically transmit your data through an encrypted connection. This provides a large array of use cases, from wireless security cameras to your garage door. With the additional ability to transmit data to AWS Greengrass devices, the ability to successfully control devices using financially affordable methods.

# Support
If support is needed at any time with help installing or utilizing this software, please be free to either create an issue on GitHub or Email one of our developers.

## GitHub Issues
Creating an issue on GitHub is the easiest way for us to get information. We will typically respond to an issue within a 24-hour period, however, in some instances it may take longer. When creating an issue on GitHub, please be sure to include lots of detail, following a template if necessary. Additionally, please add labels to make it easy to distinguish requests for new features, possible bugs, and general questions about the software. Include images or reference specific lines of code for a quicker resolution to the issue.

## Emails
Emailing a team member should be used as a last resort for getting project support. It will most likely take longer for a response, and any form of common issue will be simply added on GitHub. To find an Email address to use, please look at the _"Authors"_ section of this file. When writing an Email, be sure to be descriptive and include a short summary of your issue as the subject.

# Contributing
For information about contributing to this project, please review further documentation at CODE_OF_CONDUCT.md and CONTRIBUTING.md.

# Authors
**Michael Dierkes**: kerosenemainframe@gmail.com

# License
Transceiver is an open-source project based on the MIT license. You can learn more about your rights to this software by reading information in the LICENSE file.

# Current Status
This project is currently in heavy development, and will not have releases published to GitHub until the software is found to function properly. Updates will be regularly published to this repository, so expect constant revisions to help in this challenge.
