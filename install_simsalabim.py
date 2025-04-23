import os

from pySIMsalabim.install.get_SIMsalabim import install_SIMsalabim


def main():
    fpc_path = "/path/to/fpc/bin/x86_64-linux" # Change this to the actual path where fpc is installed
    if not os.path.exists(fpc_path):
        print("No Free Pascal Compiler (FPC) found at the specified path. Trying to run installation without it. FPC might be installed during the installation of SIMsalabim.")

    original_path = os.getenv("PATH", "")
    combined_path = f"{fpc_path}{os.pathsep}{original_path}"
    os.environ["PATH"] = combined_path

    cwd = os.getcwd()
    install_SIMsalabim(cwd)

if __name__ == "__main__":
    main()

