### Kano launcher

kano-launcher implements a poor man's container system on kernels where control groups
are not present, but namespaces are.

### Usage
kano-launcher <command> <preset>

kano-launcher is basically intended to run <command> (using system(2)).

If present, config files in ```/usr/share/kano-toolset/kano-launcher/conf/```
modify its behavior.

The optional argument ```<preset>``` helps identify a config file.

If the name of the config file exactly matches <preset> it is chosen.
Otherwise, any config file matching a substring of <command>  may match.

The following lines in the config file are allowed:

```
no_kill
extra_cmd: <cmd>
match_only_preset
```

 * match_only_preset causes a config file to match only if its filename matches the preset, not
   in the command.
 
If a matching config file is found, the command is 'containerised'. This means it, and
all processes it launches, are subject to being killed when a new kano-launch instance is run.
'no_kill' prevents a launched app from killing *other* launched apps (but not from itself
being killed).

if 'extra_cmd' is present, an additional command is run, as specified.


### Internals:

Internally, if an app is to be containerised it is launched with clone using CLONE_NEWUTS,
and a copy of ```/proc/<pid>/ns/uts``` is bind-mounted under ```~/.kano-app-containers```.
When an instance of kano-launcher decides to kill the other apps, it scans this directory and
kills any processes using one of the UTS namespaces used there, then removes the bind mount.

To do so, it uses a separate command kano-kill-ns. This is used as follows:
  ``` kano-kill-ns <signal> <inode> Pid1 Pid2 Pid3 ... ```

Which sends the signal <signal> to any of the pids listed which are in the UTS namespace
linked to <inode>

