# User-Activity-Logger
An educational Python script by me, Thash to demonstrate logging user actions and public IP addresses locally. It’s designed to help learners understand authentication, file handling, and working with public APIs, with all data stored on the user’s device for privacy

# Disclaimer
The IP logging module only stores data locally on your device and does not send it to any external servers. If you encounter any bugs, please be patient as I work on fixing them. Additionally, any feedback or improvements are greatly appreciated to help me continue developing my coding skills.

## What You Will Learn
1. **HTTP Requests**: Learn how to fetch data from an external API (e.g., fetching your public IP address).
2. **File Handling**: Understand how to append logs to a file.
3. **Date and Time**: Use Python's `datetime` module to timestamp actions.
4. **Basic Authentication**: Implement simple user authentication.
5. **Code Modularization**: Learn to structure code for optional features.


This script allows you to monitor login attempts, including logging the user's public IP address, to a file on the local device.

## Features
- Tracks login attempts with timestamps.
- Logs public IP addresses (optional, can be removed).
- Allows registering new users.

## Requirements
- Python 3.5 or later
- Internet access for public IP logging (if enabled).

## Setup
1. Install required Python libraries (ONLY FOR ENABLED IP LOGGING):
   ```bash
   pip install requests 
