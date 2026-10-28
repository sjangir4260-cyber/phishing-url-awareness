import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check URL text for six selected warning signs; never open the URL."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    # Add a scheme when the user leaves it out so urlparse can find the hostname.
    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: an @ symbol can make the apparent and actual host confusing.
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    # Check 2: very long URLs can hide their destination in a quick glance.
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # Check 3: a hostname written as four groups of digits may deserve review.
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    # Check 4: count the dot-separated pieces of the hostname.
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    # Check 5: xn-- is a marker used in punycode hostnames.
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    # Check 6: HTTP does not encrypt traffic in the way HTTPS does.
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append("No listed warning signs found. This does NOT prove safety.")

    return findings


def has_warnings(findings):
    """Return True when the result contains one or more warning signs."""
    non_warning_starts = (
        "No URL entered.",
        "Could not identify a hostname.",
        "This text is not a valid URL format.",
        "No listed warning signs found.",
    )
    return not any(findings[0].startswith(message) for message in non_warning_starts)


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    # Improvement 1: inspect more than one URL without restarting the program.
    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ")
        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)
        print("\nResult:")
        for item in findings:
            print("- " + item)

        # Improvement 2: give a readable response instead of crashing on bad input.
        # Improvement 3: summarise the number of warning signs found.
        if has_warnings(findings):
            print("\nREVIEW CAREFULLY: " + str(len(findings)) + " warning sign(s) found.")

        print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
