
# FCSC 2023: La gazette de Windows
## Stillwolfing

Here is the context:

![context](/assets/img/CTFs/FCSC2023/Intro/la_gazette_de_windows/context.png)

We are given a windows log file (Microsoft-Windows-PowerShell4Operational.evtx)

Let's open it in the Event Viewer:

![event_viewer](/assets/img/CTFs/FCSC2023/Intro/la_gazette_de_windows/event_viewer.png)

We have only 9 logs, it will make things easier.

In the first log, the user checks if the variable $global exists.

![global](/assets/img/CTFs/FCSC2023/Intro/la_gazette_de_windows/global.png)

In the second log, the user executes whoami. He is checking is permissions:

![perms](/assets/img/CTFs/FCSC2023/Intro/la_gazette_de_windows/perms.png)

In the third log, the user execute "C:\Users\jmichel\Downloads\payload.ps1" which contains "{0}". He is just testing.

![remote_code](/assets/img/CTFs/FCSC2023/Intro/la_gazette_de_windows/remote_code.png)


In the fourth log, the user execute "C:\Users\jmichel\Downloads\payload.ps1" which contains a more complicated code.

![remote_code](/assets/img/CTFs/FCSC2023/Intro/la_gazette_de_windows/test_buffer.png)

Within the function, it first creates a buffer of bytes using an array range operator (0..$TCPClient.ReceiveBufferSize). The value of each element in the array is set to zero using the percentage (%) symbol and the script scope variable "$script:Buffer".

Then, the function writes the provided string plus the string "SHELL>" to a stream writer object called "$StreamWriter", and flushes the writer to ensure that any buffered data is sent immediately.

Note that this function relies on the existence of a TCPClient object, which is not defined in the code.

Here is the code executed in the fifth log:

![payload](/assets/img/CTFs/FCSC2023/Intro/la_gazette_de_windows/payload.png)

This PowerShell script does the following:

1. It continuously attempts to create a TCP connection to an IP address "10.255.255.16" on port 1337 until it succeeds.

2. Once a connection is established, it creates a StreamWriter object to write data to the TCP network stream.

3. It defines a function named WriteToStream, which writes a string to the StreamWriter object with the prefix "SHELL> ".

4. It creates an array of bytes named "l" and populates it with values.

5. It performs an XOR operation on each byte of the "l" array with the corresponding value of the loop variable "i" to obtain another array of bytes "s".

6. It calls the WriteToStream function with the "s" string as a parameter to send the decoded command to the TCP network stream.

7. It reads input from the TCP network stream, executes the input as a PowerShell command using Invoke-Expression, captures the output, and sends the output to the TCP network stream using the WriteToStream function.


It is RCE (Remote Code Execution) with the variable "s" being the command.

We will attempt to find what the command is.

Since this is just a XOR, I will execute the code:

```powershell
$l = 0x46, 0x42, 0x51, 0x40, 0x7F, 0x3C, 0x3E, 0x64, 0x31, 0x31, 0x6E, 0x32, 0x34, 0x68, 0x3B, 0x6E, 0x25, 0x25, 0x24, 0x77, 0x77, 0x73, 0x20, 0x75, 0x29, 0x7C, 0x7B, 0x2D, 0x79, 0x29, 0x29, 0x29, 0x10, 0x13, 0x1B, 0x14, 0x16, 0x40, 0x47, 0x16, 0x4B, 0x4C, 0x13, 0x4A, 0x48, 0x1A, 0x1C, 0x19, 0x2, 0x5, 0x4, 0x7, 0x2, 0x5, 0x2, 0x0, 0xD, 0xA, 0x59, 0xF, 0x5A, 0xA, 0x7, 0x5D, 0x73, 0x20, 0x20, 0x27, 0x77, 0x38, 0x4B, 0x4D;
$s = "";
for ($i = 0; $i -lt 72; $i++) { $s += [char]([int]$l[$i] -bxor $i) }
echo $s
```

The result is the flag 😋

![flag](/assets/img/CTFs/FCSC2023/Intro/la_gazette_de_windows/flag.png)

By curiosity, let's take a look at the other logs.

In the sixth log, the user run change the execution policy to bypass so that he can execute his script. Then he execute the script.

![execution_policy](/assets/img/CTFs/FCSC2023/Intro/la_gazette_de_windows/execution_policy.png)


The seventh log has the EventID 40962 which is PowerShell console is ready for user input.


The eighth log is the user inputs:

![user_input](/assets/img/CTFs/FCSC2023/Intro/la_gazette_de_windows/user_input.png)

The final log has event id 40961 which is PowerShell console is starting up. The script is running.



