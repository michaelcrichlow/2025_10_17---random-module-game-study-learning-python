import random

MATH_CONSTANTS = {
    # random starts with choice...
    "choice": "(function) Choose a random element from a non-empty sequence.",
    "choices": "(function) Returns a list with k randomly selected elements from the specified sequence. k can be larger than the length of the original list.",
    "gauss": "(function) Gaussian distribution.",
    "getrandbits": "(function) Returns an integer in the specified size (in bits).",
    "getstate": "(function) Return internal state; can be passed to setstate() later.",

    # all the rands
    "randbytes": "(function) Generate n random bytes.",
    "randint": "(function) Returns a random integer in range [a, b], including both end points. An alias for randrange(start, stop+1).",
    "random": "(function) Returns a random floating number between 0 and 1.",
    "randrange": "(function) Choose a random integer from range(stop) or range(start, stop[, step]).",

    # Just ike you have randrange you have sample seed...
    "sample": "(function) Returns a list with k randomly selected elements from the specified sequence. k cannot be larger than the length of the original list.",
    "seed": "(function) Initialize internal state from a seed.",
    "setstate": "(function) Restore internal state from object returned by getstate().",
    "shuffle": "(function) Shuffle list x in place, and return None.",
    "triangular": "(function) Triangular distribution.",
    "uniform": "(function) Returns a random floating number between the two specified numbers (both included). Can be thought of as 'randrange_float()'", 

    # Then you have the states
    "Random":"(class) Random number generator base class used by bound module functions.",
    "SystemRandom":"(class) Alternate random number generator using sources provided by the operating system (such as /dev/urandom on Unix or CryptGenRandom on Windows).",

    # Then you have all the variates. There are nine of them...
    "betavariate":"(function) Returns a random float number between 0 and 1 based on the Beta distribution.",
    "binomialvariate":"(function) Returns a random int that follows a binomial distribution",
    "expovariate":"(function) Returns a random float number based on the Exponential distribution.",
    "gammavariate":"(function) Returns a random float number based on the Gamma distribution.",
    "lognormvariate":"(function) Returns a random float number based on a log-normal distribution.",
    "normalvariate":"(function) Returns a random float number based on the normal distribution.",
    "paretovariate":"(function) Returns a random float number based on the Pareto distribution.",
    "vonmisesvariate":"(function) Returns a random float number based on the von Mises distribution.", 
    "weibullvariate":"(function) Returns a random float number based on the Weibull distribution.", 
}



def main():
    keys = list(MATH_CONSTANTS.keys())
    random.shuffle(keys)
    total = len(keys)
    count = 0

    for test_key in keys:
        user_key = input(f"\nDefine a function that returns the value for:\n→ {MATH_CONSTANTS[test_key]}\n→ ").strip()
        if user_key == test_key or (user_key == "math." + test_key):
            print("✅ Correct!")
            count += 1
        else:
            print(f"❌ Incorrect: Correct answer was '{test_key}'")

    print(f"\nAll done! You got {count} out of {total} correct.")

if __name__ == '__main__':
    main()


