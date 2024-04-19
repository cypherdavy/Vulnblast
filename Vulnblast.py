```python
import os
import subprocess
import datetime
import argparse

# VulnBlast logo
logo = """
 _   _   _   _   _   _   _   _   _  
/ \ / \ / \ / \ / \ / \ / \ / \ / \ 
( V | u | l | n | B | l | a | s | t )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/
"""

# Print tool name and author with logo
print(logo)
print("Welcome to VulnBlast - Your Deep Vulnerability Scanner")
print("Author: Cipherdavy\n")

def deep_vuln_search(target):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f"vulnerability_report_{timestamp}.txt"
    report = open(report_file, "w")
    
    nmap_output = subprocess.check_output(["nmap", "-sV", "-A", target])
    nikto_output = subprocess.check_output(["nikto", "-h", target])
    dirb_output = subprocess.check_output(["dirb", f"http://{target}"])
    sqlmap_output = subprocess.check_output(["sqlmap", f"-u http://{target}/vuln_page"])
    xsser_output = subprocess.check_output(["xsser", f"-u http://{target}/vuln_page"])
    
    report.write("Vulnerabilities found for target: " + target + "\n\n")
    report.write("NMAP Scan Results:\n" + str(nmap_output) + "\n\n")
    report.write("Nikto Scan Results:\n" + str(nikto_output) + "\n\n")
    report.write("Dirb Scan Results:\n" + str(dirb_output) + "\n\n")
    report.write("SQLMap Scan Results:\n" + str(sqlmap_output) + "\n\n")
    report.write("XSSer Scan Results:\n" + str(xsser_output) + "\n\n")
    
    report.close()
    print(f"Vulnerability scanning completed. Check {report_file} for results.")

def main():
    parser = argparse.ArgumentParser(description='VulnBlast - Your Deep Vulnerability Scanner')
    parser.add_argument('target', type=str, help='Target URL to scan for vulnerabilities')

    args = parser.parse_args()
    target = args.target

    deep_vuln_search(target)

if __name__ == "__main__":
    main()
```

