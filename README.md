# tokengrabber
Tool to sniff honeytokens from the system. There are 2 methods of detection. The first method leverages the 
use of DNS calls made by canarytokens to trigger emails by sniffing all DNS lookups from the target machine to check for canarytokens domain.


The second method performs some reverse engineering and pattern matching to find canrytokens in their content.
The usage is described below.  


Usage:

DNS sniffer\
$python dns_sniffer.py -i interface \
example: $python dns_sniffer.py -i eth0

PDF Token\
python pdf-parser.py -o 16 -O filename.pdf \
the /URI of the object stream contains canarytokens.net

DOCX Token\
python docx.py -f filename.docx

DIRECTORY Token\
python folder.py --d dir_name

__Screenshots__

DNS Sniffer:

![DNS](https://github.com/sastry17/tokengrabber/blob/master/screenshots/DNS.png)

Detection for folder, pdf and docx Canarytokens:

![Canary_token](https://github.com/sastry17/tokengrabber/blob/master/screenshots/Application.png )



