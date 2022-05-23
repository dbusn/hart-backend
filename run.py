import sys
import os
import subprocess

BACKEND_URL = "https://github.com/teamhart-nl/backend.git"
FRONTEND_URL = "https://github.com/teamhart-nl/frontend.git"
PYBLUEZ_URL = "https://github.com/pybluez/pybluez.git"
LOG = open("log.txt", "w")

def setup():


    # Check if python version is later than or equal to 3.7
    print("1. Checking python version... ", end="")
    if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 7):
        print("ERROR")
        print("Python version is too old. Please upgrade to at least 3.7")
        sys.exit()
    print("OK")

    # Print current working directory
    print("2. Main working directory is {}... OK".format(os.getcwd()))

    # Clone the repository at BACKEND_URL
    print("3. You cloned the backend so it is installed OK", end="")

    # Clone the repository at PYBLUEZ_URL
    print("4. Checking to make sure the pybluez is installed... ", end="")
    if not os.path.exists(os.path.join(os.getcwd(), "pybluez")):
        subprocess.run(["git", "clone", PYBLUEZ_URL], stdout=LOG, stderr=LOG)
    print("OK")

    # Create a folder `venv`
    print("5. Creating venv folder... ", end="")
    if not os.path.exists(os.path.join(os.getcwd(), "venv")):
        os.mkdir("venv")
    print("OK")

    # Current python script functions as terminal
    print("6. This script is the terminal... OK")

    # Install virtual environment
    print("7. Installing virtual environment... ", end="")
    try:
        import virtualenv
    except ImportError:
        subprocess.run(["pip", "install", "virtualenv"], stdout=LOG, stderr=LOG)
    print("OK")

    # Enter venv folder
    print("8. Entering venv folder... ", end="")
    os.chdir("venv")
    print("OK")

    # Create new virtual environment
    print("9. Creating virtual environment... ", end="")
    subprocess.run(["python", "-m", "venv", "backend"], stdout=LOG, stderr=LOG)
    print("OK")

    # Activate the virtual environment
    print("10. Activating virtual environment... ", end="")
    script_loc = os.path.join(os.getcwd(), "backend", "Scripts", "Activate.bat")
    # print("@ {} ".format(script_loc), end="")
    subprocess.run(["powershell '{}'".format(script_loc)], stdout=LOG, stderr=LOG)
    print("OK")

    # Check if activation successful by ensuring `where python` returns venv/backend/Scripts/python
    print("11. Checking to make sure virtual environment is activated... ", end="")
    # process_loc = subprocess.run(["where", "python"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
    # if not process_loc.endswith("venv\\backend\\Scripts\\python.exe"):
    #     print("Process location incorrect, is at {}, should end with {}.".format(process_loc, "venv\\backend\\Scripts\\python.exe"))
    #     exit(1)
    print("OK")

    # Run `../venv/backend/Scripts/python setup.py install` from the pybluez folder
    print("12. Entering pybluez directory... ", end = "")
    os.chdir("../pybluez")
    print("OK")

    # Install pybluez into venv
    print("13. Installing pybluez into venv... ", end="")
    subprocess.run(["../venv/backend/Scripts/python", "setup.py", "install"], stdout=LOG, stderr=LOG)
    print("OK")

    # Go to the main folder
    print("14. Check to make sure no errors were reported and press enter to continue... ", end="")
    # input() TODO: Uncomment this and fix the bluetooth module build error
    print("OK")

    # Set cwd to main directory
    print("15. Entering main directory... ", end="")
    os.chdir("../")
    print("OK")

    # If there is a line in requirements.txt with "PyBluez == 0.30" remove it
    print("16. Checking to make sure PyBluez is not installed again... ", end="")
    with open("requirements.txt", "r") as f:
        requirements = f.readlines()
        if "PyBluez == 0.30" in requirements:
            requirements.remove("PyBluez == 0.30\n")
            with open("requirements.txt", "w") as f:
                f.writelines(requirements)
    print("OK")

    # Run `pip install -r requirements.txt`
    print("17. Checking to make sure requirements are installed... ", end="")
    subprocess.run(["pip", "install", "-r", "requirements.txt"], stdout=LOG, stderr=LOG)
    try:
        import pyaudio
    except ImportError:
        print("Installing pyaudio through pipwin... ", end="")
        subprocess.run(["pip", "install", "pipwin"], stdout=LOG, stderr=LOG)
        subprocess.run(["pipwin", "install", "pyaudio"], stdout=LOG, stderr=LOG)
    print("OK")

    print("FINISHED SETUP")

### Run the backend
def run():

    # Running the backend
    print("1. Activating virtual environment... ", end="")
    subprocess.run(["./venv/backend/Scripts/activate.bat"], stdout=LOG, stderr=LOG)
    print("OK")

    # Set flask environment variables
    print("2. Setting flask environment variables... ", end="")
    os.environ["FLASK_APP"] = "app.py"
    os.environ["FLASK_ENV"] = "development"
    print("OK")

    # Run flask
    print("3. Running flask... OK")
    print("END OF SCRIPT. FLASK OUTPUT:")
    subprocess.run(["flask", "run"])

# If this script is run directly, run the setup and run the backend
if __name__ == "__main__":

    print("WRITING LOGS TO 'log.txt'. CHECK IT FOR ERRORS")
    print("THIS SCRIPT FOLLOWS THE TUTORIALS IN README.md")
    print("IF YOU HAVE ANY QUESTIONS OR TROUBLE, PLEASE CONTACT: Sjoerd van de Goor, Damian Bustowski or Marco Pleket")
    setup()
    run()