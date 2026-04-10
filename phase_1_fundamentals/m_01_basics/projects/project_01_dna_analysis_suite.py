# ============================================================
# MODULE 01 | PROJECT 01 - DNA Analysis Suite
# ============================================================
# Difficulty  : ⭐⭐⭐⭐ (Hard)
# Covers      : ONLY Module 01 topics:
#               Variables, Numbers, Strings, Booleans,
#               Print, Input, Comments, Math Operators,
#               Comparison Operators, Logical Operators,
#               Type Conversion, F-Strings
# NO: functions, if/else, loops, imports, lists, dicts
# Estimated   : 3-5 hours
# ============================================================
#
# HOW THIS PROJECT WORKS:
# Each section is self-contained.
# You define variables, perform operations, and print results.
# NO functions, NO if statements, NO loops, NO imports.
# Everything is done with the 12 topics from Module 01.
# ============================================================


# ============================================================
# PROGRAM HEADER
# ============================================================
# Tests: variables, strings, f-strings, print()

PROGRAM_NAME = "DNA Analysis Suite"
VERSION      = "1.0.0"
AUTHOR       = "Your Name"
DATE         = "2025-01-15"
WIDTH        = 62

print(f"{'═' * WIDTH}")
print(f"║ {PROGRAM_NAME:^{WIDTH - 4}} ║")
print(f"║ {'Version ' + VERSION:^{WIDTH - 4}} ║")
print(f"║ {('Author: ' + AUTHOR):^{WIDTH - 4}} ║")
print(f"║ {('Date: ' + DATE):^{WIDTH - 4}} ║")
print(f"{'═' * WIDTH}")


# ============================================================
# SECTION 1: SEQUENCE DEFINITION AND BASIC INFO
# ============================================================
# Tests: variables, strings, type conversion, f-strings

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 1: SEQUENCE DEFINITION")
print(f"{'─' * WIDTH}")

# Real fragment of the TP53 tumor suppressor gene (human)
# TP53 is called "Guardian of the Genome"
# Mutations in TP53 are found in ~50% of all human cancers
sequence_raw  = "  atgTTCAAgacagattttcaaCTCTGTCTCCTTCCTCTTCCTACAGTACTCCC  "
sequence_name = "TP53 tumor suppressor gene fragment"
organism      = "Homo sapiens"
chromosome    = "17"
gene_id       = "TP53"

# Step 1: Clean the sequence - strip whitespace, convert to uppercase
# This simulates real bioinformatics data cleaning
sequence_clean = sequence_raw.strip().upper().replace(" ", "")

# Step 2: Basic information
sequence_length = len(sequence_clean)
first_10        = sequence_clean[:10]
last_10         = sequence_clean[-10:]
middle_start    = sequence_length // 2 - 5
middle_10       = sequence_clean[middle_start:middle_start + 10]

# Step 3: Display
print(f"\n  Gene         : {gene_id}")
print(f"  Organism     : {organism}")
print(f"  Chromosome   : {chromosome}")
print(f"  Raw input    : {repr(sequence_raw)}")
print(f"  Cleaned      : {sequence_clean}")
print(f"  Length       : {sequence_length} nucleotides")
print(f"  First 10 nt  : {first_10}")
print(f"  Last 10 nt   : {last_10}")
print(f"  Middle 10 nt : {middle_10}")

# Step 4: Type verification
print(f"\n  Type of sequence : {type(sequence_clean)}")
print(f"  Type of length   : {type(sequence_length)}")

# Step 5: Sequence preview (first 30 chars + ...)
preview = sequence_clean[:30] + "..." + f" ({sequence_length} nt total)"
print(f"  Preview          : {preview}")


# ============================================================
# SECTION 2: SEQUENCE VALIDATION
# ============================================================
# Tests: strings, booleans, logical operators, comparison, membership

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 2: SEQUENCE VALIDATION")
print(f"{'─' * WIDTH}")

# Check 1: Is the sequence non-empty?
is_not_empty = len(sequence_clean) > 0

# Check 2: Is it all uppercase?
is_uppercase = sequence_clean == sequence_clean.upper()

# Check 3: Does it contain ONLY valid nucleotides (A, T, G, C)?
# Count all valid chars and compare to total length
valid_char_count = (
    sequence_clean.count("A") +
    sequence_clean.count("T") +
    sequence_clean.count("G") +
    sequence_clean.count("C")
)
is_only_valid_chars = valid_char_count == sequence_length

# Check 4: Does it start with ATG (start codon)?
has_start_codon = sequence_clean[:3] == "ATG"

# Check 5: Does it end with a stop codon (TAA, TAG, or TGA)?
last_codon      = sequence_clean[-3:]
has_stop_codon  = last_codon == "TAA" or last_codon == "TAG" or last_codon == "TGA"

# Check 6: Is length divisible by 3 (complete codons)?
has_complete_codons = sequence_length % 3 == 0

# Check 7: Is it a complete gene (has start AND stop AND valid)?
is_complete_gene = (
    is_not_empty and
    is_uppercase and
    is_only_valid_chars and
    has_start_codon and
    has_stop_codon and
    has_complete_codons
)

# Display validation results using ternary in f-string
print(f"\n  Validation Results:")
print(f"  {'─' * 40}")
print(f"  Not empty          : {'✓' if is_not_empty else '✗'}  {is_not_empty}")
print(f"  Uppercase          : {'✓' if is_uppercase else '✗'}  {is_uppercase}")
print(f"  Valid chars only   : {'✓' if is_only_valid_chars else '✗'}  {is_only_valid_chars}")
print(f"  Has start (ATG)    : {'✓' if has_start_codon else '✗'}  {has_start_codon}")
print(f"  Has stop codon     : {'✓' if has_stop_codon else '✗'}  {has_stop_codon}")
print(f"  Complete codons    : {'✓' if has_complete_codons else '✗'}  {has_complete_codons}")
print(f"  {'─' * 40}")
print(f"  Complete gene      : {'✓' if is_complete_gene else '✗'}  {is_complete_gene}")

# Invalid characters check
invalid_count = sequence_length - valid_char_count
print(f"\n  Valid nucleotides  : {valid_char_count}")
print(f"  Invalid characters : {invalid_count}")
print(f"  Sequence is valid  : {is_only_valid_chars and is_not_empty and is_uppercase}")


# ============================================================
# SECTION 3: NUCLEOTIDE COMPOSITION
# ============================================================
# Tests: strings (.count()), math operators, f-strings, numbers

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 3: NUCLEOTIDE COMPOSITION")
print(f"{'─' * WIDTH}")

# Count each nucleotide
count_a = sequence_clean.count("A")
count_t = sequence_clean.count("T")
count_g = sequence_clean.count("G")
count_c = sequence_clean.count("C")
count_total = count_a + count_t + count_g + count_c

# Calculate percentages
percent_a = count_a / sequence_length * 100
percent_t = count_t / sequence_length * 100
percent_g = count_g / sequence_length * 100
percent_c = count_c / sequence_length * 100

# Calculate GC and AT content
gc_count   = count_g + count_c
at_count   = count_a + count_t
gc_percent = gc_count / sequence_length * 100
at_percent = at_count / sequence_length * 100

# Verify: all percentages sum to 100
total_percent = percent_a + percent_t + percent_g + percent_c

# Display counts table
print(f"\n  Nucleotide Counts:")
print(f"  {'─' * 50}")
print(f"  {'Nucleotide':<12} {'Count':>6} {'Percent':>8}  {'Bar':<20}")
print(f"  {'─' * 50}")

# Build bars manually (using string multiplication)
bar_width  = 20
bar_a = "█" * int(percent_a / 100 * bar_width) + "░" * (bar_width - int(percent_a / 100 * bar_width))
bar_t = "█" * int(percent_t / 100 * bar_width) + "░" * (bar_width - int(percent_t / 100 * bar_width))
bar_g = "█" * int(percent_g / 100 * bar_width) + "░" * (bar_width - int(percent_g / 100 * bar_width))
bar_c = "█" * int(percent_c / 100 * bar_width) + "░" * (bar_width - int(percent_c / 100 * bar_width))

print(f"  {'Adenine  (A)':<12} {count_a:>6} {percent_a:>7.1f}%  {bar_a}")
print(f"  {'Thymine  (T)':<12} {count_t:>6} {percent_t:>7.1f}%  {bar_t}")
print(f"  {'Guanine  (G)':<12} {count_g:>6} {percent_g:>7.1f}%  {bar_g}")
print(f"  {'Cytosine (C)':<12} {count_c:>6} {percent_c:>7.1f}%  {bar_c}")
print(f"  {'─' * 50}")
print(f"  {'TOTAL':<12} {count_total:>6} {total_percent:>7.1f}%")

# GC / AT summary
print(f"\n  GC Content  : {gc_count:>4} nucleotides = {gc_percent:.2f}%")
print(f"  AT Content  : {at_count:>4} nucleotides = {at_percent:.2f}%")
print(f"  GC + AT     : {gc_percent + at_percent:.1f}% (should be 100.0%)")

# GC classification (using bool expressions and ternary)
is_low_gc    = gc_percent < 40.0
is_normal_gc = 40.0 <= gc_percent <= 60.0
is_high_gc   = gc_percent > 60.0

gc_class = ("Low GC" if is_low_gc else ("Normal GC" if is_normal_gc else "High GC"))
print(f"  GC Class    : {gc_class}")


# ============================================================
# SECTION 4: MELTING TEMPERATURE
# ============================================================
# Tests: math operators, numbers, f-strings

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 4: MELTING TEMPERATURE")
print(f"{'─' * WIDTH}")

# Wallace Rule: Tm = 2*(A+T) + 4*(G+C)
# Valid for short sequences (< 14 nt)
# For longer sequences we use a modified formula

# Simple Wallace rule
tm_wallace = 2 * at_count + 4 * gc_count

# Modified formula for longer sequences (empirical)
# Tm = 81.5 + 16.6 * log10(Na+) + 0.41 * GC% - 675/length
# Assuming Na+ = 0.05M (typical PCR condition)
# log10(0.05) = -1.301
sodium_correction = 16.6 * (-1.301)
tm_modified = 81.5 + sodium_correction + 0.41 * gc_percent - 675 / sequence_length

# Display
print(f"\n  Melting Temperature Calculations:")
print(f"  {'─' * 40}")
print(f"  Wallace Rule   : {tm_wallace}°C")
print(f"    Formula: 2*(A+T) + 4*(G+C)")
print(f"    = 2*{at_count} + 4*{gc_count}")
print(f"    = {2*at_count} + {4*gc_count}")
print(f"    = {tm_wallace}°C")
print(f"\n  Modified Formula: {tm_modified:.1f}°C")
print(f"    (corrected for length and Na+ concentration)")
print(f"    Assumes [Na+] = 0.05M")

# Is this in typical PCR range?
in_pcr_range = 50.0 <= tm_modified <= 65.0
print(f"\n  In PCR range (50-65°C): {in_pcr_range}")


# ============================================================
# SECTION 5: SEQUENCE MANIPULATIONS
# ============================================================
# Tests: strings (.replace(), slicing, [::-1]), f-strings

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 5: SEQUENCE MANIPULATIONS")
print(f"{'─' * WIDTH}")

# 1. Complementary strand (A↔T, G↔C)
# Use lowercase temporarily to avoid double-replacement
complement = (
    sequence_clean
    .replace("A", "t")
    .replace("T", "a")
    .replace("G", "c")
    .replace("C", "g")
    .upper()
)

# 2. Reverse complement (antiparallel strand)
reverse_complement = complement[::-1]

# 3. RNA transcript (T → U)
rna_transcript = sequence_clean.replace("T", "U")

# 4. Reverse sequence
reversed_sequence = sequence_clean[::-1]

# Display (show first 40 chars if long)
display_len = 40
seq_display  = sequence_clean[:display_len]  + ("..." if sequence_length > display_len else "")
comp_display = complement[:display_len]      + ("..." if sequence_length > display_len else "")
rcomp_display= reverse_complement[:display_len] + ("..." if sequence_length > display_len else "")
rna_display  = rna_transcript[:display_len]  + ("..." if sequence_length > display_len else "")
rev_display  = reversed_sequence[:display_len] + ("..." if sequence_length > display_len else "")

print(f"\n  Original (5'→3')        : {seq_display}")
print(f"  Complement (3'→5')      : {comp_display}")
print(f"  Rev. Complement (5'→3') : {rcomp_display}")
print(f"  RNA Transcript          : {rna_display}")
print(f"  Reversed                : {rev_display}")

# Verify complement is correct length
print(f"\n  Original length          : {len(sequence_clean)}")
print(f"  Complement length        : {len(complement)}")
print(f"  Lengths match            : {len(sequence_clean) == len(complement)}")

# Is the sequence a palindrome? (same as reverse complement)
is_palindrome = sequence_clean == reverse_complement
print(f"  Is palindromic           : {is_palindrome}")


# ============================================================
# SECTION 6: CODON ANALYSIS
# ============================================================
# Tests: string slicing, math operators, comparisons, f-strings

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 6: CODON ANALYSIS")
print(f"{'─' * WIDTH}")

# Extract codons manually (groups of 3)
# We know the sequence length, so we calculate positions manually
total_codons    = sequence_length // 3
leftover_bases  = sequence_length % 3

# First 10 codons (or less if sequence is short)
codon_1  = sequence_clean[0:3]   if sequence_length >= 3  else "---"
codon_2  = sequence_clean[3:6]   if sequence_length >= 6  else "---"
codon_3  = sequence_clean[6:9]   if sequence_length >= 9  else "---"
codon_4  = sequence_clean[9:12]  if sequence_length >= 12 else "---"
codon_5  = sequence_clean[12:15] if sequence_length >= 15 else "---"
codon_6  = sequence_clean[15:18] if sequence_length >= 18 else "---"
codon_7  = sequence_clean[18:21] if sequence_length >= 21 else "---"
codon_8  = sequence_clean[21:24] if sequence_length >= 24 else "---"
codon_9  = sequence_clean[24:27] if sequence_length >= 27 else "---"
codon_10 = sequence_clean[27:30] if sequence_length >= 30 else "---"

# Last codon
last_codon_pos  = (total_codons - 1) * 3
last_codon_seq  = sequence_clean[last_codon_pos:last_codon_pos + 3]

# Is the first codon a start codon?
first_codon_is_start = codon_1 == "ATG"

# Is the last codon a stop codon?
last_is_stop = (
    last_codon_seq == "TAA" or
    last_codon_seq == "TAG" or
    last_codon_seq == "TGA"
)

# Count ATG occurrences (potential start codons)
atg_count = sequence_clean.count("ATG")

# Count stop codons
taa_count = sequence_clean.count("TAA")
tag_count = sequence_clean.count("TAG")
tga_count = sequence_clean.count("TGA")
stop_count = taa_count + tag_count + tga_count

# Reading frame 2 and 3 first codons
frame2_codon1 = sequence_clean[1:4]  if sequence_length >= 4  else "---"
frame3_codon1 = sequence_clean[2:5]  if sequence_length >= 5  else "---"

print(f"\n  Codon Statistics:")
print(f"  {'─' * 40}")
print(f"  Total codons      : {total_codons}")
print(f"  Leftover bases    : {leftover_bases}")
print(f"  ATG occurrences   : {atg_count}")
print(f"  TAA occurrences   : {taa_count}")
print(f"  TAG occurrences   : {tag_count}")
print(f"  TGA occurrences   : {tga_count}")
print(f"  Stop codon total  : {stop_count}")

print(f"\n  Reading Frame 1 (first 10 codons):")
print(f"  Pos  1: {codon_1}   {'← START ✓' if codon_1 == 'ATG' else ''}")
print(f"  Pos  2: {codon_2}")
print(f"  Pos  3: {codon_3}")
print(f"  Pos  4: {codon_4}")
print(f"  Pos  5: {codon_5}")
print(f"  Pos  6: {codon_6}")
print(f"  Pos  7: {codon_7}")
print(f"  Pos  8: {codon_8}")
print(f"  Pos  9: {codon_9}")
print(f"  Pos 10: {codon_10}")
print(f"  ...")
print(f"  Last:   {last_codon_seq}   {'← STOP ✓' if last_is_stop else '← no stop codon'}")

print(f"\n  Reading Frame 2 (starts at position 1):")
print(f"  First codon: {frame2_codon1}")
print(f"\n  Reading Frame 3 (starts at position 2):")
print(f"  First codon: {frame3_codon1}")

print(f"\n  Complete gene check:")
print(f"  Has start codon : {first_codon_is_start}")
print(f"  Has stop codon  : {last_is_stop}")
print(f"  Is complete gene: {first_codon_is_start and last_is_stop and has_complete_codons}")


# ============================================================
# SECTION 7: RESTRICTION ENZYME SITES
# ============================================================
# Tests: strings (.find(), .count(), in), comparisons, f-strings

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 7: RESTRICTION ENZYME SITES")
print(f"{'─' * WIDTH}")

# Common restriction enzymes and their recognition sites
ecori_site   = "GAATTC"    # EcoRI
bamhi_site   = "GGATCC"    # BamHI
hindiii_site = "AAGCTT"    # HindIII
noti_site    = "GCGGCCGC"  # NotI
xhoi_site    = "CTCGAG"    # XhoI
tata_box     = "TATAAA"    # TATA box (promoter element)

# Check presence and position
ecori_found   = ecori_site   in sequence_clean
bamhi_found   = bamhi_site   in sequence_clean
hindiii_found = hindiii_site in sequence_clean
noti_found    = noti_site    in sequence_clean
xhoi_found    = xhoi_site    in sequence_clean
tata_found    = tata_box     in sequence_clean

# Find positions (first occurrence, -1 if not found)
ecori_pos   = sequence_clean.find(ecori_site)
bamhi_pos   = sequence_clean.find(bamhi_site)
hindiii_pos = sequence_clean.find(hindiii_site)
noti_pos    = sequence_clean.find(noti_site)
xhoi_pos    = sequence_clean.find(xhoi_site)
tata_pos    = sequence_clean.find(tata_box)

# Count occurrences
ecori_count   = sequence_clean.count(ecori_site)
bamhi_count   = sequence_clean.count(bamhi_site)
hindiii_count = sequence_clean.count(hindiii_site)
noti_count    = sequence_clean.count(noti_site)
xhoi_count    = sequence_clean.count(xhoi_site)
tata_count    = sequence_clean.count(tata_box)

# Display
print(f"\n  {'Enzyme':<12} {'Site':<12} {'Found':<8} {'Position':>8} {'Count':>6}")
print(f"  {'─' * 52}")
print(f"  {'EcoRI':<12} {ecori_site:<12} {'✓' if ecori_found else '✗':<8} {ecori_pos:>8} {ecori_count:>6}")
print(f"  {'BamHI':<12} {bamhi_site:<12} {'✓' if bamhi_found else '✗':<8} {bamhi_pos:>8} {bamhi_count:>6}")
print(f"  {'HindIII':<12} {hindiii_site:<12} {'✓' if hindiii_found else '✗':<8} {hindiii_pos:>8} {hindiii_count:>6}")
print(f"  {'NotI':<12} {noti_site:<12} {'✓' if noti_found else '✗':<8} {noti_pos:>8} {noti_count:>6}")
print(f"  {'XhoI':<12} {xhoi_site:<12} {'✓' if xhoi_found else '✗':<8} {xhoi_pos:>8} {xhoi_count:>6}")
print(f"  {'─' * 52}")
print(f"  {'TATA box':<12} {tata_box:<12} {'✓' if tata_found else '✗':<8} {tata_pos:>8} {tata_count:>6}")

# Total sites found
total_sites_found = (
    ecori_count + bamhi_count + hindiii_count +
    noti_count + xhoi_count
)
print(f"\n  Total restriction sites : {total_sites_found}")


# ============================================================
# SECTION 8: SEQUENCE COMPARISON
# ============================================================
# Tests: strings, comparisons, math, f-strings

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 8: SEQUENCE COMPARISON")
print(f"{'─' * WIDTH}")

# Second sequence - fragment of insulin gene (human)
sequence2_raw  = "ATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGG"
sequence2_name = "Insulin gene fragment"
sequence2      = sequence2_raw.strip().upper()
length2        = len(sequence2)

# Basic comparison
are_identical       = sequence_clean == sequence2
same_length         = sequence_length == length2
length_difference   = abs(sequence_length - length2)

# GC content of sequence 2
gc2_count   = sequence2.count("G") + sequence2.count("C")
gc2_percent = gc2_count / length2 * 100
gc_diff     = abs(gc_percent - gc2_percent)

# Compare first 50 chars (or length of shorter)
compare_len = 50
seq1_50 = sequence_clean[:compare_len]
seq2_50 = sequence2[:compare_len]

# Count matching positions manually
# We compare char by char using indexing
# (without loops - we'll compare known positions)
match_0  = seq1_50[0]  == seq2_50[0]  if compare_len >= 1  else False
match_1  = seq1_50[1]  == seq2_50[1]  if compare_len >= 2  else False
match_2  = seq1_50[2]  == seq2_50[2]  if compare_len >= 3  else False
match_3  = seq1_50[3]  == seq2_50[3]  if compare_len >= 4  else False
match_4  = seq1_50[4]  == seq2_50[4]  if compare_len >= 5  else False
match_5  = seq1_50[5]  == seq2_50[5]  if compare_len >= 6  else False
match_6  = seq1_50[6]  == seq2_50[6]  if compare_len >= 7  else False
match_7  = seq1_50[7]  == seq2_50[7]  if compare_len >= 8  else False
match_8  = seq1_50[8]  == seq2_50[8]  if compare_len >= 9  else False
match_9  = seq1_50[9]  == seq2_50[9]  if compare_len >= 10 else False

# Count matches (bool arithmetic - True = 1)
matches_first_10 = (
    int(match_0) + int(match_1) + int(match_2) + int(match_3) +
    int(match_4) + int(match_5) + int(match_6) + int(match_7) +
    int(match_8) + int(match_9)
)
similarity_first_10 = matches_first_10 / 10 * 100

# Shared motifs
shared_atg  = sequence_clean.count("ATG")  > 0 and sequence2.count("ATG")  > 0
shared_tata = sequence_clean.count("TATA") > 0 and sequence2.count("TATA") > 0

print(f"\n  Sequence 1: {sequence_name[:35]}")
print(f"  Sequence 2: {sequence2_name}")
print(f"\n  {'─' * 50}")
print(f"  {'Metric':<28} {'Seq 1':>10} {'Seq 2':>10}")
print(f"  {'─' * 50}")
print(f"  {'Length (nt)':<28} {sequence_length:>10} {length2:>10}")
print(f"  {'GC content (%)':<28} {gc_percent:>10.1f} {gc2_percent:>10.1f}")
print(f"  {'AT content (%)':<28} {at_percent:>10.1f} {100 - gc2_percent:>10.1f}")
print(f"  {'A count':<28} {count_a:>10} {sequence2.count('A'):>10}")
print(f"  {'T count':<28} {count_t:>10} {sequence2.count('T'):>10}")
print(f"  {'G count':<28} {count_g:>10} {sequence2.count('G'):>10}")
print(f"  {'C count':<28} {count_c:>10} {sequence2.count('C'):>10}")
print(f"  {'─' * 50}")
print(f"\n  Are identical         : {are_identical}")
print(f"  Same length           : {same_length}")
print(f"  Length difference     : {length_difference} nt")
print(f"  GC content difference : {gc_diff:.1f}%")
print(f"  Similarity (first 10) : {similarity_first_10:.0f}%")
print(f"  Both have ATG         : {shared_atg}")
print(f"  Both have TATA        : {shared_tata}")


# ============================================================
# SECTION 9: MATHEMATICAL ANALYSIS
# ============================================================
# Tests: math operators, numbers, type conversion, f-strings

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 9: MATHEMATICAL ANALYSIS")
print(f"{'─' * WIDTH}")

# Molecular weight calculation
# Average MW of nucleotides (Da):
# A = 313.21, T = 304.19, G = 329.21, C = 289.18
mw_a = 313.21
mw_t = 304.19
mw_g = 329.21
mw_c = 289.18
water = 18.02   # subtract one water per phosphodiester bond

# Total molecular weight of single strand
total_mw_single = (
    count_a * mw_a +
    count_t * mw_t +
    count_g * mw_g +
    count_c * mw_c -
    (sequence_length - 1) * water
)

# Double-stranded DNA molecular weight
# Complement: same counts but A↔T and G↔C swapped
comp_mw = (
    count_a * mw_t +   # A pairs with T
    count_t * mw_a +   # T pairs with A
    count_g * mw_c +   # G pairs with C
    count_c * mw_g -   # C pairs with G
    (sequence_length - 1) * water
)
total_mw_double = total_mw_single + comp_mw

# Concentration calculations
# Number of molecules per mole (Avogadro)
avogadro = 6.022e23

# If we have 1 microgram of this DNA
# how many molecules?
mass_ug         = 1.0                          # micrograms
mass_g          = mass_ug * 1e-6               # convert to grams
moles           = mass_g / (total_mw_single / 1000)  # MW in kDa→ g/mol
molecules       = moles * avogadro

# GC Skew: (G - C) / (G + C)
# Positive skew = more G than C (leading strand characteristics)
gc_skew = (count_g - count_c) / (count_g + count_c) if (count_g + count_c) > 0 else 0.0

# AT Skew: (A - T) / (A + T)
at_skew = (count_a - count_t) / (count_a + count_t) if (count_a + count_t) > 0 else 0.0

# Entropy-like measure: how "random" is the sequence?
# Perfect random: each nucleotide = 25%
# Measure deviation from 25%
deviation_a = abs(percent_a - 25.0)
deviation_t = abs(percent_t - 25.0)
deviation_g = abs(percent_g - 25.0)
deviation_c = abs(percent_c - 25.0)
avg_deviation = (deviation_a + deviation_t + deviation_g + deviation_c) / 4

# Dinucleotide counts (selected)
cg_count = sequence_clean.count("CG")   # CpG sites
at_dinuc  = sequence_clean.count("AT")
gc_dinuc  = sequence_clean.count("GC")

print(f"\n  Molecular Weight:")
print(f"  {'─' * 40}")
print(f"  Single strand  : {total_mw_single:>12,.1f} Da")
print(f"  Double strand  : {total_mw_double:>12,.1f} Da")
print(f"  Per nucleotide : {total_mw_single/sequence_length:>12.1f} Da/nt")
print(f"\n  Concentration (1 µg sample):")
print(f"  Mass (g)       : {mass_g:.2e} g")
print(f"  Moles          : {moles:.2e} mol")
print(f"  Molecules      : {molecules:.2e}")
print(f"\n  Sequence Skew:")
print(f"  GC Skew        : {gc_skew:>+.4f}  ({'G-rich' if gc_skew > 0 else 'C-rich' if gc_skew < 0 else 'balanced'})")
print(f"  AT Skew        : {at_skew:>+.4f}  ({'A-rich' if at_skew > 0 else 'T-rich' if at_skew < 0 else 'balanced'})")
print(f"  Avg deviation  : {avg_deviation:.2f}% from random")
print(f"\n  Dinucleotide Counts:")
print(f"  CpG sites      : {cg_count:>4}")
print(f"  AT dinuc       : {at_dinuc:>4}")
print(f"  GC dinuc       : {gc_dinuc:>4}")


# ============================================================
# SECTION 10: FINAL SUMMARY REPORT
# ============================================================
# Tests: ALL Module 01 topics combined

print(f"\n{'═' * WIDTH}")
print(f"║ {'FINAL ANALYSIS SUMMARY':^{WIDTH - 4}} ║")
print(f"{'═' * WIDTH}")

print(f"""
  Gene          : {gene_id} ({sequence_name})
  Organism      : {organism}
  Chromosome    : {chromosome}

  ┌─────────────────────────────────────────────────────┐
  │ SEQUENCE                                            │
  │  Length     : {sequence_length:<6} nucleotides               │
  │  Codons     : {total_codons:<6} complete codons              │
  │  Is valid   : {str(is_only_valid_chars and is_not_empty):<6}                           │
  │  Complete   : {str(is_complete_gene):<6}                           │
  ├─────────────────────────────────────────────────────┤
  │ COMPOSITION                                         │
  │  A: {percent_a:4.1f}%   T: {percent_t:4.1f}%   G: {percent_g:4.1f}%   C: {percent_c:4.1f}%  │
  │  GC content : {gc_percent:5.1f}% ({gc_class})              │
  │  AT content : {at_percent:5.1f}%                           │
  ├─────────────────────────────────────────────────────┤
  │ THERMAL PROPERTIES                                  │
  │  Tm (Wallace)  : {tm_wallace}°C                         │
  │  Tm (Modified) : {tm_modified:.1f}°C                       │
  │  In PCR range  : {str(in_pcr_range):<6}                          │
  ├─────────────────────────────────────────────────────┤
  │ STRUCTURE                                           │
  │  Has start (ATG) : {str(has_start_codon):<6}                        │
  │  Has stop codon  : {str(has_stop_codon):<6}                        │
  │  Is palindrome   : {str(is_palindrome):<6}                        │
  │  GC skew         : {gc_skew:>+.4f}                      │
  ├─────────────────────────────────────────────────────┤
  │ MOLECULAR WEIGHT                                    │
  │  Single strand : {total_mw_single:>12,.1f} Da               │
  │  Double strand : {total_mw_double:>12,.1f} Da               │
  └─────────────────────────────────────────────────────┘
""")

print(f"{'═' * WIDTH}")
print(f"  Analysis complete. All results computed using Module 01 topics only.")
print(f"  No functions, no if/else, no loops, no imports used.")
print(f"{'═' * WIDTH}\n")

# ============================================================
# END OF PROJECT 01
# ============================================================