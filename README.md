# EWB Phishing URL Awareness Checker

## Overview

The Phishing URL Awareness Checker is an educational cybersecurity mini-project developed in Python. It examines the visible text of a URL and identifies selected warning signs that may require closer inspection.

The program does not open websites, make internet requests, or send URL data anywhere.

## Features

The checker looks for six warning signs:

1. An `@` symbol in the URL.
2. A URL longer than 100 characters.
3. An IP address used as the hostname.
4. Five or more hostname segments.
5. A punycode-style hostname containing `xn--`.
6. Use of the HTTP scheme.

It also handles empty input and certain malformed URLs, provides a review reminder, and allows multiple sample URLs to be checked in one session.

## Requirements

- Python 3.10 or later
- No additional Python packages

## How to Run

1. Open the project folder in Visual Studio Code.
2. Open a terminal in that folder.
3. Run:

   ```bash
   python phishing_checker.py
   ```

4. Enter a sample URL when prompted.
5. Type `quit` to exit.

## Example

Sample input:

```text
http://192.0.2.10/account
```

Expected warning signs:

- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

## Testing

Five sample URL cases are documented in `tests/test_samples.md`. Their actual results should be recorded after manual testing.

## Screenshots

### Sample Run

![Sample run](screenshots/sample_run.png)

### Test Results

![Test results](screenshots/test_results.png)

## Improvements

- Added a loop for checking multiple sample URLs.
- Added a review reminder when warning signs are found.
- Added handling for certain malformed URL inputs.

## Limitations

This tool performs simple text-based checks. It does not determine a website's reputation, inspect its content, or verify whether a URL is safe. Some dangerous URLs may not trigger any warning signs, and legitimate URLs may trigger warnings.

## Ethical Use

Use the project for cybersecurity awareness and educational testing. Use the provided sample URLs rather than visiting suspicious links.

## Author

Tapasya Satelu