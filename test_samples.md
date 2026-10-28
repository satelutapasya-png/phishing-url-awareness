# Phishing URL Awareness Checker — Test Results

## Test Environment

- **Language:** Python
- **Python version:** 3.14.7
- **Operating system:** Windows
- **Testing method:** Manual command-line testing

## Test Cases

| Test | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | `http://192.0.2.10/account` | IP address and HTTP warnings | IP address warning and HTTP warning displayed. | PASS |
| 3 | `http://example.com@sample.invalid/login` | @ symbol and HTTP warnings | @ symbol warning and HTTP warning displayed. | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments warning | Many hostname segments/subdomains warning displayed. | PASS |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname warning | Punycode-style hostname warning displayed. | PASS |

## Learning Notes

The project checks URL text for selected warning signs without opening websites or sending network requests. The results are indicators for careful review, not proof that a URL is malicious or safe.