

## LFI / RFI

File inclusion occurs when the user can control the file that will be loaded by the server.

LFI (Local File Inclusion) -> The server loads a local file.

RFI (Remote File Inclusion) -> The server loads a file located on a remote server.


## Log Poisoning

If can control the file that is being loaded (LFI) and you want to execute functions. You can use Log Poisoning!

### How does this work?

Let's imagine that the website is using PHP. You want to be able to execute php code to gain RCE.








