# mitre_extractor
A utility to extract MITRE ATTCK Techniques from a text file (csv|html|txt|json|etc), pdf, or URL.

Inspired by https://github.com/splunk/attack-detections-collector

# Usage
```
./mitre_extractor.py
Enter report: https://www.huntress.com/blog/using-backup-utilities-for-data-exfiltration
```

# Example Output

```
Technique ID: t1078 Incidence: 2
Technique ID: t1133 Incidence: 1
Technique ID: t1059 Incidence: 1
Technique ID: t1027 Incidence: 1
Technique ID: t1560 Incidence: 1
Technique ID: t1039 Incidence: 1
Technique ID: t1567 Incidence: 1
Unique Number of MITRE TEchniques found: 7.
Total MITRE Techniques found: 8
```
