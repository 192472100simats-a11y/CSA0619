import time


# Function to create LPS array for KMP Algorithm
def compute_lps(pattern):
    length = 0
    lps = [0] * len(pattern)

    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


# KMP Pattern Matching Function
def kmp_search(text, pattern):

    positions = []

    lps = compute_lps(pattern)

    i = 0
    j = 0

    while i < len(text):

        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            positions.append(i - j)
            j = lps[j - 1]

        elif i < len(text) and pattern[j] != text[i]:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions


# Main Program

network_traffic = """
Normal network request received.
User login successful.
GET /home HTTP/1.1

Normal traffic continues.

ATTACK_SQL_INJECTION detected in request.

More normal network traffic.

MALWARE_DOWNLOAD detected from suspicious server.

Normal packet received.

ATTACK_SQL_INJECTION found again.

DDOS_ATTACK detected from multiple connections.

Normal traffic completed.
"""


malicious_patterns = [
    "ATTACK_SQL_INJECTION",
    "MALWARE_DOWNLOAD",
    "DDOS_ATTACK"
]


print("CYBERSECURITY THREAT DETECTION SYSTEM")
print("-" * 45)

start_time = time.perf_counter()

total_threats = 0

for pattern in malicious_patterns:

    positions = kmp_search(network_traffic, pattern)

    if positions:

        print("\nThreat Detected:", pattern)
        print("Number of Occurrences:", len(positions))
        print("Positions:", positions)

        total_threats += len(positions)

    else:
        print("\nNo Threat Found:", pattern)


end_time = time.perf_counter()

execution_time = end_time - start_time


print("\n" + "-" * 45)
print("PERFORMANCE RESULTS")
print("-" * 45)

print("Total Threats Detected:", total_threats)
print("Network Traffic Size:", len(network_traffic), "characters")
print("Patterns Checked:", len(malicious_patterns))
print("Execution Time:", execution_time, "seconds")

print("\nThreat Detection Completed Successfully.")
