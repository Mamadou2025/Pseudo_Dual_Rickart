from itertools import product

def gcd(x, y):
    """Computes the GCD of x and y with gcd(0,0) = 0"""
    while y != 0:
        x, y = y, x % y
    return abs(x) if x != 0 else 0

def is_endomorphism(f, M):
    """Checks if f preserves the GCD operation"""
    return all(f[gcd(x, y)] == gcd(f[x], f[y]) for x, y in product(M, repeat=2))

def is_idempotent(f, M):
    """Checks if f ∘ f = f"""
    return all(f[f[x]] == f[x] for x in M)

def direct_image(f, M):
    """Computes the direct image of f"""
    return {f[x] for x in M}

def extended_image(f, M):
    """Computes the closure of the image under GCD"""
    im_f = direct_image(f, M)
    return {y for y in M if any(gcd(y, f[x]) in im_f for x in M)}  # Fixed here

def kernel(f, M):
    """Computes the kernel of f (values x where f(x) = 0)"""
    return {x for x in M if f[x] == 0}

def generate_valid_functions(M):
    """Generates all valid endomorphism functions"""
    functions = []
    for f_vals in product(M, repeat=len(M)):
        f = dict(enumerate(f_vals))
        if f[0] == 0 and is_endomorphism(f, M):
            functions.append(f)
    return functions

def analyze_functions(M):
    """Displays analysis and checks the Dual weak Rickart property"""
    valid_functions = generate_valid_functions(M)
    idempotents = [g for g in valid_functions if is_idempotent(g, M)]
    
    # Display table
    print("\nFunction".ljust(15), "Idempotent".ljust(12), "Image".ljust(15), "Extended Image".ljust(18), "Kernel".ljust(15), "i-regular")
    print("-" * 85)
    
    for f in valid_functions:
        f_tuple = tuple(f[i] for i in sorted(M))
        im = direct_image(f, M)
        im_et = extended_image(f, M)
        ker = kernel(f, M)
        
        line = f"{str(f_tuple).ljust(15)} | "
        line += f"{'Yes' if is_idempotent(f, M) else 'No'.ljust(10)} | "
        line += f"{str(im).ljust(13)} | "
        line += f"{str(im_et).ljust(16)} | "
        line += f"{str(ker).ljust(13)} | "
        line += "Yes" if im != im_et else "No"
        print(line)
    
    # Check Dual weak Rickart property
    is_dual_weak_rickart = True
    for f in valid_functions:
        im_et_f = extended_image(f, M)
        # Check if there exists an idempotent g such that im_et_f = kernel(g)
        condition = any(im_et_f == kernel(g, M) for g in idempotents)
        if not condition:
            is_dual_weak_rickart = False
            break
    
    print("\nFinal Result:")
    print("M is Dual weak Rickart :", "Yes" if is_dual_weak_rickart else "No")

# Example usage
n = 2  # Modify n here
M = list(range(n + 1))
analyze_functions(M)
