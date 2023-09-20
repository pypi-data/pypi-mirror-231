# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['udevbackup']

package_data = \
{'': ['*']}

install_requires = \
['google-speech>=1.2,<2.0', 'systemlogger>=0.1,<0.2', 'termcolor>=2.3,<3.0']

setup_kwargs = {
    'name': 'udevbackup',
    'version': '1.2.1',
    'description': 'detects when specified storage devices are connected, mounts them, executes a script, umounts them and tells when it is done.',
    'long_description': 'UdevBackup\n==========\n\nOn Linux, detects when specified storage devices are connected, then mounts them,\nexecutes a script, unmounts them and tells when it is done (using mail or text to speech).\n\nA config file defines storage devices and the scripts to run.\n\nI wrote this script for a simple offline backup of my server: I just have to turn\nthe external USB drive on and wait for the message (using text to speech) before\nturning it off again. UdevBackup double forks before running the script, so\nthere is no timeout problem with udev and slow scripts.\n\nRequire the "at" utility for running long jobs (more than 30 seconds).\n\ninstallation\n------------\n\n    sudo pip3 install udevbackup --upgrade\n\nyou need to create a udev rule to launch udevbackup when a new device (with a file system) is connected:\n\n    echo \'ACTION=="add", ENV{DEVTYPE}=="partition", RUN+="/usr/local/bin/udevbackup at"\' | sudo tee /etc/udev/rules.d/udevbackup.rules\n    udevadm control --reload-rules\n\nIf you only have short jobs, you can use\n\n    echo \'ACTION=="add", ENV{DEVTYPE}=="partition", RUN+="/usr/local/bin/udevbackup run"\' | sudo tee /etc/udev/rules.d/udevbackup.rules\n    udevadm control --reload-rules\n\nconfiguration\n-------------\n\nCreate a .ini config file with a "main" section for global options, and another section for each\ntarget partition. The name is not important. All .ini files in /etc/udevbackup are read.\nThese files must use the UTF-8 encoding.\n\nYou can display all available options with the "help" command, but .\n\n    udevbackup help\n\n    Create one or more .ini files in /etc/udevbackup.\n    Yellow lines are mandatory.\n    [main]\n    smtp_auth_user = SMTP user. Default to "".\n    smtp_auth_password = SMTP password. Default to "".\n    smtp_server = SMTP server. Default to "localhost".\n    smtp_from_email = Recipient of the e-mail.  Default to "".\n    smtp_to_email = E-mail address for the FROM: value. Default to "".\n    use_speech = Use google speech for announcing successes and failures. Default to 0.\n    use_stdout = Display messages on stdout. Default to 0.\n    use_smtp = Send messages by email (with the whole content of stdout/stderr of your scripts). Default to 0.\n    smtp_use_tls = Use TLS (smtps) for emails. Default to 0.\n    smtp_use_starttls = Use STARTTLS for emails. Default to 0.\n    smtp_smtp_port = The SMTP port. Default to 25.\n\n    [example]\n    fs_uuid = UUID of the used file system. Check /dev/disk/by-uuid/ before and after having connected your disk to get it.\n    command = Command to call for running the script (whose name is passed as first argument). Default to "bash".\n    script = Content of the script to execute when the disk is mounted. Current working dir is the mounted directory. This script will be copied in a temporary file, whose name is passed to the command.\n    stdout = Write stdout to this filename.\n    stderr = Write stderr to this filename.\n    mount_options = Extra mount options. Default to "".\n    user = User used for running the script and mounting the disk.Default to "current user".\n    pre_script = Script to run before mounting the disk. The disk will not be mounted if this script does not returns 0. Default to "".\n    post_script = Script to run after the disk umount. Only run if the disk was mounted. Default to "".\n\nHere is a complete example:\n\n    cat /etc/udevbackup/example.ini\n    [main]\n    smtp_auth_user = user\n    smtp_auth_password = s3cr3tP@ssw0rd\n    smtp_server = localhost\n    use_speech = 1\n    use_stdout = 0\n    use_smtp = 1\n\n    [example]\n    fs_uuid = 58EE-7CAE\n    script = mkdir -p ./data\n        rsync -av /data/to_backup/ ./data/\n\nYou can display the current config:\n\n    udevbackup show\n',
    'author': 'Matthieu Gallet',
    'author_email': 'github@19pouces.net',
    'maintainer': 'Matthieu Gallet',
    'maintainer_email': 'github@19pouces.net',
    'url': 'https://github.com/d9pouces/udevbackup',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
