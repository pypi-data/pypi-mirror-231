#!/usr/bin/env python3
import os
import sys
import pathlib
import shutil
import subprocess
import tempfile

def main():
    print("-- Starting installation of PhotoLibDownloader.")
    print("-- This will take a minute or two. Please be patient ...")
    print("----------------------------------------")

    theLib = pathlib.Path(__file__).parent.resolve()
    theDir = tempfile.mkdtemp()

    print("-- Step 1 of 4: Installing preliminary requirements ...")

    subprocess.check_call([sys.executable,
                           "-m", "pip", "install", '--upgrade', '--quiet', 'pip'])
    subprocess.check_call([sys.executable,
                           "-m", "pip", "install", '--upgrade', '--quiet', 'pyinstaller'])

    theWhl = None
    theName = None
    for d in pathlib.Path(theLib).glob('*.whl'):
        theWhl = str(d.resolve())
        theName = d.name.split('-')[0]
        break

    if theWhl is None: exit(1)
    print("-- Step 2 of 4: Downloading program scripts and dependencies. Please wait ...")

    subprocess.check_call([sys.executable,
                           "-m", "pip", "install", '--target', theDir, '--quiet', theWhl])

    theSubDir = theDir + "/" + theName
    theIcon = theSubDir + "/Paomedia_Small_N_Flat_Cloud_down.icns"
    theData = theIcon + ":."

    if not pathlib.Path(theIcon).exists: exit(1)
    print("-- Step 3 of 4: Compiling PhotoLibDownloader app. This may take a minute ...")

    os.chdir(theDir)
    subprocess.check_call([sys.executable, "-m", "PyInstaller",
                           "--paths", theDir,
                           "--paths", theSubDir,
                           "--add-data", theData,
                           "--icon", theIcon,
                           "--name", theName,
                           "--onedir", "--windowed",
                           "--log-level", "ERROR",
                           theName + "/main.py"
                           ])

    theAppSource = pathlib.Path(theDir + "/dist/" + theName + ".app")

    if not pathlib.Path(theAppSource).exists: exit(1)
    print("-- Step 4 of 4: Moving PhotoLibDownloader to the ~/Applications folder")

    theAppDir = pathlib.Path('~/Applications').expanduser()
    if not theAppDir.exists():
        pathlib.Path.mkdir(theAppDir)
    theAppDir = str(theAppDir)

    theAppTarget = pathlib.Path(theAppDir + "/" + theName + ".app")

    if theAppSource.exists():
        if theAppTarget.exists():
            shutil.rmtree(theAppTarget)
        shutil.copytree(theAppSource, theAppTarget)

    if theAppTarget.exists():
        subprocess.Popen(['/usr/bin/open', str(theAppDir)])

        theSymlink = pathlib.Path('~/Desktop/' + theName).expanduser()
        if theSymlink.exists():
            theSymlink.unlink(True)
        theSymlink.symlink_to(theAppTarget)

    print("----------------------------------------")
    print("-- PhotoDownloader app has been installed and can be found in")
    print("-- " + str(theAppTarget) )
    print("-- There is also an icon on your desktop")
    print("")
    print("-- Installation finished. This window can be closed.")

if __name__ == '__main__':
    main()
