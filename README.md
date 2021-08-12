Winver recreation for Linux

# Screenshots #
* GUI mode
If there's no image for your distro, the program will put Tux instead. 
<br> ![alt text](https://github.com/BrenoMartinsDeOliveiraVasconcelos/linver/blob/main/screenshots/example.png?raw=true)
* Command Line mode
<br> ![alt text](https://github.com/BrenoMartinsDeOliveiraVasconcelos/linver/blob/main/screenshots/sampleclm.png?raw=true)

# Running it #
This program uses tkinter, some distros doesn't have it installed by defult. There is how to install it:
### Debian/Ubuntu (or based) ###
sudo apt install python3-tk

### Arch or based ###
sudo pacman -Sy python3-tk

### Other ###
See the apropriated documentation for details

After installing tkinter, install python3-pip if it is not installed
### Debian/Ubuntu (or based) ###
sudo apt install python3-pip

### Arch or based ###
sudo pacman -Sy python3-pip

### Other ###
See the apropriate documentation for details

Then do:

python3 -m pip install -r requeriments.txt && python3 linver.py

# Arguments #
You can run using arguments to modify how the program will work
* --distro [Name]
Will change distro name, useful to test new images
* --clmode
WIll run the command line version

# Adding new images for not listed distros or change existing distro images #
To add new images or change distro images, the image needs to follow these rules to the modification work propely:
* The image needs to be in PNG format
* Size between 300x300 and 600x600 (Recommended)

## How to add an image ##
<br> 1 - Go to "assets" folder
<br> 2 - Put your image in there with the name displayed on the first line of the program
<br> 2.1 - Replace spaces with _ and slashes with -
<br> 3 - Run the program to see if everything works fine

