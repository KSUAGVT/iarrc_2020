# Kennesaw State University Autonomous Ground Vehicle Team

1. How to set-up your GitHub account so that you can collaborate on this repository
2. How to set-up your development environment on your personal computer

## Setting up GitHub

All members of AGVT need to create a personal GitHub account tied to an easily accessible email. It does not have to be a student email, as the work done here can be used as a portion of your "coding portfolio" for use after you graduate.

Students need to have GitHub accounts in order to have modification access to the codebase. They also need to be manually added as a collaborator by the current Software Lead.

Students who are not collaborators should either DM the Software Lead in the Discord Server, or should post in in the #General Sofware channel, tagging the Software Lead.

Once added, it is recommended that students create an ssh key that permits the specific computer you are using access to your GitHub account from the command line. That will be discussed later

## Setting up your Development Environment 

All of the machines that exist on the vehicle currently run Ubuntu 18.04 LTS. Thus, it is recommended that you develop code in a similar environment.

There are many options, Listed from best to worst in terms of performance:

1. Dual Boot / Full Up Ubuntu 18.04 LTS Installation
2. Windows 10 Ubuntu 18.04 Kernel 
3. Ubuntu 18.04 Docker container
4. Ubuntu 18.04 Virtual Machine

### Full Ubuntu Installation

When it comes to running an operating system, the most efficent form is when the OS you intend to develop on is the only OS running on the entire machine. This can be done by either using Ubuntu 18.04 LTS as your only operating system on your computer, or by a much more popular method, having both Windows and Ubuntu exist on your machine.

The latter, refered to as Dual Booting, is easy to setup if you are able to have a single hard driver per operating system, however can be hard for newcomers if their PC only has a single hard drive. 

### Windows 10 Ubuntu Kernel

If you have a Windows 10 Installation on your current PC, this is the recommendation AGVT gives for developing Linux based programs on your machine. 

In short, an Operating System's kernel is the minimum set of drivers and required software that allow the operating system to interface with your hardware. This means it is much more lightweight than running a virtual machine, and will experience leaps better performance.

First, download the Ubuntu software package from the microsoft store [here](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab)

Once that is installed, open WindowsPowershell as administrator and run the following command:

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

The terminal will prompt you to restart your computer.

Once restarted, anytime you wish to launch the Ubuntu kernel for you to develop in, search for "Ubuntu" in the start menu.

When you first run Ubuntu, it will perform a setup process, where it will ask for you to create a UNIX username and UNIX password. These are for the local user that is being run inside ubuntu, and are seperate from windows, so make sure you write down what you use for it.

Once complete, you'll be brought to the home directory of the user you created in a bash prompt, where you can follow any Ubuntu development instructions or tutorials as usual.

### Docker Container

Before Windows 10 offered an Ubuntu kernel to run, docker was the industry standard method to do the same exact approach. 

Docker is much more configurable than the windows offering, but can only be run on Windows 10 Pro machines due to virtualization of hardware that only Pro offers. Thus, it is most likely not the solution for AGVT.

### Virtual Machine

If all else fails, a virtual machine, while slow, will allow you to develop in Ubuntu. This will run the entire Ubuntu Operating System, including all of the visualzations and user interaction software, all in an emulated environment, and as a result will perform very slow. 

There is a plethora of doccumentation of how to setup an "Ubuntu 18.04 Virtual Machine", and any resource you find should do the trick.

# The rest of the readme is to be done in the format of ubuntu you chose

## Setting up GitHub SSH Key

It is highly recommended you utilize a GitHub ssh key for interfacing with the repository. It prevents you from having to type your username and password any time you wish to make a change, primarily.

This can be done using the following commands:

```
ssh-keygen -t rsa -b 4086 -C "<your_emal_here@domain.com>"
```

replace the `<your_email_here@domain.com>` with your github account's email. Make sure the email is still in double quotes.

The command will prompt you to enter a file to save the key. Press Enter to accept the default location.

It will then ask you for a password for the sshkey. While you can use a password, it is not required for this repository that you do so, so feel free to press enter twice to have no password on your ssh key.

Once you've done that, add the generated ssh-key to the list of keys on your system with the following command:

```
ssh-add ~/.ssh/id_rsa
```

Finally, you need to add this key to the list of registered keys on your github account. First, navigate to your user settings in github. Find the "SSH and GPG keys" tab, then click "Add SSH Key". A Dialog popup will display, asking for a name (use any name you want, its the one tied to the current computer your adding), and the key itself. 

To get the key, it is recommended that you open the file the key is stored in with a text editor (nano will be the example here) and copy it so that you can paste it into the dialog box.

```
nano ~/.ssh/id_rsa.pub
```

This will open up a text editor called nano. simply select the text of the entire file using your mouse, then use the keyboard shortcut `ctrl + c`. Paste that entire result as the key and add it to your account.

## Getting the Repository

Once you have addeed the ssh key to your account, you will be able to download the repository onto your local machine. This can be done by first, going into the directory that you wish for the project to exis, then running the following command:

```
git clone https://github.com/KSUAGVT/iarrc_2020.git
```

This will download the repository onto your computer in a folder named iarrc_2020 in the directory you are currently in. 

## Installing Required Software

As of now, the following software packages need to be installed:

1. Pip3
2. OpenCV
3. numpy
4. matplotlib

They can be instlled from the following commands:

### Pip3

```
sudo apt update
sudo apt install python3-pip
```

### OpenCV

```
sudo apt update
sudo apt install python3-opencv
```

### numpy

```
python3 -m pip install numpy
```

### matplotlib

```
python3 -m pip install matplotlib
```

This set of software should be all you need to run code. Any GUI's that are created as a result of the code, however, need extra software on the windows machine in order to handle them

## Installing an X-Server

[X-Ming](https://sourceforge.net/projects/xming/) Is software that allows ubuntu GUI to be sent from the kernel to display on the windows machine's monitor. X-Ming is generally regarded by the community as the best option for this type of work.

Once installed, you need to have it running in the background while you do any development in your linux kernel in order to view guis created by the kernel. 

Make sure to accept the request for X-Ming to have access to the local network traffic, as that is how it communicates in the backend with the linux kernel.

Once that is running, simply run the following command:

```
echo "export DISPLAY=:0" >> ~/.bashrc
. ~/.bashrc
```


