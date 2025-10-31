import sys
from xml.etree import ElementTree as ET

THRESHOLD = 0.80

if __name__ == "__main__":
    tree = ET.parse('coverage.xml')
    root = tree.getroot()
    # coverage.py XML root has 'line-rate' attr for overall coverage
    line_rate = root.get('line-rate')
    if line_rate is None:
        print('No line-rate found in coverage.xml')
        sys.exit(2)
    cov = float(line_rate)
    print(f'Coverage: {cov*100:.2f}%')
    if cov < THRESHOLD:
        print(f'FAIL: coverage {cov*100:.2f}% < {THRESHOLD * 100}%')
        sys.exit(1)
    print('OK')
    sys.exit(0)