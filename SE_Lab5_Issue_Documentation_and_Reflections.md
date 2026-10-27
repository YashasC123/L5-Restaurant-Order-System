# SE Lab 5 — Static Code Analysis

**Student:** Yashash C.  
**SRN:** PES2UG24CS611  
**Project:** Restaurant Order System  
**Repository:** https://github.com/YashasC123/L5-Restaurant-Order-System

## 1. Issue Documentation Table

The table records the issues observed during the original analysis and the changes made to address them. Line numbers are not listed because the corrected file has different line positions from the original version.

| Issue | Tool / source | Description | Fix applied |
|---|---|---|---|
| Mutable default argument | Pylint | `order_log=[]` could reuse a mutable list across calls. | Changed the default to `None` and initialized a new list inside the function. |
| Missing docstrings | Pylint | Functions did not consistently explain their purpose. | Added concise docstrings. |
| Function naming | Pylint | Some function names used camelCase instead of snake_case. | Renamed functions to snake_case and updated their call sites. |
| Bare exception handler | Pylint | A bare `except` could hide unrelated errors. | Caught the expected `KeyError` when deleting a table order. |
| Comparison with `None` | Pylint | Used equality comparison when checking for `None`. | Changed the check to `is None` where applicable. |
| Unused variables | Pylint | Some variables were assigned but not used. | Removed unnecessary variables. |
| Unsafe `eval()` | Pylint / security review | Evaluating an input expression can execute unintended code. | Replaced expression evaluation with a numeric discount-rate calculation and validation. |
| Insecure PIN generation | Bandit | `random.randint()` is not suitable for security-sensitive random values. | Used `secrets.randbelow()` to generate a four-digit PIN. |
| Shell command invocation | Security review | `os.system()` was used for a notification that did not require a shell. | Replaced the shell command with a Python `print()` statement. |
| Hard-coded token | Security review | A POS token was written directly in the source file. | Read the token from the `POS_TERMINAL_SECRET_TOKEN` environment variable. |
| Weak hash algorithm | Security review | MD5 was used to generate the ticket digest. | Replaced MD5 with SHA-256. |
| File handling | Code-quality review | The file was opened and closed manually. | Used a `with open(...)` context manager and specified UTF-8 encoding. |
| Long line / formatting | Pylint / Flake8 | Some statements did not follow the expected formatting style. | Reformatted statements and reran the style checker. |
| Trailing whitespace | Flake8 | Extra spaces at the end of a line caused a style warning. | Removed trailing whitespace and reran Flake8. |

## 2. Reflection Answers

> Note: These answers address the lab's stated learning outcomes. If the instructor provided specific reflection questions elsewhere, use those exact questions and adapt the answers accordingly.

### Reflection 1: What is static code analysis, and why is it useful?

Static code analysis examines source code without running the program. It helps detect potential bugs, security risks, and style violations early. This improves code quality, readability, maintainability, and reliability.

### Reflection 2: What did you learn from Pylint, Bandit, and Flake8?

Pylint checks code quality and common programming mistakes, Bandit looks for common security risks in Python code, and Flake8 checks style and formatting. Using all three provides complementary checks rather than relying on a single tool.

### Reflection 3: What issues did you fix in the program?

I corrected the mutable default argument, renamed functions using snake_case, added docstrings, narrowed the exception handler, removed unsafe `eval()` and unnecessary shell invocation, replaced the PIN generator with a security-appropriate function, moved the POS token to an environment variable, changed MD5 to SHA-256, improved file handling, and fixed formatting issues.

### Reflection 4: How did you verify the fixes?

I reran the static analysis tools after changing the code. The observed final results were a Pylint score of **10.00/10**, no issues identified by Bandit, and no output from Flake8 after the trailing-whitespace correction. I also ran the Python program and observed the sample restaurant-order operations completing successfully.

### Reflection 5: What did you learn from this lab?

I learned that a program can run successfully and still have security, maintainability, or style problems. Static analysis tools help find different classes of issues before submission. Keeping before-and-after reports also makes it easier to demonstrate and review the changes.

## 3. Verification Summary

| Check | Final observed result |
|---|---|
| Pylint | 10.00/10 |
| Bandit | No issues identified |
| Flake8 | No output after the whitespace fix |
| Program execution | Sample operations completed successfully |

## 4. Git Commits and Reports

The repository contains the three lab-related commits:

1. `Add initial static analysis reports`
2. `Fix code quality and security issues`
3. `Add verified static analysis reports`

The repository also contains the before-and-after reports:

- `pylint_before.txt`
- `pylint_after.txt`
- `bandit_before.txt`
- `bandit_after.txt`
- `flake8_before.txt`
- `flake8_after.txt`

**Repository:** https://github.com/YashasC123/L5-Restaurant-Order-System

## Conclusion

The restaurant order system was updated to address code-quality, security, and formatting findings. The program was run, the three static analysis tools were rerun, and the reports were uploaded to the GitHub repository.
