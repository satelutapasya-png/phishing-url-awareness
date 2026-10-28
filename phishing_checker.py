
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check URL text for selected phishing warning signs."""

    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["Invalid URL format. Please check the input."]

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: Look for an @ symbol
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    # Check 2: Check whether the URL is longer than 100 characters
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # Check 3: Check whether the hostname is an IPv4 address
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    # Check 4: Count hostname segments
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    # Check 5: Look for a punycode marker
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    # Check 6: Check whether the URL uses HTTP
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def main():
    print("=" * 45)
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - URLs are not opened.")
    print("=" * 45)

    while True:
        raw_url = input(
            "\nEnter a sample URL to inspect (or type 'quit' to exit): "
        ).strip()

        if raw_url.lower() == "quit":
            print("Thank you for using the awareness checker.")
            break

        print("\nResult:")
        findings = inspect_url(raw_url)

        for item in findings:
            print("- " + item)

        if findings and findings != ["No URL entered."]:
            if not (
                len(findings) == 1
                and findings[0].startswith("No listed warning signs")
            ):
                print("\nReview carefully: warning signs are not proof of fraud.")

        print("\nRemember: Never enter passwords through unexpected links.")


if __name__ == "__main__":
    main()
