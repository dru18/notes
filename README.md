# notes

## My notes for solving my tasks.

* Search all the files ( listed in source directory ) in destination directory.

```for f in $(ls $1); do ls -a $2 | grep $f; done;```

* Using last command with different argument


```
cp ~/Pictures/error.png issue/screenshot/```
		
^error^solved^
```

* [Look](https://github.com/dru18/notes/blob/master/cylinder_volume.py) Cylinder volume program shows args and colored example for python3

* [Look](https://github.com/dru18/notes/wiki/Recover-password) How to recover the password for the Linux and Windows.

## Exclude

* 10.0.0.0/8

* 192.168.0.0/16

* 172.16.0.0/12

> Exclude these port rang from masscan and nmap in python scripts to avoid unnecessary scans.

