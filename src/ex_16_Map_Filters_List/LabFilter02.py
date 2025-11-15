# -------------------------------------------------------------
# Step 1: Test Results List
# -------------------------------------------------------------
# A list containing different test statuses.

test_results = ["PASS", "FAIL", "PASS", "SKIP", "FAIL"]


# -------------------------------------------------------------
# Step 2: Filter only "PASS" values using lambda
# -------------------------------------------------------------
# filter() + lambda will keep only those values which match "PASS".
# (Hindi: Sirf "PASS" wale hi filter hoke nikaal jayenge.)

pass_results = list(filter(lambda x: x == "PASS", test_results))


# -------------------------------------------------------------
# Step 3: Print Filtered Output
# -------------------------------------------------------------
# Expected Output: ['PASS', 'PASS']

print(pass_results)
