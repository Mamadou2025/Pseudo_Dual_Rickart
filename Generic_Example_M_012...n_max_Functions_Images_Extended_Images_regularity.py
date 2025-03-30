from itertools import product

def is_endomorphism(f, M):
    """Check if f preserves the max operation of the join-semilattice."""
    return all(f[max(x, y)] == max(f[x], f[y]) for x, y in product(M, repeat=2))

def direct_image(f, M):
    """Compute the direct image of f."""
    return {f[x] for x in M}

def extended_image(f, M):
    """Compute the extended image via max closure."""
    im_f = direct_image(f, M)
    return {y for y in M if any(max(y, f[x]) in im_f for x in M)}

def generate_endomorphisms(n):
    """Generate all endomorphism functions for M = {0, 1, ..., n}."""
    M = list(range(n + 1))
    results = []
    
    # Generate all possible functions f: M → M
    for f_vals in product(M, repeat=len(M)):
        f = dict(enumerate(f_vals))
        
        # Filter: f(0) = 0 and check endomorphism
        if f[0] == 0 and is_endomorphism(f, M):
            im_f = direct_image(f, M)
            ext_im = extended_image(f, M)
            results.append({
                'function': f_vals,
                'image': im_f,
                'extended_image': ext_im,
                'irregular': im_f != ext_im
            })
    
    return results

def display_results(n):
    """Display formatted analysis results."""
    results = generate_endomorphisms(n)
    M = list(range(n + 1))
    
    print(f"\nAnalysis for M = {M} (n = {n})")
    print("{:<15} | {:<12} | {:<16} | {}".format(
        "Function", "Image", "Extended Image", "i-irregular"))
    print("-" * 52)
    
    for res in results:
        f_str = str(res['function']).ljust(15)
        im_str = str(res['image']).ljust(12)
        ext_im_str = str(res['extended_image']).ljust(16)
        irr_str = "Yes" if res['irregular'] else "No"
        print(f"{f_str} | {im_str} | {ext_im_str} | {irr_str}")

# Example usage
display_results(2)  # Original version with n=2
display_results(2)  # Generalized version with n=2