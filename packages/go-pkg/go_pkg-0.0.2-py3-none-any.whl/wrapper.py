import subprocess

def run_go_binary():
    try:
        result = subprocess.check_output(['./binary'])
        decoded_result = result.decode('utf-8')
        return decoded_result
    except subprocess.CalledProcessError as e:
        print(f'Error: Go binary returned non-zero exit code {e.returncode}')

if __name__ == '__main__':
    run_go_binary()
