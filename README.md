# Security Automation Scripts

A collection of Python and PowerShell security automation projects focused on vulnerability management, system monitoring, patch management, and remediation.

## Features

- System security and configuration checks
- Vulnerability management automation
- Patch management and validation
- Security monitoring
- Administrative automation
- Security reporting

## Technologies

- Python
- SQL
- PowerShell
- Windows
- Linux
- Git/GitHub

## Current Project

### System Security Check

The `system_security_check.py` script collects basic system information useful for security and administrative reviews, including:

- Hostname
- Operating system
- OS version
- System architecture
- Current user

## Security Notice

All scripts in this repository are sanitized demonstration projects. They do not contain employer data, credentials, internal URLs, IP addresses, or proprietary configurations.

## Author Vincent Anany

## Testing

The vulnerability assessment tool was successfully tested on macOS.

### Test Results

The tool successfully:

- Collected operating system and system architecture information
- Identified the current user context
- Evaluated available disk space
- Identified the current privilege level
- Classified findings by severity

During testing, the tool identified a medium-severity disk-space warning
and confirmed that the assessment was running with standard user
privileges.

The project demonstrates Python-based security assessment, automation,
finding classification, and security reporting.

## Vulnerability Report Analyzer

The `vulnerability_report_analyzer.py` script analyzes sample vulnerability
data and generates security metrics and remediation priorities.

### Capabilities

- Counts vulnerabilities by severity
- Tracks open and remediated findings
- Calculates remediation rate
- Prioritizes open vulnerabilities using CVSS scores
- Produces a security summary for remediation planning

### Sample Results

- Total vulnerabilities: 5
- Open findings: 3
- Remediated findings: 2
- Remediation rate: 40%
- Critical: 1
- High: 2
- Medium: 1
- Low: 1

### Remediation Priority

The analyzer prioritizes unresolved vulnerabilities by CVSS score, helping
security teams identify higher-risk findings that should be addressed first.

> Note: All vulnerability IDs, assets, and findings in this project are
> fictional and are provided for demonstration purposes only.


Vincent Anany
