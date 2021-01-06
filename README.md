# drive_profiler
a simple script to walk down a directory structure and identify storage size for each folder

gets the size of all files (files only, not subfolders) in each folder starting in a defined directory

### command line use:
```
$ python profile_drive.py --path <path_to_profile>
```

### output:
A CSV file with a filename "profile_results_YYYY-MM-DD_HH.mm.SSAM/PM.csv" will be saved to the top level of the directory that was profiled  
The rows will be ordered by the folder size, with the largest folder at the top  
Columns in the output folder are:  
* fullpath: the full path to the folder
* foldername: the name of the folder
* size_bytes: the size of all files in the folder (not counting subfolders) in bytes
* size_kb: the size of all files in the folder (not counting subfolders) in kilobytes
* size_mb: the size of all files in the folder (not counting subfolders) in megabytes
* size_gb: the size of all files in the folder (not counting subfolders) in gigabytes
