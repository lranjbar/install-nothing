import argparse

def hello(string):
    print("Hello, " + string + "!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hello From Python!")
    parser.add_argument("--name", action="store", help="Enter your name to say hello.", default="World")
    args = parser.parse_args()
    hello(args.name)