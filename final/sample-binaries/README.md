##### Submission by the _SDDR_ Group for the Final Exam: Cyber Grander Challenge in CSE4830.

### [Google Drive Folder](https://drive.google.com/drive/folders/1cdcL03g5zB2vutJCjjeq-Ro25LG-ZKcu?usp=sharing “Google Drive Folder”)

## Team Members
|Name|Leader?|
|----|----|
|Kourtnee Fernalld|Yes|
|----|----|
|Ivan Hernandez|No|
|----|----|
|Dave Breeden|No|
|----|----|
|Cael Shoop|No|

---

## Workload Distribution
### Kourtnee
Wrote easy_format.py, sddr_rop.py.
Contributed to Identify.py.
### Ivan
Wrote Identify.py, aeg.py, and CGC.py.
Contributed to sddr_rop.py.
### Dave
Wrote {???}.
Contributed to Identify.py.
### Cael
Wrote README.md.
Attempted to write a script to replace the value of *Pwnme* with 1337. Ivan's aeg.py was successful with this before Cael's script worked.

***

# Setup and Run
Please download all .py files. You can run **aeg.py** with an binary filename supplied into BIN:
```python3 aeg.py BIN={binary}```
or run **CGC.py** with all of the binary files placed in a vulns/ directory:
```python3 CGC.py```

---

## How It Works

#### CGC.py - Test Execution
Uses **os** to run **aeg.py** on each vuln in the vulns/ directory.

#### aeg.py - Main Script
Uses **pwn**, **Identify.py**, and **easy_format.py**. It accepts a binary name and creates a ROP instance, which is passed with the binary into **Identify.py** to create *curBinary*. This is passed into AttackVector() and assigned to *string*. It then is compared to "Pwnme", "Ret2Execve + /bin/sh", "WritePrim", and "Ret2Win" and calls the corresponding function. If it is none of those, it passes the binary into *Format_easy()*.

#### Identify.py - Identifies Vulnerabilities
Uses **e.sym[]**, **r.find_gadget([])**, and **e.search()** to build a list of vulnerabilities within the binary passed to it.

#### easy_format.py - Exploits Binaries.
Contains *Format_easy()*. Within a 20 iteration for loop, it sends registry values into the binary and receives output until it encounters a colon. It then strips "0x", splits by spaces, decodes, and strips the recvline() data and assigns that to *leak*. After that, it will try to decode unhexlify(leak) and append that to the *total* list.

#### sddr_rop.py - Exploits Binaries.
Class to call subprocess and return a more precise list of potential rop gadgets, as well as a setup register method for some rop chains.