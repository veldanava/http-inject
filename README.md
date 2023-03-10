# HTTP Packet Inject:

HTTP Packet Inject is a project aimed at intercepting and injecting HTTP packets to monitor and modify network traffic. This project is useful for network administrators, security professionals, and developers who need to analyze HTTP traffic or test the security of web applications.

## Example:

![WhatsApp Image 2023-03-10 at 2 20 09 PM](https://user-images.githubusercontent.com/84911110/224254431-9f333e59-4d2d-4dfc-800e-f60080d9cc53.jpeg)

![WhatsApp Image 2023-03-10 at 2 20 09 PM (1)](https://user-images.githubusercontent.com/84911110/224254405-28135524-6f47-4d6b-aaa5-2f9ccd57fda0.jpeg)

## Dependencies:
Python 3.x <br>
scapy library <br>
NetfilterQueue <br>
colorama <br>

## Installation:

Clone the repository:
```zsh
https://github.com/veldanava/http-packet-inject
```
Install Requirement:
```zsh
pip install -r requirement.txt
```
## Supported Platform:
```zsh
For now, we only support Linux because there are libraries that only support Linux
Some linux may get error in Netfilterqueue
```

## Running:
Start the program:
```
python main.py
````
>input ur injection code <br>
>this program works with ARP Spoofing as a partner, so you have to do Spoofing first

## Contribution:
Feel free to contribute to this project by submitting bug reports or feature requests through GitHub issues or by creating a pull request.
