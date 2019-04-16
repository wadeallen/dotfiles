#!/bin/bash

# Make sure that fstab has been setup
echo "Make sure that you have added the following to the /etc/fstab file and have rebooted"
echo "UUID=120f16fd-17fe-42a8-948b-1444531dd58c     /mnt/msata   ext4   defaults    0  0"
echo "The external drive should now be mounted at /mnt/msata"
echo "Once you have rebooted, continue with the script"

printf "Press any key to continue or 'CTRL+C' to exit : "
(tty_state=$(stty -g)
stty -icanon
LC_ALL=C dd bs=1 count=1 >/dev/null 2>&1
stty "$tty_state"
) </dev/tty

function dir {
	# Make sure that drive is not linked before adding link
	cd $HOME
	dir="$1"
	# if directory exists and is not a symlink
	if [ -d $dir ] && [ ! -L $dir ]; then
	  rm -Rf $dir
	  ln -s /mnt/msata/$dir $dir
	  echo "$dir exists and is not a symlink, removed $dir and added $dir as symblink"
	# if not a directory but is already a symblink
	elif [ -L $dir ]; then
	  echo "$dir is already linked"
	# if no directory or symlink in place
	else
	  ln -s /mnt/msata/$dir $dir
	  echo "added $dir as symlink"
	fi
	}

dir Documents
dir dotfiles
dir Downloads
dir Editing
dir Music
dir Pictures
dir Print
dir Scans
dir Sites
dir Videos
dir .config/fish
dir .config/syncthing

