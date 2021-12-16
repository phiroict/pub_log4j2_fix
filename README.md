# Mule patcher

A simple script that patches Mule anypoint studio, but it can be adapted for other projects as well. 
Mule seems to work after the patch though deep dives need to be done for each application. 

Note that the scala log4j drivers have not been patched yet. 

# Legal 

This is a quick and dirty tool, free to use and comes with NO WARRANTY at all. Use at your own risk!

# Usage 

## Stack 
- make 
- python 3.8+ 
- unzip

## Running 

Run first 
```bash
make init
```

This will download and unzip the 2.16 version of the log4j2 library that have been patched with 2 issues:
- CVE-2021-44228
- CVE-2021-45046


## Setup

In the patch_log4j.py 
Set the path to your Anypoint / Mule server dist. 

```python
source = "/mnt/c/AnypointStudio"
```

Make a copy of the folder for instance

```bash
cp -rpf  /mnt/c/AnypointStudio /mnt/c/OriginalAnypointStudio
```

Now check where the log4j jars are placed

```bash
make check
```
Make sure AnypointStudio or the mule server is shut down. When running these jars are in memory and patching will do something unpredictable. 
Then run 

```bash
make run 
```

Check if it were successful by: 

```bash
make check
```

If things went pear shaped: Restore with 

```bash
make restore
```
