import hashlib, hmac, os, base64

ITERATIONS = 180_000

def hash_password(password):
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, ITERATIONS)
    return base64.b64encode(salt).decode() + "$" + base64.b64encode(digest).decode()

def verify_password(password, stored):
    try:
        salt_b64, digest_b64 = stored.split("$", 1)
        salt = base64.b64decode(salt_b64)
        expected = base64.b64decode(digest_b64)
        actual = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, ITERATIONS)
        return hmac.compare_digest(actual, expected)
    except Exception:
        return False

def make_token(user_id):
    secret = os.getenv("FITBUDDY_SESSION_SECRET", "change-this-local-secret")
    payload = str(user_id)
    sig = hmac.new(secret.encode(), payload.encode(), "sha256").hexdigest()
    return base64.urlsafe_b64encode((payload + "." + sig).encode()).decode()

def read_token(token):
    try:
        secret = os.getenv("FITBUDDY_SESSION_SECRET", "change-this-local-secret")
        raw = base64.urlsafe_b64decode(token.encode()).decode()
        user_id, sig = raw.split(".", 1)
        expected = hmac.new(secret.encode(), user_id.encode(), "sha256").hexdigest()
        return int(user_id) if hmac.compare_digest(sig, expected) else None
    except Exception:
        return None
