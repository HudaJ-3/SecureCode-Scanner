from scanner import scan_code


def test_hardcoded_password():
    code = 'password = "admin123"'
    results = scan_code(code)

    assert "Possible hardcoded password found" in results


def test_eval():
    code = "eval(user_input)"
    results = scan_code(code)

    assert "Use of eval() detected" in results