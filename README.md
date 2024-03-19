# mitre_extractor
A utility to extract MITRE ATTCK Techniques from a text file (csv|html|txt|json|etc), pdf, or URL.

Inspired by https://github.com/splunk/attack-detections-collector

# Usage
```
python.exe ./mitre_extractor.py --text ./test.txt
```

# Example Output

```
Technique ID: t1070 Incidence: 5
Technique ID: t1041 Incidence: 3
Technique ID: t1566 Incidence: 1
Technique ID: t1193 Incidence: 1
Technique ID: t1204 Incidence: 1
Technique ID: t1547 Incidence: 1
Technique ID: t1059 Incidence: 1
Technique ID: t1083 Incidence: 1
Technique ID: t1562 Incidence: 1
Technique ID: t1047 Incidence: 1
Technique ID: t1486 Incidence: 1
Technique ID: t1027 Incidence: 1
Technique ID: t1003 Incidence: 1
Technique ID: t1098 Incidence: 1
Technique ID: t1569 Incidence: 1
Unique Number of MITRE TEchniques found: 15.
Total MITRE Techniques found: 21
```
