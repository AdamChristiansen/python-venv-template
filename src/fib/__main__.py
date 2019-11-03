import argparse
from colored import fg, attr
import random
import sys

import fib

p = argparse.ArgumentParser(description="Compute Fibonacci numbers")
p.add_argument("number", metavar="n", type=int,
        help="The Fibonnaci number to compute")
p.add_argument("-s", "--seq", action="store_true",
        help="Generate the full sequence")
p.add_argument("-d", "--delim", action="store", type=str, default="\n",
        help="The sequence delimeter")
p.add_argument("-c", "--color", choices=["always", "auto", "never"],
        action="store", default="auto", help="Set color output")
p.add_argument("-r", "--no-color", action="store_true",
        help="Disable color output")
args = p.parse_args()

if args.number < 0:
    print("number must be non-negative", file=sys.stderr)

def p(f, i=None):
    """
    Print a Fibonacci number with a specified color index. This function
    determines whether or not color should be used.
    """
    if args.color == "always" or (args.color == "auto" and sys.stdout.isatty()):
        if i is None:
            i = random.randint(1, 6)
        color = fg(i % 6 + 1)
        reset = attr("reset")
        print(f"{color}{f}{reset}", end="")
    else:
        print(f"{f}", end="")

# Print the sequence/number
if args.seq:
    for i, f in enumerate(fib.fib_seq(args.number)):
        p(f, i)
        # Don't print the delimeter on the last item
        if i < args.number - 1:
            print(args.delim, end="")
else:
    p(fib.fib(args.number))
# Print the newline at the end
print()
