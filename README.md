
# Folder Synchronization

This project is created create a backup folder that will be sincronized to the Sorce Folder ddepending on user input


## Tech Stack

**Programming Language** Python

**Libraries** time, datetime, os, shutil


## Usage/Examples

The program is designed to create a "Source" folder, a "Replica" folder, and a "Log" file.
In the first phase, the user must enter the path of each element mentioned above, if in the destination folder there is already a "Source" folder or a "Replica" folder they will not be created and will be used the existing ones.

In case of creation, the respective information will be shown in the console and logged in the "Log" file.

In the second phase, the user must enter the unit of measurement of time:

•	Seconds

•	Minutes

•	Hours

•	Days

Depending on the unit of measurement and the quantity inserted, the program calculates a time interval between each synchronization.

Finally, the third part consists of two components:

•	In the first part, the items in the "Source" folder are copied to the "Replica" folder, each copied file is displayed in the console and logged in the log file

•	In the second part, the files in the "Replica" folder are deleted if they are not in the "Source" folder, each deleted file is displayed in the console and logged in the log file

Finally, the program is designed to wait for the end of the previously calculated time interval to repeat the third part
Both actions are in one direction "Source" -> "Replica" so if a file is deleted from the "Replica" folder it will be copied again from the "Source" folder

## Run Locally

Clone the project

```bash
  git clone https://github.com/OMarius97/Folder_Synchronization
```
## Authors

- [@Marius](https://www.github.com/OMarius97)


## Feedback

If you have any feedback, please reach out to me at mariusoana1997@gmail.com

