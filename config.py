# Safe version: no hardcoded secret is stored in the source code.
# The value should come from an environment variable or GitHub Secret.
import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")

# LAB-DEMO-314159
# KHAN-10001
# KHAN-24680
# KHAN-99999
# KHAM-12345
# KHAN-1234
# KHAN-123456
