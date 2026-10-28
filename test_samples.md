# Test Results — EWB Phishing URL Awareness Checker

**Name:** Sneha Jangid  
**Group:** EWB AI POWERED CYBERSECURITY INTERNSHIP  
**Python version used:** Fill in after running `python --version`  
**Operating system:** Fill in (for example, Windows 11)  
**Test date:** Fill in the date you ran the tests

Run the program once for each sample below. Copy the actual warning messages shown in your terminal into the **Actual result** column. Mark **PASS** only when the output matches the expected result. Do not mark a test PASS before running it.

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs found; message says this does NOT prove safety | Fill after running | Pending |
| 2 | `http://192.0.2.10/account` | IP-address hostname and HTTP warnings | Fill after running | Pending |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol and HTTP warnings | Fill after running | Pending |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments/subdomains warning | Fill after running | Pending |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname warning | Fill after running | Pending |

## Notes

After running the five tests, write 2–3 sentences in your own words about what you learned and what surprised you. For example, explain why a result with no listed warning signs does not prove that a URL is safe.

## Extra checks for the improvements

- Enter `http://[bad` and confirm the program shows a clear invalid-URL message instead of crashing.
- Enter two sample URLs in the same run and confirm the program keeps asking for another URL.
- Type `q` and confirm the program exits with a goodbye message.
