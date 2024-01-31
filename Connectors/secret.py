import secrets
token = secrets.token_hex(32)  # Generates a 64-character hexadecimal token
print(token)