import subprocess
import sys

def get_cpuid_output():
    """
    Get CPUID output for leaf 7
    """
    try:
        cmd = ['./amx_detection.exe']
        process = subprocess.run(cmd, capture_output=True, text=True)
        
        if process.returncode != 0:
            print(f"Error running app: {process.stderr}")
            return None
            
        return process.stdout
        
    except FileNotFoundError:
        print("Error: 'amx_detection' command not found. Please check if exe is in the same directory.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def check_amx_support(output):
    """
    Check AMX support by looking for specific feature strings
    """
    if not output:
        return None
        
    # Initialize features dictionary
    features = {
        'amx_bf16'    : False,
        'amx_tile'    : False,
        'amx_int8'    : False,
	'amx_state' : False
    }
    
    # Look for AMX-related strings in the output
    for line in output.split('\n'):
        line = line.strip()
        if "CPUID.07H.00H:EDX[22]" in line:
            features['amx_bf16'] = "1" in line
        elif "CPUID.07H.00H:EDX[24]" in line:
            features['amx_tile'] = "1" in line
        elif "CPUID.07H.00H:EDX[25]" in line:
            features['amx_int8'] = "1" in line

        if "AMX State" in line:
            features['amx_state'] = "AMX State is supported" in line
    
    return features

def main():
    print("Checking AMX support...")
    
    # Get CPUID output
    output = get_cpuid_output()
    if not output:
        sys.exit(1)
    
    # Check AMX support
    result = check_amx_support(output)
    if result is None:
        print("Error checking AMX support")
        sys.exit(1)
    
    # Print results
    print("\nAMX Support Status:")
    print(f"AMX-TILE (Tile Architecture):  {'Yes' if result['amx_tile'] else 'No'}")
    print(f"AMX-BF16 (BFloat16):           {'Yes' if result['amx_bf16'] else 'No'}")
    print(f"AMX-INT8 (8-bit Integer):      {'Yes' if result['amx_int8'] else 'No'}")
    print(f"AMX State enabled by OS:       {'Yes' if result['amx_state'] else 'No'}")
    
    # Overall AMX support
    amx_supported = all([result['amx_tile'], result['amx_bf16'], result['amx_int8']])
    print(f"\nAMX Support in Platform: {'Yes' if amx_supported else 'No'}")
    amx_state_supported = result['amx_state']
    print(f"\nAMX Support in OS: {'Yes' if amx_state_supported else 'No'}")
    
    if amx_supported:
        print("\nYour CPU supports all AMX features!")
        print("This includes:")
        print("- Tile Architecture (AMX-TILE)")
        print("- BFloat16 Operations (AMX-BF16)")
        print("- 8-bit Integer Operations (AMX-INT8)")
        print("- AMX State by OS")

if __name__ == "__main__":
    main()
