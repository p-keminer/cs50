# Local Port Scanner & Report Generator

#### Video Demo: https://youtu.be/SO0Cmr6KRkE

#### Description:

This project is a port scanner written in Python with report generation capabilities, intended solely for use on authorized targets and for educational purposes.
The idea arose because I work extensively with microcontrollers and systems in general, and it offers real added value, particularly for security-sensitive interfaces.

The port scanner is not a simple script that just runs through the process, but a full-fledged CLI application that parses, validates, and checks user input, and based on this, performs a port scan within a selected range.
The goal of the tool is to verify the information a system exposes to the outside world and to record it in both machine-readable and human-readable reports.
It can check both TCP and UDP ports, although UDP ports are inherently more unreliable to check due to their native architecture.

The project is fundamentally designed as a CLI application, but due to the modularity of its individual functions, it can be easily extended with, for example, a GUI.
However, this was important to me for the MVP so that I could focus on the underlying logic, such as network connections, sockets, input validation, error handling, data formatting, and file output.

The most important thing is: this project is not an attack tool but is intended solely for defensive and educational purposes; this was also the very first feature implemented,
namely the prompt at the start of the project, where the tool requires confirmation that it will be used only for educational purposes or against authorized targets.

After the user confirms that the tool will only be used against authorized targets, the user is prompted to set the host, start port, end port, and a timeout.

Hosts can be specified as IP addresses or as simple domain names; IP entries are validated by a helper function from a pset in cs50p, otherwise the system first checks whether the host can be resolved using `socket.gethostbyname`.

The actual scanning logic is divided into several individual functions, such as `is_tcp_port_open`, which creates a TCP socket, sets a timeout, and uses `connect_ex` to establish a connection to the respective port.
The function’s return value validates whether the port is open (0 = open).

In addition, the tool checks typical UDP ports by sending small individual probes and verifying whether a response is received; however, as mentioned at the beginning, this is quite unreliable because, depending on the design of the UDP protocol, UDP ports may or may not respond.
Ultimately, the tool’s limitation is that it can only detect poorly configured UDP ports in order to avoid excessively prolonging the runtime.

For detected TCP ports, the tool then checks whether it can obtain further information; for example, it sends simple ‘HEAD’ requests to HTTP-like services to retrieve a header. From this, additional information such as specific header details—e.g., ‘Server’—can be extracted.
If no header can be read, a simple attempt is made to grab a banner. Here, too, there is a limitation, as some services send a banner directly while others do not;
therefore, reliability is a deliberate design choice here as well, serving only as an additional fallback to obtain “as much information” as possible without straining runtime.

Subsequently, `classify_service` determines how the service is named; this is based on 1.) HTTP headers, 2.) the banner, 3.) its own port table, and finally 4.) the system database `socket.getservbyport`. From this, a “confidence level” is additionally derived and added to the report.

Another deliberate design decision was the handling of the discovered ports, which are subsequently stored as a dictionary containing IP address, port, protocol, status, service, source, confidence, banner, header, and evidence.
This was important to keep the file formatting as simple as possible in the end.

Finally, there is one of the most important main functions for formatting and output: `build_summary`, which counts the number of TCP and UDP ports, adds runtime measurements to the summary, and lists the respective services.

The machine-readable and human-readable reports are then generated in the `reports` directory, which is also created automatically if it does not exist.

The most important files in the project are:

- `project.py`: contains the complete program, scan logic, input prompts, service detection, formatting, and report functions.
- `README.md`: explains the purpose, operation, structure, design decisions, and limitations of the project.
- `requirements.txt`: remains empty
- `reports/`: is created automatically and contains generated TXT and CSV reports.

The project primarily uses the standard libraries `socket`, `time`, `re`, `os`, `shutil`, `sys`, `csv`, and `datetime`. External packages are not required for the current version.

You can run the program with:

```text
python project.py
```

When testing, you should use a permitted target, such as
your own device on the local network.


Other important limitations and design decisions include the fact that the tool is not a vulnerability scanner and does not map exploits; it merely collects harmless service information. It does not perform password attacks.
Port 443 (HTTPS) is also not examined further, as this would require a TLS handshake.

Overall, the goal was to build a small but functional network tool that combines several topics from CS50: functions, loops, conditions, dictionaries, lists, error handling, file I/O, and network programming,
but in particular to deepen my knowledge of Python, as well as to further sharpen my knowledge of network programming and cybersecurity.

---

AI Usage Disclosure
Chatgpt was used whilde developing this final project as a support tool for asking
questions about debugging errors, socket concepts and general python concepts

The project idea, code decisions, testing on my own Raspberry Pi and final implementation were completed and reviewed by me
