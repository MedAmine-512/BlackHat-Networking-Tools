import subprocess
import shlex


def execute(cmd):
    cmd = cmd.strip()
    cmd =  shlex.split(cmd)
    output = subprocess.check_output(cmd,stderr= subprocess.STDOUT)

    return output.decode()

    pass


if __name__ == '__main__':

    



    pass