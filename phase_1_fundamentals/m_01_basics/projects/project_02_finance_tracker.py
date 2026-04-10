# ============================================================
# MODULE 01 | PROJECT 02 - Personal Finance Tracker
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
# All financial data is stored in individual variables.
# All calculations use only arithmetic and string operators.
# All output uses f-strings and print().
# NO functions, NO if statements, NO loops, NO imports.
# ============================================================


# ============================================================
# PROGRAM HEADER
# ============================================================

PROGRAM_NAME  = "Personal Finance Tracker"
VERSION       = "1.0.0"
PERIOD        = "January 2025"
CURRENCY      = "PLN"
WIDTH         = 64

print(f"{'╔' + '═' * (WIDTH - 2) + '╗'}")
print(f"║ {PROGRAM_NAME:^{WIDTH - 4}} ║")
print(f"║ {'Version ' + VERSION:^{WIDTH - 4}} ║")
print(f"║ {'Period: ' + PERIOD:^{WIDTH - 4}} ║")
print(f"{'╚' + '═' * (WIDTH - 2) + '╝'}")


# ============================================================
# SECTION 1: INCOME TRANSACTIONS
# ============================================================
# Tests: variables, numbers, strings, type conversion

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 1: INCOME")
print(f"{'─' * WIDTH}")

# Each transaction: date, description, amount, category
income_date_1   = "2025-01-01"
income_desc_1   = "Monthly salary"
income_amount_1 = 8500.00
income_cat_1    = "salary"

income_date_2   = "2025-01-15"
income_desc_2   = "Freelance Python project"
income_amount_2 = 1200.00
income_cat_2    = "freelance"

income_date_3   = "2025-01-20"
income_desc_3   = "Stock dividend"
income_amount_3 = 150.00
income_cat_3    = "investment"

income_date_4   = "2025-01-25"
income_desc_4   = "Birthday gift"
income_amount_4 = 200.00
income_cat_4    = "gift"

# Calculate totals by category
total_salary     = income_amount_1
total_freelance  = income_amount_2
total_investment = income_amount_3
total_gift       = income_amount_4

# Grand total income
total_income = (
    income_amount_1 +
    income_amount_2 +
    income_amount_3 +
    income_amount_4
)

# Transaction count
income_count = 4

print(f"\n  {'Date':<12} {'Description':<28} {'Category':<14} {'Amount':>10}")
print(f"  {'─' * 66}")
print(f"  {income_date_1:<12} {income_desc_1:<28} {income_cat_1:<14} {income_amount_1:>10,.2f}")
print(f"  {income_date_2:<12} {income_desc_2:<28} {income_cat_2:<14} {income_amount_2:>10,.2f}")
print(f"  {income_date_3:<12} {income_desc_3:<28} {income_cat_3:<14} {income_amount_3:>10,.2f}")
print(f"  {income_date_4:<12} {income_desc_4:<28} {income_cat_4:<14} {income_amount_4:>10,.2f}")
print(f"  {'─' * 66}")
print(f"  {'TOTAL INCOME':<56} {total_income:>10,.2f}")
print(f"  {'Transactions':<56} {income_count:>10}")


# ============================================================
# SECTION 2: EXPENSE TRANSACTIONS
# ============================================================
# Tests: variables, numbers, strings, math operators

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 2: EXPENSES")
print(f"{'─' * WIDTH}")

# --- HOUSING ---
exp_housing_1_date   = "2025-01-01"
exp_housing_1_desc   = "Rent"
exp_housing_1_amount = 2200.00
exp_housing_1_cat    = "housing"

# --- UTILITIES ---
exp_util_1_date   = "2025-01-01"
exp_util_1_desc   = "Internet"
exp_util_1_amount = 89.99
exp_util_1_cat    = "utilities"

exp_util_2_date   = "2025-01-01"
exp_util_2_desc   = "Phone plan"
exp_util_2_amount = 49.99
exp_util_2_cat    = "utilities"

# --- SUBSCRIPTIONS ---
exp_sub_1_date   = "2025-01-01"
exp_sub_1_desc   = "Netflix"
exp_sub_1_amount = 49.00
exp_sub_1_cat    = "subscriptions"

exp_sub_2_date   = "2025-01-01"
exp_sub_2_desc   = "Spotify"
exp_sub_2_amount = 23.99
exp_sub_2_cat    = "subscriptions"

# --- FOOD ---
exp_food_1_date   = "2025-01-02"
exp_food_1_desc   = "Grocery shopping"
exp_food_1_amount = 320.50
exp_food_1_cat    = "food"

exp_food_2_date   = "2025-01-07"
exp_food_2_desc   = "Restaurant dinner"
exp_food_2_amount = 85.00
exp_food_2_cat    = "food"

exp_food_3_date   = "2025-01-10"
exp_food_3_desc   = "Coffee shop"
exp_food_3_amount = 42.50
exp_food_3_cat    = "food"

exp_food_4_date   = "2025-01-14"
exp_food_4_desc   = "Grocery shopping"
exp_food_4_amount = 280.30
exp_food_4_cat    = "food"

exp_food_5_date   = "2025-01-18"
exp_food_5_desc   = "Pizza delivery"
exp_food_5_amount = 55.00
exp_food_5_cat    = "food"

exp_food_6_date   = "2025-01-21"
exp_food_6_desc   = "Grocery shopping"
exp_food_6_amount = 195.80
exp_food_6_cat    = "food"

exp_food_7_date   = "2025-01-28"
exp_food_7_desc   = "Grocery shopping"
exp_food_7_amount = 310.20
exp_food_7_cat    = "food"

# --- TRANSPORT ---
exp_trans_1_date   = "2025-01-03"
exp_trans_1_desc   = "Monthly bus pass"
exp_trans_1_amount = 110.00
exp_trans_1_cat    = "transport"

exp_trans_2_date   = "2025-01-12"
exp_trans_2_desc   = "Uber ride"
exp_trans_2_amount = 35.50
exp_trans_2_cat    = "transport"

exp_trans_3_date   = "2025-01-19"
exp_trans_3_desc   = "Fuel"
exp_trans_3_amount = 180.00
exp_trans_3_cat    = "transport"

exp_trans_4_date   = "2025-01-25"
exp_trans_4_desc   = "Car parking"
exp_trans_4_amount = 45.00
exp_trans_4_cat    = "transport"

# --- ENTERTAINMENT ---
exp_ent_1_date   = "2025-01-06"
exp_ent_1_desc   = "Cinema tickets"
exp_ent_1_amount = 60.00
exp_ent_1_cat    = "entertainment"

exp_ent_2_date   = "2025-01-13"
exp_ent_2_desc   = "Video game"
exp_ent_2_amount = 79.99
exp_ent_2_cat    = "entertainment"

exp_ent_3_date   = "2025-01-20"
exp_ent_3_desc   = "Concert tickets"
exp_ent_3_amount = 150.00
exp_ent_3_cat    = "entertainment"

exp_ent_4_date   = "2025-01-27"
exp_ent_4_desc   = "Books"
exp_ent_4_amount = 89.99
exp_ent_4_cat    = "entertainment"

# --- HEALTHCARE ---
exp_health_1_date   = "2025-01-01"
exp_health_1_desc   = "Gym membership"
exp_health_1_amount = 99.00
exp_health_1_cat    = "healthcare"

exp_health_2_date   = "2025-01-08"
exp_health_2_desc   = "Doctor visit"
exp_health_2_amount = 150.00
exp_health_2_cat    = "healthcare"

exp_health_3_date   = "2025-01-09"
exp_health_3_desc   = "Pharmacy"
exp_health_3_amount = 67.50
exp_health_3_cat    = "healthcare"

# --- EDUCATION ---
exp_edu_1_date   = "2025-01-05"
exp_edu_1_desc   = "Online course"
exp_edu_1_amount = 199.00
exp_edu_1_cat    = "education"

exp_edu_2_date   = "2025-01-15"
exp_edu_2_desc   = "Technical book"
exp_edu_2_amount = 59.99
exp_edu_2_cat    = "education"

# --- CLOTHING ---
exp_cloth_1_date   = "2025-01-11"
exp_cloth_1_desc   = "Winter jacket"
exp_cloth_1_amount = 399.00
exp_cloth_1_cat    = "clothing"

exp_cloth_2_date   = "2025-01-22"
exp_cloth_2_desc   = "Running shoes"
exp_cloth_2_amount = 299.00
exp_cloth_2_cat    = "clothing"

# --- OTHER ---
exp_other_1_date   = "2025-01-16"
exp_other_1_desc   = "Haircut"
exp_other_1_amount = 80.00
exp_other_1_cat    = "other"

exp_other_2_date   = "2025-01-24"
exp_other_2_desc   = "Household items"
exp_other_2_amount = 145.50
exp_other_2_cat    = "other"

# --- CATEGORY TOTALS ---
total_housing      = exp_housing_1_amount
total_utilities    = exp_util_1_amount    + exp_util_2_amount
total_subscriptions= exp_sub_1_amount    + exp_sub_2_amount
total_food         = (exp_food_1_amount  + exp_food_2_amount +
                      exp_food_3_amount  + exp_food_4_amount +
                      exp_food_5_amount  + exp_food_6_amount +
                      exp_food_7_amount)
total_transport    = (exp_trans_1_amount + exp_trans_2_amount +
                      exp_trans_3_amount + exp_trans_4_amount)
total_entertainment= (exp_ent_1_amount   + exp_ent_2_amount +
                      exp_ent_3_amount   + exp_ent_4_amount)
total_healthcare   = (exp_health_1_amount + exp_health_2_amount +
                      exp_health_3_amount)
total_education    = exp_edu_1_amount    + exp_edu_2_amount
total_clothing     = exp_cloth_1_amount  + exp_cloth_2_amount
total_other        = exp_other_1_amount  + exp_other_2_amount

# Grand total expenses
total_expenses = (
    total_housing       +
    total_utilities     +
    total_subscriptions +
    total_food          +
    total_transport     +
    total_entertainment +
    total_healthcare    +
    total_education     +
    total_clothing      +
    total_other
)

expense_count = 28

print(f"\n  Expense Summary by Category:")
print(f"  {'─' * 40}")
print(f"  {'Category':<18} {'Amount':>12} {'Count':>6}")
print(f"  {'─' * 40}")
print(f"  {'Housing':<18} {total_housing:>12,.2f} {1:>6}")
print(f"  {'Utilities':<18} {total_utilities:>12,.2f} {2:>6}")
print(f"  {'Subscriptions':<18} {total_subscriptions:>12,.2f} {2:>6}")
print(f"  {'Food':<18} {total_food:>12,.2f} {7:>6}")
print(f"  {'Transport':<18} {total_transport:>12,.2f} {4:>6}")
print(f"  {'Entertainment':<18} {total_entertainment:>12,.2f} {4:>6}")
print(f"  {'Healthcare':<18} {total_healthcare:>12,.2f} {3:>6}")
print(f"  {'Education':<18} {total_education:>12,.2f} {2:>6}")
print(f"  {'Clothing':<18} {total_clothing:>12,.2f} {2:>6}")
print(f"  {'Other':<18} {total_other:>12,.2f} {2:>6}")
print(f"  {'─' * 40}")
print(f"  {'TOTAL':<18} {total_expenses:>12,.2f} {expense_count:>6}")


# ============================================================
# SECTION 3: FINANCIAL OVERVIEW
# ============================================================
# Tests: math operators, comparisons, booleans, f-strings

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 3: FINANCIAL OVERVIEW")
print(f"{'─' * WIDTH}")

# Core calculations
net_savings   = total_income - total_expenses
savings_rate  = net_savings / total_income * 100
expense_ratio = total_expenses / total_income * 100

# Tax calculation (19% flat tax on income)
tax_rate      = 0.19
tax_amount    = total_income * tax_rate
net_income    = total_income - tax_amount
after_tax_savings = net_income - total_expenses

# Daily averages (January = 31 days)
days_in_month       = 31
daily_income        = total_income  / days_in_month
daily_expenses      = total_expenses / days_in_month
daily_savings       = net_savings   / days_in_month

# Annual projections
annual_income       = total_income   * 12
annual_expenses     = total_expenses * 12
annual_savings      = net_savings    * 12

# Financial health checks (booleans)
is_saving_money    = net_savings > 0
is_good_savings    = savings_rate >= 20.0     # 20% savings rate is good
is_affordable      = expense_ratio <= 70.0    # spending < 70% of income
is_tax_efficient   = net_income > total_expenses
has_emergency_fund = net_savings >= (total_expenses * 3)  # 3 months expenses

# Progress bars (using string multiplication - no loops!)
bar_width      = 25
savings_ratio  = min(savings_rate / 100, 1.0)
expense_ratio2 = min(expense_ratio / 100, 1.0)
savings_filled = int(savings_ratio * bar_width)
expense_filled = int(expense_ratio2 * bar_width)
savings_bar    = "█" * savings_filled + "░" * (bar_width - savings_filled)
expense_bar    = "█" * expense_filled + "░" * (bar_width - expense_filled)

print(f"""
  ╔══════════════════════════════════════════════════════════╗
  ║              MONTHLY FINANCIAL SUMMARY                  ║
  ╠══════════════════════════════════════════════════════════╣
  ║  INCOME & EXPENSES                                      ║
  ║  Total Income   : {total_income:>12,.2f} {CURRENCY}                    ║
  ║  Total Expenses : {total_expenses:>12,.2f} {CURRENCY}                    ║
  ║  Net Savings    : {net_savings:>12,.2f} {CURRENCY}                    ║
  ╠══════════════════════════════════════════════════════════╣
  ║  SAVINGS RATE                                           ║
  ║  [{savings_bar}] {savings_rate:5.1f}%            ║
  ║  EXPENSE RATIO                                          ║
  ║  [{expense_bar}] {expense_ratio:5.1f}%            ║
  ╠══════════════════════════════════════════════════════════╣
  ║  TAX CALCULATION (19% flat rate)                        ║
  ║  Gross Income   : {total_income:>12,.2f} {CURRENCY}                    ║
  ║  Tax Amount     : {tax_amount:>12,.2f} {CURRENCY}                    ║
  ║  Net Income     : {net_income:>12,.2f} {CURRENCY}                    ║
  ║  After-tax save : {after_tax_savings:>12,.2f} {CURRENCY}                    ║
  ╠══════════════════════════════════════════════════════════╣
  ║  DAILY AVERAGES                                         ║
  ║  Daily income   : {daily_income:>12,.2f} {CURRENCY}                    ║
  ║  Daily expenses : {daily_expenses:>12,.2f} {CURRENCY}                    ║
  ║  Daily savings  : {daily_savings:>12,.2f} {CURRENCY}                    ║
  ╠══════════════════════════════════════════════════════════╣
  ║  ANNUAL PROJECTIONS                                     ║
  ║  Annual income  : {annual_income:>12,.2f} {CURRENCY}                    ║
  ║  Annual expenses: {annual_expenses:>12,.2f} {CURRENCY}                    ║
  ║  Annual savings : {annual_savings:>12,.2f} {CURRENCY}                    ║
  ╚══════════════════════════════════════════════════════════╝
""")


# ============================================================
# SECTION 4: BUDGET TRACKING
# ============================================================
# Tests: math operators, comparisons, booleans, f-strings

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 4: BUDGET TRACKING")
print(f"{'─' * WIDTH}")

# Monthly budget limits
budget_housing      = 2300.00
budget_utilities    = 200.00
budget_subs         = 150.00
budget_food         = 1000.00
budget_transport    = 400.00
budget_entertainment= 300.00
budget_healthcare   = 300.00
budget_education    = 300.00
budget_clothing     = 400.00
budget_other        = 300.00

# Budget usage (spent / budget * 100)
usage_housing       = total_housing       / budget_housing       * 100
usage_utilities     = total_utilities     / budget_utilities     * 100
usage_subs          = total_subscriptions / budget_subs          * 100
usage_food          = total_food          / budget_food          * 100
usage_transport     = total_transport     / budget_transport     * 100
usage_entertainment = total_entertainment / budget_entertainment * 100
usage_healthcare    = total_healthcare    / budget_healthcare    * 100
usage_education     = total_education     / budget_education     * 100
usage_clothing      = total_clothing      / budget_clothing      * 100
usage_other         = total_other         / budget_other         * 100

# Remaining budget
rem_housing       = budget_housing       - total_housing
rem_utilities     = budget_utilities     - total_utilities
rem_subs          = budget_subs          - total_subscriptions
rem_food          = budget_food          - total_food
rem_transport     = budget_transport     - total_transport
rem_entertainment = budget_entertainment - total_entertainment
rem_healthcare    = budget_healthcare    - total_healthcare
rem_education     = budget_education     - total_education
rem_clothing      = budget_clothing      - total_clothing
rem_other         = budget_other         - total_other

# Status booleans
ok_housing       = usage_housing       <= 80.0
ok_utilities     = usage_utilities     <= 80.0
ok_subs          = usage_subs          <= 80.0
ok_food          = usage_food          <= 80.0
ok_transport     = usage_transport     <= 80.0
ok_entertainment = usage_entertainment <= 80.0
ok_healthcare    = usage_healthcare    <= 80.0
ok_education     = usage_education     <= 80.0
ok_clothing      = usage_clothing      <= 80.0
ok_other         = usage_other         <= 80.0

warn_housing       = usage_housing       > 80.0 and usage_housing       <= 95.0
warn_food          = usage_food          > 80.0 and usage_food          <= 95.0
warn_transport     = usage_transport     > 80.0 and usage_transport     <= 95.0
warn_entertainment = usage_entertainment > 80.0 and usage_entertainment <= 95.0
warn_healthcare    = usage_healthcare    > 80.0 and usage_healthcare    <= 95.0
warn_clothing      = usage_clothing      > 80.0 and usage_clothing      <= 95.0

over_housing       = usage_housing       > 100.0
over_food          = usage_food          > 100.0
over_transport     = usage_transport     > 100.0
over_entertainment = usage_entertainment > 100.0
over_clothing      = usage_clothing      > 100.0

# Status symbols (ternary in f-string)
status_housing       = "✗ OVER" if over_housing       else ("⚠ WARN" if warn_housing       else "✓ OK  ")
status_utilities     = "✓ OK  "
status_subs          = "✓ OK  "
status_food          = "✗ OVER" if over_food          else ("⚠ WARN" if warn_food          else "✓ OK  ")
status_transport     = "✗ OVER" if over_transport     else ("⚠ WARN" if warn_transport     else "✓ OK  ")
status_entertainment = "✗ OVER" if over_entertainment else ("⚠ WARN" if warn_entertainment else "✓ OK  ")
status_healthcare    = "✓ OK  " if ok_healthcare else ("⚠ WARN" if warn_healthcare else "✗ OVER")
status_education     = "✓ OK  " if ok_education  else "⚠ WARN"
status_clothing      = "✗ OVER" if over_clothing      else ("⚠ WARN" if warn_clothing      else "✓ OK  ")
status_other         = "✓ OK  "

# Progress bars for each category
bw = 15
bar_housing       = "█" * int(min(usage_housing,100)/100*bw)       + "░" * (bw - int(min(usage_housing,100)/100*bw))
bar_utilities     = "█" * int(min(usage_utilities,100)/100*bw)     + "░" * (bw - int(min(usage_utilities,100)/100*bw))
bar_subs          = "█" * int(min(usage_subs,100)/100*bw)          + "░" * (bw - int(min(usage_subs,100)/100*bw))
bar_food          = "█" * int(min(usage_food,100)/100*bw)          + "░" * (bw - int(min(usage_food,100)/100*bw))
bar_transport     = "█" * int(min(usage_transport,100)/100*bw)     + "░" * (bw - int(min(usage_transport,100)/100*bw))
bar_entertainment = "█" * int(min(usage_entertainment,100)/100*bw) + "░" * (bw - int(min(usage_entertainment,100)/100*bw))
bar_healthcare    = "█" * int(min(usage_healthcare,100)/100*bw)    + "░" * (bw - int(min(usage_healthcare,100)/100*bw))
bar_education     = "█" * int(min(usage_education,100)/100*bw)     + "░" * (bw - int(min(usage_education,100)/100*bw))
bar_clothing      = "█" * int(min(usage_clothing,100)/100*bw)      + "░" * (bw - int(min(usage_clothing,100)/100*bw))
bar_other         = "█" * int(min(usage_other,100)/100*bw)         + "░" * (bw - int(min(usage_other,100)/100*bw))

print(f"\n  {'Category':<14} {'Spent':>9} {'Budget':>9} {'Bar':<17} {'Used':>7} {'Status'}")
print(f"  {'─' * 70}")
print(f"  {'Housing':<14} {total_housing:>9,.2f} {budget_housing:>9,.2f} [{bar_housing}] {usage_housing:>6.1f}% {status_housing}")
print(f"  {'Utilities':<14} {total_utilities:>9,.2f} {budget_utilities:>9,.2f} [{bar_utilities}] {usage_utilities:>6.1f}% {status_utilities}")
print(f"  {'Subscriptions':<14} {total_subscriptions:>9,.2f} {budget_subs:>9,.2f} [{bar_subs}] {usage_subs:>6.1f}% {status_subs}")
print(f"  {'Food':<14} {total_food:>9,.2f} {budget_food:>9,.2f} [{bar_food}] {usage_food:>6.1f}% {status_food}")
print(f"  {'Transport':<14} {total_transport:>9,.2f} {budget_transport:>9,.2f} [{bar_transport}] {usage_transport:>6.1f}% {status_transport}")
print(f"  {'Entertainment':<14} {total_entertainment:>9,.2f} {budget_entertainment:>9,.2f} [{bar_entertainment}] {usage_entertainment:>6.1f}% {status_entertainment}")
print(f"  {'Healthcare':<14} {total_healthcare:>9,.2f} {budget_healthcare:>9,.2f} [{bar_healthcare}] {usage_healthcare:>6.1f}% {status_healthcare}")
print(f"  {'Education':<14} {total_education:>9,.2f} {budget_education:>9,.2f} [{bar_education}] {usage_education:>6.1f}% {status_education}")
print(f"  {'Clothing':<14} {total_clothing:>9,.2f} {budget_clothing:>9,.2f} [{bar_clothing}] {usage_clothing:>6.1f}% {status_clothing}")
print(f"  {'Other':<14} {total_other:>9,.2f} {budget_other:>9,.2f} [{bar_other}] {usage_other:>6.1f}% {status_other}")
print(f"  {'─' * 70}")

total_budget = (budget_housing + budget_utilities + budget_subs +
                budget_food + budget_transport + budget_entertainment +
                budget_healthcare + budget_education + budget_clothing +
                budget_other)
total_usage  = total_expenses / total_budget * 100
print(f"  {'TOTAL':<14} {total_expenses:>9,.2f} {total_budget:>9,.2f} {'':17} {total_usage:>6.1f}%")


# ============================================================
# SECTION 5: STATISTICAL ANALYSIS
# ============================================================
# Tests: math operators, numbers, comparisons, f-strings

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 5: STATISTICAL ANALYSIS")
print(f"{'─' * WIDTH}")

# Expense category amounts (for statistics)
# Manually list all category totals
cat_min = total_subscriptions   # smallest category
cat_max = total_housing          # largest category

# Sum of all categories (= total_expenses, verification)
cat_sum_check = (
    total_housing + total_utilities + total_subscriptions +
    total_food + total_transport + total_entertainment +
    total_healthcare + total_education + total_clothing +
    total_other
)
cat_count     = 10
cat_mean      = total_expenses / cat_count

# Median: sort manually (we know the order)
# Sorted ascending: subscriptions, utilities, other, education,
#                   transport, entertainment, healthcare, food,
#                   clothing, housing
# subscriptions=72.99, utilities=139.98, other=225.50, education=258.99
# transport=370.50, entertainment=379.98, healthcare=316.50
# food=1289.30, clothing=698.00, housing=2200.00
# Sorted: 72.99, 139.98, 225.50, 258.99, 316.50, 370.50, 379.98, 698.00, 1289.30, 2200.00
# Median of 10 = average of 5th and 6th = (316.50 + 370.50) / 2
median_5th = total_healthcare   # 316.50
median_6th = total_transport    # 370.50
cat_median = (median_5th + median_6th) / 2

# Range
cat_range = cat_max - cat_min

# Largest and smallest single transactions
# Largest: Rent (2200.00)
# Smallest: Spotify (23.99)
largest_amount  = exp_housing_1_amount
largest_desc    = exp_housing_1_desc
smallest_amount = exp_sub_2_amount
smallest_desc   = exp_sub_2_desc

# Count over-budget categories
over_budget_count = int(over_housing) + int(over_food) + int(over_clothing)
warn_count        = int(warn_transport) + int(warn_entertainment)
ok_count          = cat_count - over_budget_count - warn_count

# Income distribution
salary_pct     = total_salary     / total_income * 100
freelance_pct  = total_freelance  / total_income * 100
investment_pct = total_investment / total_income * 100
gift_pct       = total_gift       / total_income * 100

print(f"\n  EXPENSE CATEGORY STATISTICS:")
print(f"  {'─' * 42}")
print(f"  Count        : {cat_count} categories")
print(f"  Total        : {total_expenses:>10,.2f} {CURRENCY}")
print(f"  Mean         : {cat_mean:>10,.2f} {CURRENCY}")
print(f"  Median       : {cat_median:>10,.2f} {CURRENCY}")
print(f"  Minimum      : {cat_min:>10,.2f} {CURRENCY}  ({total_subscriptions:.2f} - subscriptions)")
print(f"  Maximum      : {cat_max:>10,.2f} {CURRENCY}  ({total_housing:.2f} - housing)")
print(f"  Range        : {cat_range:>10,.2f} {CURRENCY}")
print(f"  Verification : {cat_sum_check:>10,.2f} {CURRENCY}  (matches total: {cat_sum_check == total_expenses})")

print(f"\n  SINGLE TRANSACTION EXTREMES:")
print(f"  Largest  : {largest_desc:<28} {largest_amount:>10,.2f} {CURRENCY}")
print(f"  Smallest : {smallest_desc:<28} {smallest_amount:>10,.2f} {CURRENCY}")
print(f"  Ratio    : {largest_amount/smallest_amount:.1f}x difference")

print(f"\n  INCOME DISTRIBUTION:")
print(f"  {'─' * 42}")
bar_sal  = "█" * int(salary_pct/100*20)     + "░" * (20 - int(salary_pct/100*20))
bar_free = "█" * int(freelance_pct/100*20)  + "░" * (20 - int(freelance_pct/100*20))
bar_inv  = "█" * int(investment_pct/100*20) + "░" * (20 - int(investment_pct/100*20))
bar_gift = "█" * int(gift_pct/100*20)       + "░" * (20 - int(gift_pct/100*20))
print(f"  salary     [{bar_sal}] {salary_pct:5.1f}%  {total_salary:>9,.2f} {CURRENCY}")
print(f"  freelance  [{bar_free}] {freelance_pct:5.1f}%  {total_freelance:>9,.2f} {CURRENCY}")
print(f"  investment [{bar_inv}] {investment_pct:5.1f}%  {total_investment:>9,.2f} {CURRENCY}")
print(f"  gift       [{bar_gift}] {gift_pct:5.1f}%  {total_gift:>9,.2f} {CURRENCY}")


# ============================================================
# SECTION 6: FINANCIAL HEALTH REPORT
# ============================================================
# Tests: booleans, logical operators, comparisons, f-strings

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 6: FINANCIAL HEALTH REPORT")
print(f"{'─' * WIDTH}")

# Health checks
is_saving_money    = net_savings > 0
is_good_savings    = savings_rate >= 20.0
is_tax_efficient   = net_income > total_expenses
housing_affordable = total_housing / total_income <= 0.30  # 30% rule
has_food_issue     = over_food
has_clothing_issue = over_clothing
total_budget_ok    = total_usage <= 100.0

# Health score (out of 10 points)
score = (
    int(is_saving_money)    * 2 +  # 2 points for saving anything
    int(is_good_savings)    * 2 +  # 2 points for 20%+ savings rate
    int(housing_affordable) * 2 +  # 2 points for housing < 30% income
    int(total_budget_ok)    * 2 +  # 2 points for total under budget
    int(not has_food_issue) * 1 +  # 1 point for food on budget
    int(not has_clothing_issue) * 1  # 1 point for clothing on budget
)

# Score bar
score_bar  = "★" * score + "☆" * (10 - score)
score_text = (
    "Excellent!" if score >= 9 else
    "Good"       if score >= 7 else
    "Fair"       if score >= 5 else
    "Needs work" if score >= 3 else
    "Critical"
)

# Overspending details
food_over_amount     = total_food     - budget_food     if over_food     else 0
clothing_over_amount = total_clothing - budget_clothing if over_clothing else 0
total_over           = food_over_amount + clothing_over_amount

# How many months to reach emergency fund (3 months expenses)?
emergency_fund_target = total_expenses * 3
months_to_emergency   = (
    emergency_fund_target / net_savings if net_savings > 0 else 999
)

print(f"""
  ┌─────────────────────────────────────────────────────┐
  │              FINANCIAL HEALTH SCORECARD             │
  ├─────────────────────────────────────────────────────┤
  │  Score: {score}/10  {score_bar}  {score_text:<12}     │
  ├─────────────────────────────────────────────────────┤
  │  CHECKS                                             │
  │  Saving money         : {'✓ YES' if is_saving_money    else '✗ NO '} ({net_savings:>+10,.2f} {CURRENCY})  │
  │  Good savings rate    : {'✓ YES' if is_good_savings    else '✗ NO '} ({savings_rate:>8.1f}%)     │
  │  Tax efficient        : {'✓ YES' if is_tax_efficient   else '✗ NO '}                        │
  │  Housing affordable   : {'✓ YES' if housing_affordable else '✗ NO '} ({total_housing/total_income*100:.0f}% of income) │
  │  Total under budget   : {'✓ YES' if total_budget_ok    else '✗ NO '} ({total_usage:.1f}% of budget) │
  │  Food on budget       : {'✓ YES' if not has_food_issue else '✗ NO '} ({usage_food:.1f}% used)    │
  │  Clothing on budget   : {'✓ YES' if not has_clothing_issue else '✗ NO '} ({usage_clothing:.1f}% used)  │
  ├─────────────────────────────────────────────────────┤
  │  ISSUES                                             │
  │  Over-budget categories : {over_budget_count}                           │
  │  Warning categories     : {warn_count}                           │
  │  OK categories          : {ok_count}                           │
  │  Total overspending     : {total_over:>10,.2f} {CURRENCY}             │
  ├─────────────────────────────────────────────────────┤
  │  GOALS                                              │
  │  Emergency fund target  : {emergency_fund_target:>10,.2f} {CURRENCY}             │
  │  Months to reach it     : {months_to_emergency:>10.1f} months             │
  │  Annual savings goal    : {annual_savings:>10,.2f} {CURRENCY}             │
  └─────────────────────────────────────────────────────┘
""")


# ============================================================
# SECTION 7: RECOMMENDATIONS
# ============================================================
# Tests: booleans, logical operators, f-strings, strings

print(f"\n{'─' * WIDTH}")
print(f"  SECTION 7: RECOMMENDATIONS")
print(f"{'─' * WIDTH}")

# Build recommendation strings using bool expressions
rec_food = (
    f"  ⚠  FOOD: Over budget by {food_over_amount:,.2f} {CURRENCY}. "
    f"Target: reduce by {food_over_amount/7:.2f} {CURRENCY}/week."
    if has_food_issue else
    f"  ✓  FOOD: Within budget. {rem_food:,.2f} {CURRENCY} remaining."
)

rec_clothing = (
    f"  ⚠  CLOTHING: Over budget by {clothing_over_amount:,.2f} {CURRENCY}. "
    f"Avoid clothing purchases next month."
    if has_clothing_issue else
    f"  ✓  CLOTHING: Within budget. {rem_clothing:,.2f} {CURRENCY} remaining."
)

rec_savings = (
    f"  ✓  SAVINGS: Good rate of {savings_rate:.1f}%. Keep it up!"
    if is_good_savings else
    f"  ⚠  SAVINGS: Rate of {savings_rate:.1f}% is below 20% target. "
    f"Need {total_income * 0.20 - net_savings:,.2f} {CURRENCY} more monthly."
)

rec_emergency = (
    f"  ✓  EMERGENCY FUND: On track - {months_to_emergency:.0f} months to target."
    if months_to_emergency <= 6 else
    f"  ⚠  EMERGENCY FUND: {months_to_emergency:.1f} months to reach target. "
    f"Consider increasing savings."
)

rec_housing = (
    f"  ✓  HOUSING: Cost is {total_housing/total_income*100:.0f}% of income (under 30% rule)."
    if housing_affordable else
    f"  ⚠  HOUSING: Cost is {total_housing/total_income*100:.0f}% of income (over 30% rule)."
)

rec_overall = (
    f"  ✓  OVERALL: Excellent financial health! Score {score}/10."
    if score >= 8 else
    f"  ⚠  OVERALL: Good but room for improvement. Score {score}/10."
    if score >= 6 else
    f"  ✗  OVERALL: Significant improvements needed. Score {score}/10."
)

print()
print(rec_food)
print(rec_clothing)
print(rec_savings)
print(rec_emergency)
print(rec_housing)
print()
print(f"  {'─' * 55}")
print(rec_overall)

# Potential savings if food and clothing were on budget
potential_monthly = food_over_amount + clothing_over_amount
potential_annual  = potential_monthly * 12
print(f"\n  💡 If food and clothing were on budget:")
print(f"     Monthly savings would increase by {potential_monthly:,.2f} {CURRENCY}")
print(f"     Annual savings would increase by  {potential_annual:,.2f} {CURRENCY}")


# ============================================================
# FINAL SUMMARY
# ============================================================

print(f"\n{'╔' + '═' * (WIDTH - 2) + '╗'}")
print(f"║ {'FINAL SUMMARY - ' + PERIOD:^{WIDTH - 4}} ║")
print(f"{'╠' + '═' * (WIDTH - 2) + '╣'}")
print(f"║  {'Total Income':<28} {total_income:>14,.2f} {CURRENCY}  ║")
print(f"║  {'Total Expenses':<28} {total_expenses:>14,.2f} {CURRENCY}  ║")
print(f"║  {'Net Savings':<28} {net_savings:>14,.2f} {CURRENCY}  ║")
print(f"║  {'Savings Rate':<28} {savings_rate:>14.1f}%      ║")
print(f"║  {'Tax Paid':<28} {tax_amount:>14,.2f} {CURRENCY}  ║")
print(f"║  {'Over-budget Categories':<28} {over_budget_count:>14}       ║")
print(f"║  {'Financial Health Score':<28} {score:>14}/10       ║")
print(f"{'╚' + '═' * (WIDTH - 2) + '╝'}")
print(f"\n  Computed using ONLY Module 01 Python concepts.")
print(f"  No functions, no if/else, no loops, no imports.\n")

# ============================================================
# END OF PROJECT 02
# ============================================================