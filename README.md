# EWB Phishing URL Awareness Checker

**Author:** Sneha Jangid  
**Group:** EWB AI POWERED CYBERSECURITY INTERNSHIP

## Overview

Phishing is a trick in which fake links or messages try to make someone share information such as a password or an OTP. This beginner Python project reads a URL as text and points out six warning signs that deserve a closer look. It does not open the URL or send information over the internet.

## Features

- Detects an `@` symbol in the URL.
- Flags URLs longer than 100 characters.
- Flags hostname text formatted like an IPv4 address.
- Flags hostnames with five or more dot-separated parts.
- Flags hostnames containing the `xn--` punycode marker.
- Flags URLs using HTTP.
- Handles empty and malformed input with a message.
- Allows multiple URLs to be checked in one run and exits when the user enters `q`, `quit` or `exit`.
- Prints a `REVIEW CAREFULLY` summary when warning signs are found.

## Requirements

- Python 3.10 or later
- No additional Python packages

## How to Run

Open a terminal in this project folder.

**Windows:**

```bash
python phishing_checker.py
```

If `python` is not recognised, try:

```bash
py phishing_checker.py
```

**macOS/Linux:**

```bash
python3 phishing_checker.py
```

Enter one of the sample URLs from `tests/test_samples.md`. The program only analyses the text and never visits the address. Enter `q` to exit.

## Example Output

For `http://192.0.2.10/account`, the warning messages should include:

```text
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.
Never enter passwords from unexpected links.
```

## Testing

Five required sample cases are listed in [`tests/test_samples.md`](tests/test_samples.md). Run each case, record the actual output, and mark PASS or FAIL only after comparing it with the expected result. Add your actual Python version, operating system and test date there.

## Screenshots

After running the program on your own computer, save these screenshots in the `screenshots` folder:

- `sample_run.png` — terminal command, sample input and printed result.
- `test_results.png` — the completed five-test table or readable terminal evidence.

The screenshot files are not included yet because they must show your real local run.

## Improvements

1. **Repeat and quit:** The program can inspect multiple sample URLs in one session. This avoids restarting it for every test. To verify this, enter more than one sample URL in the same run, then type `q`.
2. **Handle malformed input:** URL parsing is protected by `try/except`, so malformed bracketed input produces a message rather than stopping the program. To verify this, enter `http://[bad` and confirm the program returns a message without crashing.
3. **Warning summary:** When warning signs are found, the program counts them and prints `REVIEW CAREFULLY`. To verify this, enter `http://192.0.2.10/account` and confirm the program reports two warning signs.

Before submission, run these checks yourself and update the test evidence. Only describe a check as completed after you have personally run it.

## Limitations

This is an educational awareness checker, not a full URL reputation or malware detection service. It checks only six visible patterns. It does not visit URLs, query threat-intelligence services or prove that a link is safe or malicious. A URL with no listed warning signs may still be dangerous, and a URL with warning signs may be legitimate.

## Ethical Use

Use the sample strings supplied in the workbook. Do not open suspicious links to test them, collect credentials, send phishing messages or probe websites without written authorisation. Never commit passwords, OTPs, API keys or private data to GitHub.

## Author

Sneha Jangid — EWB AI POWERED CYBERSECURITY INTERNSHIP
