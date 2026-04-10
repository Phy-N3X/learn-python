# ============================================================
# MODULE 01 | PROJECT 01 - DNA Analysis Suite
# ============================================================
# Difficulty  : ⭐⭐⭐⭐ (Hard)
# Covers      : ALL topics from Module 01
#               Variables, Numbers, Strings, Booleans,
#               Print, Input, Comments, Math, Comparisons,
#               Logical operators, Type conversion, F-strings
# Estimated   : 3-5 hours
# ============================================================
#
# OVERVIEW:
# You will build a complete DNA Analysis Suite - a command-line
# tool that analyzes DNA sequences. It uses REAL concepts from
# bioinformatics and covers EVERY topic from Module 01.
#
# The program has 10 analysis modules, each testing different
# Python skills you learned in this module.
# ============================================================


import math
import datetime


# ============================================================
# SECTION 1: CONFIGURATION AND CONSTANTS
# ============================================================
# Tests: variables, type conversion, comments, f-strings

# --- Program metadata ---
PROGRAM_NAME    = "DNA Analysis Suite"
VERSION         = "1.0.0"
AUTHOR          = "Your Name"
RELEASE_DATE    = "2025-01-15"

# --- Valid nucleotides ---
VALID_DNA_CHARS = {"A", "T", "G", "C"}
VALID_RNA_CHARS = {"A", "U", "G", "C"}

# --- Codon tables ---
# Start codon: ATG (Methionine)
START_CODON = "ATG"

# Stop codons: TAA, TAG, TGA
STOP_CODONS = {"TAA", "TAG", "TGA"}

# --- GC content classification thresholds ---
GC_LOW_THRESHOLD  = 40.0   # below this = low GC
GC_HIGH_THRESHOLD = 60.0   # above this = high GC

# --- Melting temperature constants (Wallace rule) ---
# Tm = 2*(A+T) + 4*(G+C) for short sequences
TEMP_AT = 2    # degrees per A or T
TEMP_GC = 4    # degrees per G or C


# ============================================================
# SECTION 2: DISPLAY UTILITIES
# ============================================================
# Tests: f-strings, print(), string formatting


def print_header():
    """
    Print the program header banner.

    Uses f-strings with alignment and unicode box characters.
    """
    width = 62
    print(f"\n{'═' * width}")
    print(f"║ {PROGRAM_NAME:^{width - 4}} ║")
    print(f"║ {'Version ' + VERSION:^{width - 4}} ║")
    print(f"║ {('Author: ' + AUTHOR):^{width - 4}} ║")
    print(f"{'═' * width}\n")


def print_section(title):
    """
    Print a section separator with title.

    Args:
        title (str): Section title to display.
    """
    width = 62
    print(f"\n{'─' * width}")
    print(f"  {title}")
    print(f"{'─' * width}")


def print_result(label, value, width=30):
    """
    Print a labeled result with consistent formatting.

    Args:
        label (str): Description of the result.
        value      : The result value (any type).
        width (int): Label column width.
    """
    print(f"  {label:<{width}}: {value}")


def make_bar(value, maximum, width=30, fill="█", empty="░"):
    """
    Create a progress bar string.

    Args:
        value   (float): Current value.
        maximum (float): Maximum value.
        width   (int)  : Bar width in characters.
        fill    (str)  : Character for filled portion.
        empty   (str)  : Character for empty portion.

    Returns:
        str: Formatted progress bar string.
    """
    # TODO: handle edge case where maximum is 0
    ratio       = value / maximum if maximum != 0 else 0
    filled      = int(ratio * width)
    empty_count = width - filled
    bar         = fill * filled + empty * empty_count
    percent     = ratio * 100
    return f"[{bar}] {percent:5.1f}%"


# ============================================================
# SECTION 3: SEQUENCE VALIDATION
# ============================================================
# Tests: strings, booleans, logical operators, membership


def is_valid_dna(sequence):
    """
    Check if sequence is a valid DNA sequence.

    A valid DNA sequence:
    - Is not empty
    - Contains only A, T, G, C characters
    - Is uppercase

    Args:
        sequence (str): Sequence to validate.

    Returns:
        bool: True if valid DNA, False otherwise.
    """
    # YOUR CODE HERE:
    # 1. Check not empty
    # 2. Check all uppercase
    # 3. Check only valid chars using all() and membership
    pass


def is_valid_rna(sequence):
    """
    Check if sequence is valid RNA (A, U, G, C only).

    Args:
        sequence (str): Sequence to validate.

    Returns:
        bool: True if valid RNA, False otherwise.
    """
    # YOUR CODE HERE:
    pass


def has_start_codon(sequence):
    """
    Check if sequence begins with ATG (start codon).

    Args:
        sequence (str): DNA sequence.

    Returns:
        bool: True if starts with ATG.
    """
    # YOUR CODE HERE:
    pass


def has_stop_codon(sequence):
    """
    Check if sequence ends with a stop codon (TAA, TAG, TGA).

    Args:
        sequence (str): DNA sequence.

    Returns:
        bool: True if ends with valid stop codon.
    """
    # YOUR CODE HERE:
    # Hint: check last 3 characters against STOP_CODONS set
    pass


def validate_sequence(sequence):
    """
    Run all validation checks and return results dict.

    Args:
        sequence (str): DNA sequence to validate.

    Returns:
        dict: Validation results for each check.
    """
    # YOUR CODE HERE:
    # Return dict with keys:
    # not_empty, is_uppercase, valid_chars,
    # has_start, has_stop, is_complete_gene
    pass


# ============================================================
# SECTION 4: BASIC SEQUENCE ANALYSIS
# ============================================================
# Tests: strings methods, math operators, f-strings


def count_nucleotides(sequence):
    """
    Count occurrences of each nucleotide.

    Args:
        sequence (str): DNA sequence.

    Returns:
        dict: Count of A, T, G, C.
    """
    # YOUR CODE HERE:
    pass


def calculate_gc_content(sequence):
    """
    Calculate GC content percentage.

    Args:
        sequence (str): DNA sequence.

    Returns:
        float: GC content as percentage (0.0 to 100.0).
               Returns 0.0 for empty sequence.
    """
    # YOUR CODE HERE:
    # GC% = (G + C) / total * 100
    pass


def calculate_at_content(sequence):
    """
    Calculate AT content percentage.

    Args:
        sequence (str): DNA sequence.

    Returns:
        float: AT content as percentage.
    """
    # YOUR CODE HERE:
    pass


def calculate_melting_temp(sequence):
    """
    Calculate approximate melting temperature using Wallace rule.

    Formula: Tm = 2*(A+T) + 4*(G+C)
    Valid for sequences shorter than 14 nucleotides.

    Args:
        sequence (str): DNA sequence.

    Returns:
        float: Estimated melting temperature in Celsius.
    """
    # YOUR CODE HERE:
    # Use TEMP_AT and TEMP_GC constants
    pass


def classify_gc(gc_percent):
    """
    Classify GC content level.

    Args:
        gc_percent (float): GC content percentage.

    Returns:
        str: "Low GC", "Normal GC", or "High GC"
    """
    # YOUR CODE HERE:
    # Use GC_LOW_THRESHOLD and GC_HIGH_THRESHOLD constants
    pass


# ============================================================
# SECTION 5: SEQUENCE MANIPULATION
# ============================================================
# Tests: string slicing, methods, type conversion


def get_complement(sequence):
    """
    Get the complementary DNA strand.

    Complementary rules: A↔T, G↔C
    Uses temporary lowercase to avoid double-replacement.

    Args:
        sequence (str): DNA sequence.

    Returns:
        str: Complementary sequence (same direction).
    """
    # YOUR CODE HERE:
    # Step 1: A → t (lowercase temp)
    # Step 2: T → a (lowercase temp)
    # Step 3: G → c (lowercase temp)
    # Step 4: C → g (lowercase temp)
    # Step 5: .upper() to finalize
    pass


def get_reverse_complement(sequence):
    """
    Get the reverse complement of a DNA sequence.

    This is used constantly in bioinformatics.
    Represents the antiparallel complementary strand.

    Args:
        sequence (str): DNA sequence.

    Returns:
        str: Reverse complement sequence.
    """
    # YOUR CODE HERE:
    # Hint: get_complement() then reverse with [::-1]
    pass


def transcribe_to_rna(sequence):
    """
    Transcribe DNA to RNA (T → U).

    Args:
        sequence (str): DNA sequence.

    Returns:
        str: RNA sequence.
    """
    # YOUR CODE HERE:
    pass


def extract_codons(sequence):
    """
    Extract all codons from sequence (groups of 3).

    Args:
        sequence (str): DNA sequence.

    Returns:
        list: List of codon strings.
    """
    # YOUR CODE HERE:
    # Use slicing: sequence[i:i+3] for i in range(0, len, 3)
    # Only include complete codons (length == 3)
    pass


def get_reading_frames(sequence):
    """
    Get all three reading frames of a sequence.

    Reading frames start at positions 0, 1, 2.

    Args:
        sequence (str): DNA sequence.

    Returns:
        dict: {"frame1": [...], "frame2": [...], "frame3": [...]}
    """
    # YOUR CODE HERE:
    # Frame 1: sequence[0:]
    # Frame 2: sequence[1:]
    # Frame 3: sequence[2:]
    # Extract codons from each
    pass


# ============================================================
# SECTION 6: SEQUENCE SEARCH
# ============================================================
# Tests: string methods, comparisons, logical operators


def find_motif(sequence, motif):
    """
    Find all positions where motif occurs in sequence.

    Args:
        sequence (str): DNA sequence to search.
        motif    (str): Pattern to find.

    Returns:
        list: List of start positions (0-indexed).
    """
    # YOUR CODE HERE:
    # Use str.find() in a loop, or manual comparison
    # Return list of all positions where motif found
    positions = []
    start     = 0
    while True:
        pos = sequence.find(motif, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions


def count_motif(sequence, motif):
    """
    Count non-overlapping occurrences of motif.

    Args:
        sequence (str): DNA sequence.
        motif    (str): Pattern to count.

    Returns:
        int: Number of occurrences.
    """
    # YOUR CODE HERE:
    pass


def has_restriction_site(sequence, enzyme_name, site):
    """
    Check if sequence contains a restriction enzyme site.

    Args:
        sequence    (str): DNA sequence.
        enzyme_name (str): Name of restriction enzyme.
        site        (str): Recognition site sequence.

    Returns:
        tuple: (bool found, int position or -1)
    """
    # YOUR CODE HERE:
    pass


# ============================================================
# SECTION 7: STATISTICS AND COMPARISON
# ============================================================
# Tests: math operators, comparisons, type conversion


def sequence_statistics(sequence):
    """
    Calculate comprehensive statistics for a sequence.

    Args:
        sequence (str): DNA sequence.

    Returns:
        dict: All statistical measures.
    """
    # YOUR CODE HERE:
    # Return dict with:
    # length, a_count, t_count, g_count, c_count,
    # gc_percent, at_percent, gc_ratio (G/C),
    # at_ratio (A/T), melting_temp
    pass


def compare_sequences(seq1, seq2):
    """
    Compare two sequences and return similarity metrics.

    Args:
        seq1 (str): First DNA sequence.
        seq2 (str): Second DNA sequence.

    Returns:
        dict: Comparison metrics.
    """
    # YOUR CODE HERE:
    # Return dict with:
    # same_length, length_diff, identical (seq1==seq2),
    # gc_diff (abs difference in GC%), shorter, longer
    pass


def calculate_similarity(seq1, seq2):
    """
    Calculate percentage identity between two sequences.

    Only compares positions up to the shorter sequence length.

    Args:
        seq1 (str): First DNA sequence.
        seq2 (str): Second DNA sequence.

    Returns:
        float: Percentage of matching positions (0.0-100.0).
    """
    # YOUR CODE HERE:
    # Count matching positions at same index
    # Return matches / min_length * 100
    pass


# ============================================================
# SECTION 8: REPORT GENERATOR
# ============================================================
# Tests: f-strings, print(), string formatting, all topics


def generate_full_report(sequence, sequence_name="Unknown"):
    """
    Generate a complete analysis report for a DNA sequence.

    Args:
        sequence      (str): DNA sequence to analyze.
        sequence_name (str): Name/ID of the sequence.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    width     = 62

    # Header
    print(f"\n{'═' * width}")
    print(f"║ {'DNA SEQUENCE ANALYSIS REPORT':^{width-4}} ║")
    print(f"║ {('Generated: ' + timestamp):^{width-4}} ║")
    print(f"{'═' * width}")

    # YOUR CODE HERE - generate complete report including:

    # SECTION 1: Sequence Info
    # - Name, length, first/last 10 chars (with ... if longer)
    print_section("SEQUENCE INFORMATION")
    # YOUR CODE HERE

    # SECTION 2: Validation
    print_section("VALIDATION")
    # YOUR CODE HERE - run validate_sequence() and display results
    # Show ✓ or ✗ for each check

    # SECTION 3: Nucleotide Composition
    print_section("NUCLEOTIDE COMPOSITION")
    # YOUR CODE HERE - counts and percentages for each nucleotide
    # Include a mini bar chart for each:
    # A: ████████░░░░░░░░░░░░  40.0%  (count: X)

    # SECTION 4: GC Content Analysis
    print_section("GC CONTENT ANALYSIS")
    # YOUR CODE HERE
    # - GC% and AT%
    # - Classification (Low/Normal/High)
    # - Visual bar
    # - Melting temperature

    # SECTION 5: Sequence Manipulations
    print_section("SEQUENCE MANIPULATIONS")
    # YOUR CODE HERE
    # - Complement
    # - Reverse complement
    # - RNA transcript

    # SECTION 6: Codon Analysis
    print_section("CODON ANALYSIS")
    # YOUR CODE HERE
    # - Total codons
    # - First 5 codons
    # - Has start/stop codon
    # - Count ATG occurrences

    # SECTION 7: Restriction Sites
    print_section("RESTRICTION ENZYME SITES")
    # Check these common restriction enzymes:
    enzymes = [
        ("EcoRI",  "GAATTC"),
        ("BamHI",  "GGATCC"),
        ("HindIII","AAGCTT"),
        ("NotI",   "GCGGCCGC"),
        ("XhoI",   "CTCGAG"),
    ]
    # YOUR CODE HERE
    # For each enzyme: show if found and at what position

    # Footer
    print(f"\n{'═' * width}\n")


# ============================================================
# SECTION 9: INTERACTIVE MENU
# ============================================================
# Tests: input(), type conversion, logical operators


def get_sequence_from_user():
    """
    Get and validate a DNA sequence from user input.

    Returns:
        tuple: (sequence str, name str)
    """
    print("\n  Enter sequence name (or press ENTER for 'Unknown'):")
    name = input("  > ").strip() or "Unknown"

    print("\n  Enter DNA sequence (A, T, G, C only):")
    print("  (will be converted to uppercase automatically)")
    raw = input("  > ").strip().upper().replace(" ", "")

    if not raw:
        print("  ⚠  No sequence entered.")
        return None, None

    if not is_valid_dna(raw):
        print(f"  ✗  Invalid DNA sequence: contains non-ATGC characters")
        return None, None

    print(f"  ✓  Valid sequence accepted ({len(raw)} nucleotides)")
    return raw, name


def show_menu():
    """Display the main menu."""
    print("\n  ┌─────────────────────────────────┐")
    print("  │         MAIN MENU               │")
    print("  ├─────────────────────────────────┤")
    print("  │  1. Analyze sample sequences    │")
    print("  │  2. Enter your own sequence     │")
    print("  │  3. Compare two sequences       │")
    print("  │  4. Run all tests               │")
    print("  │  0. Exit                        │")
    print("  └─────────────────────────────────┘")
    print("  Choice: ", end="")


# ============================================================
# SECTION 10: SAMPLE DATA AND TESTS
# ============================================================
# Real biological sequences for testing


# Real gene fragments (shortened for learning purposes):
SAMPLE_SEQUENCES = {
    "TP53_fragment": {
        "sequence": "ATGTTCAAGACAGATTTTCAACTCTGTCTCCTTCCTCTTCCTACAGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGACATAGTGTGGTGGTGCCCTATGAGCCGCCTGAGGTTGGCTCTGACTGTACCACCATCCACTACAACTACATGTGTAACAGTTCCTGCATGGGCGGCATGAACCGGAGGCCCATCCTCACCATCATCACACTGGAAGACTCCAGTGGTAATCTACTGGGACGGAACAGCTTTGAGGTGCGTGTTTGTGCCTGTCCTGGGAGAGACCGGCGCACAGAGGAAGAGAATCTCCGCAAGAAAGGGGAGCCTCACCACGAGCTGCCCCCAGGGAGCACTAAGCGAGCACTGCCCAACAACACCAGCTCCTCTCCCCAGCCAAAGAAGAAACCACTGGATGGAGAATATTTCACCCTTCAGATCCGTGGGCGTGAGCGCTTCGAGATGTTCCGAGAGCTGAATGAGGCCTTGGAACTCAAGCCGGTGGAAATATTCTGGACCAGTGGTAATGAAGTGCAAAAGCGGGGAGAAAGACCGGCATTTCCGGACGATATTGAACAATGGATGATTTGAAGAAATGTTCCGTGGGGAGAAATCGTAAGCCCTCCTGGGCCAGTACCACAGTTATCCCTAAGACTCATAACCCCAATGCTTCTTACACAGAAGATCATGCAAGCATTGCCTCAGACCCAGGATGGCAAGTGGAAGAAATCAAAGTGCCTGTGGCTTCCTTTAGATGCAGCAGTTTTATTGTGGGGAGCAGGCTGTGGTGGTGTCCCCAGGGAAAGCTGTGGCCTGGATGTGGAATACCTACCAGGGAAGCAAAGGCCAAATACAGAATCAGAGGGCAGAGATGTTGGGGAGAAAGAAGCTACTTTCAAAGACTGGGCAGCTTTGAGTCAGTTTCCAAAGAGCCGGCTCCTCAGATTCCAGGTCCCCAGAGCCACCTGAATGGAAGGAAAATGCTCAGGAAACATTTTCAGTGGTT",
        "name": "TP53 tumor suppressor gene (human)"
    },
    "insulin_fragment": {
        "sequence": "ATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAG",
        "name": "Insulin gene fragment (human)"
    },
    "ecoli_16s": {
        "sequence": "ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGACGCGTACAGGAAACACAGAAAAAAGCCCGCACCTGACAGTGCGGGCTTTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGTACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCCAGGCAGGGGCAGGTGGCCACCGTCCTCTCTGCCCCCGCCAAAATCACCAACCACCTGGTGGCGATGATTGAAAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAACGTATTTTTGCCGAACTTTTGACGGGACTCGCCGCCGCCCAGCCGGGGTTCCCGCTGGCGCAATTGAAAACTTTCGTCGATCAGGAATTTGCCCAAATAAAACATGTCCTGCATGGCATTAGTTTGTTGGGGCAGTGCCCGGATAGCATCAACGCCGCGCTGATTTGCCGTGGCGAGAAAATGTCGATCGCCATTATGGCCGGCGTATTAGAAGCGCGCGGTCACAACGTTACTGTTATCGATCCGGTCGAAAAACTGCTGGCAGTGGGGCATTACCTCGAATCTACCGTCGATATTGCTGAGTCCACCCGCCGTATTGCGGCAAGCCGCATTCCGGCTGATCACATGGTGCTGATGGCAGGTTTCACCGCCGGTAATGAAAAAGGCGAACTGGTGGTGCTTGGACGCAACGGTTCCGACTACTCTGCTGCGGTGCTGGCTGCCTGTTTACGCGCCGATTGTTGCGAGATTTGGACGGACGTTGACGGGGTCTATACCTGCGACCCGCGTCAGGTGCCCGATGCGAGGTTGTTGAAGTCGATGTCCTACCAGGAAGCGATGGAGCTTTCCTACTTCGGCGCTAAAGTTCTTCACCCCCGCACCATTACCCCCATCGCCCAGTTCCAGATCCCTTGCCTGATTAAAAATACCGGAAATCCTCAAGCACCGTCTATAAAATTTATTTGCTTTGTGAGCGGATAACAATTATAATAGATTCAATTGTGAGCGGATAACAATTTCACACAGGAAACAGCTATGACCATGATTACGCCAAGCTTGCATGCCTGCAG",
        "name": "E. coli 16S rRNA gene fragment"
    },
    "covid_spike": {
        "sequence": "ATGTTCGTGTTCCTGGTGCTGCTGCCTCTGGTGTCAAGCCAGTGTGTGAACCTGACCACCAGAACACAGCTGCCTCCAGCCTATACCAACAGCTTCACAAGAGGCGTGTACTATCCCGACAAGGTTTTCAGATCTAGCGTGTATCTGCCTCTCCACCTTTTGAAGTATAATGTTACAGGCTTTATGGAAGTGAGTGTGAACTTCAGTTTCGGTATCGGTCCCGGCATCGTGCCTACCAAAACCAACAGCCCCTTTCGATTCAACGTGAAACCCTTCATCACCCAAGTGTCTAAAACCAGATCTACAGCCTCTAACAGGCAGCAACAGAACAAATGTTTCGGCAGCACTGGACATCAGAAGGCTTCCTGTGACAGCCATCAGAAGGGCCACAGCCATCACAAGCACAGACAGGCATCAGCAAGCACATCAGAAGGCAACAGCAATCAGAAGGCAAAGCCCAACAGCAATCAGAAGGCAACAGCAATCAGAAGGCAACAGCAATCAGAAGG",
        "name": "SARS-CoV-2 Spike protein gene (fragment)"
    }
}


def run_sample_analysis():
    """Run analysis on all sample sequences."""
    print_section("SAMPLE SEQUENCE ANALYSIS")

    for key, data in SAMPLE_SEQUENCES.items():
        seq  = data["sequence"]
        name = data["name"]

        print(f"\n  {'─'*58}")
        print(f"  Analyzing: {name}")
        print(f"  {'─'*58}")

        # YOUR CODE HERE:
        # For each sequence print:
        # 1. Length
        # 2. GC% with bar
        # 3. Has start codon?
        # 4. Has stop codon?
        # 5. Melting temperature
        # 6. Top restriction site if found


def run_comparison_demo():
    """Compare two sample sequences."""
    print_section("SEQUENCE COMPARISON DEMO")

    seq1 = SAMPLE_SEQUENCES["TP53_fragment"]["sequence"][:100]
    seq2 = SAMPLE_SEQUENCES["insulin_fragment"]["sequence"][:100]

    # YOUR CODE HERE:
    # Compare seq1 and seq2 using compare_sequences()
    # and calculate_similarity()
    # Print a formatted comparison report


def run_all_tests():
    """Run built-in tests to verify all functions work."""
    print_section("RUNNING TESTS")

    tests_passed = 0
    tests_failed = 0

    def test(description, actual, expected):
        nonlocal tests_passed, tests_failed
        # YOUR CODE HERE:
        # Compare actual to expected
        # Print ✓ or ✗ with description
        # Update counters
        pass

    # Test is_valid_dna():
    test("Valid DNA uppercase",     is_valid_dna("ATCG"),    True)
    test("Invalid DNA lowercase",   is_valid_dna("atcg"),    False)
    test("Invalid DNA with X",      is_valid_dna("ATXG"),    False)
    test("Empty sequence invalid",  is_valid_dna(""),        False)

    # Test count_nucleotides():
    counts = count_nucleotides("ATCGGCTA")
    test("Count A = 2",  counts["A"], 2)
    test("Count T = 2",  counts["T"], 2)
    test("Count G = 2",  counts["G"], 2)
    test("Count C = 2",  counts["C"], 2)

    # Test calculate_gc_content():
    test("GC 50%",  calculate_gc_content("ATCG"),  50.0)
    test("GC 100%", calculate_gc_content("GCGC"),  100.0)
    test("GC 0%",   calculate_gc_content("ATAT"),  0.0)

    # Test get_complement():
    test("Complement ATCG", get_complement("ATCG"), "TAGC")
    test("Complement AAAA", get_complement("AAAA"), "TTTT")

    # Test get_reverse_complement():
    test("Rev comp ATCG", get_reverse_complement("ATCG"), "CGAT")
    test("Rev comp AAAA", get_reverse_complement("AAAA"), "TTTT")

    # Test has_start_codon():
    test("Has start ATG",     has_start_codon("ATGCCC"), True)
    test("No start codon",    has_start_codon("CCCATG"), False)

    # Test has_stop_codon():
    test("Has stop TAA",  has_stop_codon("CCCTAA"), True)
    test("Has stop TAG",  has_stop_codon("CCCTAG"), True)
    test("Has stop TGA",  has_stop_codon("CCCTGA"), True)
    test("No stop codon", has_stop_codon("CCCAAA"), False)

    # Test transcribe_to_rna():
    test("Transcribe ATCG", transcribe_to_rna("ATCG"), "AUCG")
    test("Transcribe TTTT", transcribe_to_rna("TTTT"), "UUUU")

    # Test extract_codons():
    test("Extract codons",
         extract_codons("ATGCGATAA"),
         ["ATG", "CGA", "TAA"])

    # Test calculate_similarity():
    test("Identical 100%",   calculate_similarity("ATCG", "ATCG"), 100.0)
    test("Completely diff 0%", calculate_similarity("AAAA", "TTTT"), 0.0)
    test("50% similar",      calculate_similarity("AAAA", "AATT"), 50.0)

    # Summary:
    total = tests_passed + tests_failed
    print(f"\n  Results: {tests_passed}/{total} tests passed")
    if tests_failed == 0:
        print("  ✓ All tests passed!")
    else:
        print(f"  ✗ {tests_failed} test(s) failed - check your functions")


# ============================================================
# MAIN PROGRAM
# ============================================================


def main():
    """Main program entry point."""
    print_header()

    # Run tests first to verify functions work:
    run_all_tests()

    # Analyze a sample sequence with full report:
    print_section("FULL ANALYSIS DEMO")
    demo_seq  = SAMPLE_SEQUENCES["TP53_fragment"]["sequence"][:150]
    demo_name = "TP53 Fragment (first 150 nt)"
    generate_full_report(demo_seq, demo_name)

    # Run sample analysis on all sequences:
    run_sample_analysis()

    # Run comparison demo:
    run_comparison_demo()

    # Interactive menu (optional - comment out if not using input()):
    # while True:
    #     show_menu()
    #     choice = input().strip()
    #     if choice == "0":
    #         print("\n  Goodbye!\n")
    #         break
    #     elif choice == "1":
    #         run_sample_analysis()
    #     elif choice == "2":
    #         seq, name = get_sequence_from_user()
    #         if seq:
    #             generate_full_report(seq, name)
    #     elif choice == "3":
    #         run_comparison_demo()
    #     elif choice == "4":
    #         run_all_tests()
    #     else:
    #         print("  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# ============================================================
# END OF PROJECT 01
# ============================================================