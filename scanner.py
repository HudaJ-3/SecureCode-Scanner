import re


def scan_code(code):
    findings = []

    if re.search(r'password\s*=\s*["\']', code, re.IGNORECASE):
        findings.append("Possible hardcoded password found")

    if re.search(r'(api_key|apikey|secret)\s*=\s*["\']', code, re.IGNORECASE):
        findings.append("Possible hardcoded secret found")

    if "eval(" in code:
        findings.append("Use of eval() detected")

    return findings


if __name__ == "__main__":
    sample_code = '''
password = "admin123"
api_key = "ABC123"
eval(user_input)
'''

    results = scan_code(sample_code)

    print("SecureCode Scanner")
    print("------------------")

    if results:
        for finding in results:
            print("[WARNING]", finding)
    else:
        print("No security issues found.")