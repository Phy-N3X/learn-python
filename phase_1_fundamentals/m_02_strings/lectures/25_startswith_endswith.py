# ============================================================
# MODULE 02 | LECTURE 25 - .startswith() and .endswith()
# ============================================================
# What you will learn:
#   - What .startswith() does and how to use it
#   - What .endswith() does and how to use it
#   - The full syntax: start and end parameters
#   - Checking multiple prefixes/suffixes with a TUPLE
#   - Case sensitivity and how to handle it
#   - Return value: always True or False
#   - Combining with other methods
#   - Real world use cases
#   - Common mistakes
# ============================================================


# ------------------------------------------------------------
# PART 1: The problem they solve
# ------------------------------------------------------------

# Very often in programming you need to check
# HOW a string BEGINS or HOW it ENDS.

# Examples from real life:
#   - Does this filename end with ".pdf"?
#   - Does this URL start with "https://"?
#   - Does this DNA sequence start with "ATG" (start codon)?
#   - Does this variable name start with "_"?
#   - Does this email end with ".edu"?

# Without .startswith() and .endswith(), you might do this:
filename = "report.pdf"

# ❌ Clunky approach using slicing:
if filename[-4:] == ".pdf":
    print("It's a PDF!")

# ❌ Clunky approach using .find():
if filename.find(".pdf") == len(filename) - 4:
    print("It's a PDF!")

# ✅ Clean approach with .endswith():
if filename.endswith(".pdf"):
    print("It's a PDF!")

# The third version is readable, clear, and expressive.
# It reads almost like plain English!


# ------------------------------------------------------------
# PART 2: .startswith() - basic usage
# ------------------------------------------------------------

# .startswith(prefix) returns True if the string
# BEGINS with the given prefix, False otherwise.
#
# Syntax:
#   string.startswith(prefix)
#   string.startswith(prefix, start)
#   string.startswith(prefix, start, end)
#
# Returns: BOOLEAN (True or False) - always!

# ── Basic examples ──
text = "Python programming"

print(text.startswith("Python"))        # True
print(text.startswith("python"))        # False  ← case sensitive!
print(text.startswith("Pro"))           # False  ← "Pro" not at start
print(text.startswith("programming"))   # False  ← not at the start!
print(text.startswith("P"))            # True   ← single character prefix
print(text.startswith(""))             # True   ← empty string is always True!

# ── Return type is always bool ──
result = text.startswith("Python")
print(result)           # True
print(type(result))     # <class 'bool'>

# ── More examples ──
url = "https://www.example.com"
print(url.startswith("https"))      # True
print(url.startswith("http"))       # True  ← "https" STARTS with "http"!
print(url.startswith("https://"))   # True
print(url.startswith("ftp"))        # False
print(url.startswith("www"))        # False  ← "www" is not at the very start

filename = "report_2024.pdf"
print(filename.startswith("report"))    # True
print(filename.startswith("Report"))    # False  ← case sensitive!
print(filename.startswith("2024"))      # False  ← not at start


# ------------------------------------------------------------
# PART 3: .endswith() - basic usage
# ------------------------------------------------------------

# .endswith(suffix) returns True if the string
# ENDS with the given suffix, False otherwise.
#
# Syntax:
#   string.endswith(suffix)
#   string.endswith(suffix, start)
#   string.endswith(suffix, start, end)
#
# Returns: BOOLEAN (True or False) - always!

# ── Basic examples ──
filename = "genome_data.fasta"

print(filename.endswith(".fasta"))      # True
print(filename.endswith("fasta"))       # True   ← with or without dot
print(filename.endswith(".FASTA"))      # False  ← case sensitive!
print(filename.endswith("data"))        # False  ← "data" not at the end
print(filename.endswith("a"))           # True   ← last char is 'a'
print(filename.endswith(""))            # True   ← empty string always True!

# ── More examples ──
url = "https://www.example.com/page"
print(url.endswith("/page"))        # True
print(url.endswith("page"))         # True
print(url.endswith(".com"))         # False  ← ".com" is NOT at the end
print(url.endswith(".com/page"))    # True   ← this IS at the end!

email = "anna@university.edu"
print(email.endswith(".edu"))       # True
print(email.endswith(".com"))       # False
print(email.endswith("edu"))        # True

dna = "ATGCCCGCATAA"
print(dna.endswith("TAA"))          # True   ← stop codon!
print(dna.endswith("TAG"))          # False
print(dna.endswith("TGA"))          # False
print(dna.startswith("ATG"))        # True   ← start codon!


# ------------------------------------------------------------
# PART 4: Case sensitivity and how to handle it
# ------------------------------------------------------------

# Both methods are CASE SENSITIVE by default.
# "Python" and "python" are different prefixes/suffixes.

text = "Hello World"
print(text.startswith("hello"))     # False  ← lowercase 'h'
print(text.startswith("Hello"))     # True   ← uppercase 'H'
print(text.endswith("world"))       # False  ← lowercase 'w'
print(text.endswith("World"))       # True   ← uppercase 'W'

# ── Case-insensitive check: convert first ──
text = "GENOME_DATA.FASTA"

# ❌ Case-sensitive (might miss it):
print(text.endswith(".fasta"))      # False  ← FASTA is uppercase!

# ✅ Case-insensitive:
print(text.lower().endswith(".fasta"))      # True  ← convert both to lower
print(text.upper().endswith(".FASTA"))      # True  ← or convert to upper

# ── Real use case: file extension check ~~
filename = "DATA.CSV"
if filename.lower().endswith(".csv"):
    print("It's a CSV file!")       # ← this prints correctly


# ------------------------------------------------------------
# PART 5: Checking MULTIPLE prefixes/suffixes with a TUPLE
# ------------------------------------------------------------

# This is one of the most powerful features of these methods!
# You can pass a TUPLE of strings to check against.
# Returns True if the string matches ANY of them.
#
# Syntax:
#   string.startswith((prefix1, prefix2, prefix3))
#   string.endswith((suffix1, suffix2, suffix3))
#
# Note: it MUST be a TUPLE, not a list!
# (A list would cause TypeError)

# ── .endswith() with tuple - check multiple file types ~~
filename1 = "report.pdf"
filename2 = "data.csv"
filename3 = "script.py"
filename4 = "image.jpg"
filename5 = "archive.zip"

# Check if file is a document:
image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
print(filename1.endswith(image_extensions))     # False  ← PDF not an image
print(filename4.endswith(image_extensions))     # True   ← JPG is an image!

# Check if file is a data file:
data_extensions = (".csv", ".tsv", ".xlsx", ".json")
print(filename2.endswith(data_extensions))      # True   ← CSV is data!
print(filename1.endswith(data_extensions))      # False  ← PDF is not

# ── .startswith() with tuple - check multiple protocols ~~
url1 = "https://www.example.com"
url2 = "http://www.example.com"
url3 = "ftp://files.example.com"
url4 = "file:///home/user/doc.txt"

# Is it a web URL?
web_protocols = ("http://", "https://")
print(url1.startswith(web_protocols))   # True
print(url2.startswith(web_protocols))   # True
print(url3.startswith(web_protocols))   # False  ← FTP is not HTTP/HTTPS
print(url4.startswith(web_protocols))   # False  ← local file

# ── Check stop codons in DNA ──
dna = "ATGCCCGCATAA"
stop_codons = ("TAA", "TAG", "TGA")
print(dna.endswith(stop_codons))    # True  ← ends with TAA

dna2 = "ATGCCCGCATAG"
print(dna2.endswith(stop_codons))   # True  ← ends with TAG

dna3 = "ATGCCCGCAAAA"
print(dna3.endswith(stop_codons))   # False ← ends with AAAA

# ── IMPORTANT: tuple, not list! ~~
extensions = [".pdf", ".docx"]     # This is a LIST
# filename.endswith(extensions)    # ❌ TypeError!

extensions = (".pdf", ".docx")     # This is a TUPLE
print(filename1.endswith(extensions))   # ✅ True  ← works!


# ------------------------------------------------------------
# PART 6: The start parameter
# ------------------------------------------------------------

# .startswith(prefix, start) begins the check
# from position 'start' in the string.
# It's as if you're checking: string[start:].startswith(prefix)

text = "Hello World"
#       01234567890

# Normal check from the beginning:
print(text.startswith("Hello"))         # True

# Check from position 6 onward:
print(text.startswith("World", 6))      # True  ← "World" starts at 6
print(text.startswith("Hello", 6))      # False ← no "Hello" from pos 6

# Check from position 3:
print(text.startswith("lo", 3))         # True  ← "lo" at position 3
print(text.startswith("Hello", 3))      # False ← "Hello" not at position 3

# ── Practical use: check second word starts with capital ~~
sentence = "Hello World"
space_pos = sentence.find(" ") + 1      # position of second word
print(sentence.startswith("W", space_pos))  # True


# ------------------------------------------------------------
# PART 7: The start AND end parameters
# ------------------------------------------------------------

# .startswith(prefix, start, end) checks only within
# the substring string[start:end].

text = "Hello World Python"
#       012345678901234567

# Check "World" within positions [6:11]:
print(text.startswith("World", 6, 11))   # True  ← "World" is exactly [6:11]
print(text.startswith("World", 6, 10))   # False ← only "Worl" in [6:10]

# Check "Python" within positions [12:18]:
print(text.startswith("Python", 12, 18)) # True
print(text.startswith("Hello", 0, 5))    # True  ← "Hello" exactly in [0:5]
print(text.startswith("Hello", 0, 4))    # False ← only "Hell" in [0:4]

# .endswith() with start and end:
print(text.endswith("World", 0, 11))     # True  ← "World" ends [0:11]
print(text.endswith("Hello", 0, 5))      # True  ← "Hello" ends [0:5]
print(text.endswith("Python", 12))       # True  ← from 12 to end


# ------------------------------------------------------------
# PART 8: Empty string behavior
# ------------------------------------------------------------

# Any string "starts with" and "ends with" the empty string "".
# This is mathematically consistent: "" is a prefix/suffix of everything.

print("Hello".startswith(""))   # True
print("Hello".endswith(""))     # True
print("".startswith(""))        # True
print("".endswith(""))          # True

# This can cause unexpected behavior if you're not careful:
prefix = ""
text = "Hello World"
if text.startswith(prefix):
    print("Starts with prefix!")    # This always prints!

# Always make sure your prefix/suffix is meaningful.
# An empty prefix/suffix always returns True.


# ------------------------------------------------------------
# PART 9: Comparing .startswith()/.endswith() to alternatives
# ------------------------------------------------------------

# There are multiple ways to check prefixes/suffixes.
# Let's compare them:

filename = "report.pdf"

# ── Method 1: Slicing ~~
print(filename[:6] == "report")        # True
print(filename[-4:] == ".pdf")         # True

# ── Method 2: .find() ~~
print(filename.find("report") == 0)    # True
print(filename.rfind(".pdf") == len(filename) - 4)  # True

# ── Method 3: .startswith() / .endswith() ~~
print(filename.startswith("report"))   # True
print(filename.endswith(".pdf"))       # True

# Which is best?
# .startswith()/.endswith() → most READABLE and EXPRESSIVE
# Slicing → works but less clear what you're checking
# .find() → verbose and error-prone

# ── Performance note ~~
# .startswith() and .endswith() are also optimized by Python.
# They stop checking as soon as a mismatch is found.
# For long strings, this can be faster than slicing.

# ── When slicing has an advantage ~~
# If you need the actual prefix/suffix (not just True/False),
# use slicing. .startswith()/.endswith() only give you bool.
text = "https://www.example.com"
# Get the protocol:
colon = text.find("://")
protocol = text[:colon]     # "https"
# .startswith() can't give you the protocol - only True/False


# ------------------------------------------------------------
# PART 10: Combining with other string methods
# ------------------------------------------------------------

# .startswith() and .endswith() are often used with
# .strip(), .lower(), .split() and other methods.

# ── Strip then check ~~
raw = "  report.pdf  "
filename = raw.strip()
if filename.endswith(".pdf"):
    print("It's a PDF!")    # ← correct, spaces removed first

# ❌ Without strip:
if raw.endswith(".pdf"):
    print("Found")          # ← this would NOT print! trailing spaces!

# ── Lower then check ~~
filename = "Report.PDF"
if filename.lower().endswith(".pdf"):
    print("It's a PDF!")    # ← works regardless of case

# ── Use in filtering ~~
files = ["data.csv", "report.pdf", "script.py",
         "genome.fasta", "results.csv", "image.png"]

# Print only CSV files:
print("CSV files:")
for f in files:
    if f.endswith(".csv"):
        print(f"  {f}")

# Print only files NOT starting with "report":
print("Non-report files:")
for f in files:
    if not f.startswith("report"):
        print(f"  {f}")

# ── Use result in calculation ~~
urls = ["https://secure.com", "http://old.com",
        "https://shop.com", "ftp://files.com"]

secure_count = sum(1 for u in urls if u.startswith("https://"))
print(f"Secure URLs: {secure_count}")   # 2

# ── Combine startswith and endswith ~~
# Check if a string is a complete Python function definition:
code_line = "def calculate_gc_content():"
is_function = code_line.startswith("def ") and code_line.endswith(":")
print(f"Is function definition: {is_function}")     # True


# ------------------------------------------------------------
# PART 11: Boolean logic with startswith/endswith
# ------------------------------------------------------------

# Since both methods return booleans, you can use
# and, or, not with them freely.

filename = "genome_data.fasta"

# ── AND: both conditions must be true ~~
is_genome_fasta = (filename.startswith("genome") and
                   filename.endswith(".fasta"))
print(is_genome_fasta)      # True

# ── OR: either condition is true ~~
is_data_file = (filename.endswith(".fasta") or
                filename.endswith(".fastq") or
                filename.endswith(".fa"))
print(is_data_file)         # True  ← .fasta matches

# ── NOT: invert the result ~~
is_not_pdf = not filename.endswith(".pdf")
print(is_not_pdf)           # True  ← it's not a PDF

# ── Complex conditions ~~
url = "https://api.example.com/data"
is_secure_api = (url.startswith("https://") and
                 "/api/" in url and
                 not url.endswith(".html"))
print(is_secure_api)        # True

# ── Tuple OR logic ~~
# Using tuple is cleaner than multiple OR conditions:

# ❌ Verbose:
is_image = (filename.endswith(".jpg") or
            filename.endswith(".jpeg") or
            filename.endswith(".png") or
            filename.endswith(".gif"))

# ✅ Clean with tuple:
is_image = filename.endswith((".jpg", ".jpeg", ".png", ".gif"))
print(is_image)     # False  ← .fasta is not an image


# ------------------------------------------------------------
# PART 12: Real world applications
# ------------------------------------------------------------

# ── Application 1: File type classification ~~
def classify_file(filename):
    fn = filename.lower()
    if fn.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg")):
        return "Image"
    elif fn.endswith((".mp4", ".avi", ".mov", ".mkv", ".wmv")):
        return "Video"
    elif fn.endswith((".mp3", ".wav", ".flac", ".aac")):
        return "Audio"
    elif fn.endswith((".pdf", ".docx", ".doc", ".txt", ".odt")):
        return "Document"
    elif fn.endswith((".csv", ".xlsx", ".json", ".xml")):
        return "Data"
    elif fn.endswith((".py", ".js", ".java", ".cpp", ".c")):
        return "Code"
    elif fn.endswith((".fasta", ".fastq", ".fa", ".bam", ".vcf")):
        return "Bioinformatics"
    else:
        return "Unknown"

files = ["photo.jpg", "lecture.mp4", "genome.fasta",
         "data.csv", "script.py", "thesis.pdf", "song.mp3"]
for f in files:
    print(f"{f:<20} → {classify_file(f)}")

# ── Application 2: URL protocol handler ~~
def handle_url(url):
    if url.startswith("https://"):
        return f"Secure connection to: {url[8:]}"
    elif url.startswith("http://"):
        return f"Insecure connection to: {url[7:]}"
    elif url.startswith("ftp://"):
        return f"FTP transfer from: {url[6:]}"
    else:
        return f"Unknown protocol: {url}"

print(handle_url("https://www.python.org"))
print(handle_url("http://old-site.com"))
print(handle_url("ftp://files.example.com"))
print(handle_url("mailto:anna@example.com"))

# ── Application 3: DNA sequence validation ~~
def validate_dna(sequence):
    seq = sequence.upper()
    has_start = seq.startswith("ATG")
    has_stop  = seq.endswith(("TAA", "TAG", "TGA"))
    is_divisible = len(seq) % 3 == 0
    only_valid = all(c in "ATGC" for c in seq)  # preview

    print(f"Sequence: {seq}")
    print(f"  Has start codon (ATG): {has_start}")
    print(f"  Has stop codon:        {has_stop}")
    print(f"  Length divisible by 3: {is_divisible}")
    return has_start and has_stop and is_divisible

print(validate_dna("ATGCCCGCATAA"))    # True
print(validate_dna("ATGCCCGCAAAA"))    # False (no stop codon)
print(validate_dna("CCCGCATAATAG"))    # False (no start codon)

# ── Application 4: Comment detection in code ~~
lines = [
    "def hello():",
    "    # This is a comment",
    "    print('Hello')",
    "    # Another comment",
    "    return True",
    "# Module-level comment",
]

code_lines    = [l for l in lines if not l.strip().startswith("#")]
comment_lines = [l for l in lines if l.strip().startswith("#")]

print(f"Code lines:    {len(code_lines)}")      # 4
print(f"Comment lines: {len(comment_lines)}")   # 3 wait, let me recount
# Actually: line 2, 4, 6 are comments = 3

# ── Application 5: Email domain checker ~~
emails = ["anna@university.edu", "jan@gmail.com",
          "info@hospital.org", "research@mit.edu"]

edu_emails = [e for e in emails if e.endswith(".edu")]
print(f"Academic emails: {edu_emails}")

# ── Application 6: Python identifier check ~~
def is_private(name):
    return name.startswith("_") and not name.startswith("__")

def is_dunder(name):
    return name.startswith("__") and name.endswith("__")

def is_public(name):
    return not name.startswith("_")

names = ["hello", "_private", "__init__", "__dunder__",
         "_protected", "public_func", "__str__"]

for name in names:
    if is_dunder(name):
        print(f"{name:<20} → dunder/magic method")
    elif is_private(name):
        print(f"{name:<20} → private")
    else:
        print(f"{name:<20} → public")

# ── Application 7: Command parser ~~
def parse_command(command):
    cmd = command.strip().lower()
    if cmd.startswith("get "):
        return f"Fetching: {cmd[4:]}"
    elif cmd.startswith("delete "):
        return f"Deleting: {cmd[7:]}"
    elif cmd.startswith("update "):
        return f"Updating: {cmd[7:]}"
    elif cmd == "help":
        return "Showing help..."
    elif cmd == "quit" or cmd == "exit":
        return "Goodbye!"
    else:
        return f"Unknown command: {cmd}"

commands = ["get users", "delete record_42",
            "update profile", "help", "QUIT"]
for cmd in commands:
    print(parse_command(cmd))


# ------------------------------------------------------------
# PART 13: Performance tip - startswith vs slicing vs find
# ------------------------------------------------------------

# For checking prefixes/suffixes:
# .startswith()/.endswith() are optimized for this exact task.
# They are generally faster and cleaner than alternatives.

import timeit  # preview - don't worry about this yet

text = "Hello, this is a long string " * 100 + "Python"

# All three produce the same result (True/False)
# but .startswith()/.endswith() are the most readable
# and competitive in performance.

# Best practice: always use .startswith()/.endswith()
# for prefix/suffix checks. Reserve slicing for when
# you actually need the substring, not just the bool.

# ── When slicing IS the right choice ──
text = "Hello World"
# I need to EXTRACT the first 5 characters:
first_five = text[:5]           # ← use slicing!

# I need to CHECK if it starts with "Hello":
starts = text.startswith("Hello")   # ← use startswith!


# ------------------------------------------------------------
# PART 14: Edge cases
# ------------------------------------------------------------

# ── Prefix/suffix longer than the string ~~
word = "Hi"
print(word.startswith("Hello"))     # False  ← "Hello" longer than "Hi"
print(word.endswith("Hello"))       # False  ← same reason
print(word.startswith("Hi there"))  # False

# ── Exact match ~~
word = "Python"
print(word.startswith("Python"))    # True  ← exact match works!
print(word.endswith("Python"))      # True  ← exact match works!

# ── Single character ~~
word = "Python"
print(word.startswith("P"))         # True
print(word.endswith("n"))           # True
print(word.startswith("p"))         # False  ← case sensitive!

# ── Tuple with one element ~~
# A one-element tuple still works:
print("Hello".startswith(("H",)))   # True  ← tuple with one item
print("Hello".startswith(("H")))    # True  ← just a string (same here)

# ── Tuple with empty string ~~
print("Hello".startswith(("", "H")))   # True  ← "" always matches

# ── Overlapping prefix/suffix ~~
word = "abcabc"
print(word.startswith("abc"))   # True  ← first 3 chars
print(word.endswith("abc"))     # True  ← last 3 chars
# Both True! The string starts AND ends with "abc"


# ------------------------------------------------------------
# PART 15: Summary table
# ------------------------------------------------------------

# ┌───────────────────────┬──────────────────────────────────┐
# │ Method                │ Returns True when...             │
# ├───────────────────────┼──────────────────────────────────┤
# │ s.startswith(p)       │ s begins with prefix p           │
# │ s.startswith(p, i)    │ s[i:] begins with prefix p       │
# │ s.startswith(p, i, j) │ s[i:j] begins with prefix p      │
# │ s.startswith((p1,p2)) │ s begins with p1 OR p2           │
# ├───────────────────────┼──────────────────────────────────┤
# │ s.endswith(x)         │ s ends with suffix x             │
# │ s.endswith(x, i)      │ s[i:] ends with suffix x         │
# │ s.endswith(x, i, j)   │ s[i:j] ends with suffix x        │
# │ s.endswith((x1,x2))   │ s ends with x1 OR x2             │
# └───────────────────────┴──────────────────────────────────┘

# Key facts:
text = "Hello World"
print(text.startswith("Hello"))         # True
print(text.endswith("World"))           # True
print(text.startswith(("Hi", "Hello"))) # True  ← tuple!
print(text.endswith(("Earth", "World")))# True  ← tuple!
print(text.startswith(""))              # True  ← empty always True
print(text.endswith(""))                # True  ← empty always True


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ .startswith(prefix) → True if string BEGINS with prefix
# ✅ .endswith(suffix)   → True if string ENDS with suffix
# ✅ Both return BOOLEAN: True or False, ALWAYS
# ✅ Both are CASE SENSITIVE
# ✅ Case-insensitive: use .lower().startswith() or .upper()
# ✅ Pass a TUPLE to check multiple prefixes/suffixes at once
# ✅ Tuple returns True if ANY of the options match
# ✅ MUST be tuple (not list) for multiple options → TypeError otherwise
# ✅ .startswith("") → always True (empty prefix)
# ✅ .endswith("") → always True (empty suffix)
# ✅ start/end parameters: limit the check to a substring
# ✅ More readable than slicing or .find() for prefix/suffix checks
# ✅ Combine with 'not' to check what string does NOT start/end with
# ✅ Combine with 'and'/'or' for complex conditions
# ✅ Classic uses: file extensions, URL protocols, DNA codons