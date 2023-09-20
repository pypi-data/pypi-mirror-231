from wrapper import run_go_binary

def test_running_go_binary():
    out = run_go_binary()
    assert out == 'Hello from Go!\n'

if __name__ == "__main__":
    test_running_go_binary()
    print("Everything passed")