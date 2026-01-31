import platform
import sys

def main():
    if platform.architecture()[0] == "64bit":
        import forget1_XD
        forget1_XD.approval()
    else:
        print("32bit Not Supported! Sorry")
        sys.exit(1)

if __name__ == "__main__":
    main()

