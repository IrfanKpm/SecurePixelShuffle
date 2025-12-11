import numpy as np
from PIL import Image
import hashlib

def make_seed(password1, password2):
    combo = (password1 + password2).encode()
    h = hashlib.sha256(combo).hexdigest()
    return int(h, 16) % (2**32)


def encrypt_image(path, password1, password2, out_path):
    img = Image.open(path)
    arr = np.array(img)
    shape = arr.shape
    flat = arr.reshape(-1, 3)
    N = flat.shape[0]
    seed = make_seed(password1, password2)
    rng = np.random.RandomState(seed)
    perm = rng.permutation(N)
    scrambled = flat[perm]
    scrambled_img = scrambled.reshape(shape)
    Image.fromarray(scrambled_img).save(out_path)
    return N


def decrypt_image(path, password1, password2, out_path):
    img = Image.open(path)
    arr = np.array(img)
    shape = arr.shape
    flat = arr.reshape(-1, 3)
    N = flat.shape[0]
    seed = make_seed(password1, password2)
    rng = np.random.RandomState(seed)
    perm = rng.permutation(N)
    inverse_perm = np.argsort(perm)
    restored = flat[inverse_perm]
    restored_img = restored.reshape(shape)
    Image.fromarray(restored_img).save(out_path)


# Encrypt (lock)
encrypt_image("input.png", "passA", "passB", "locked.png")

# Decrypt (unlock)
decrypt_image("locked.png", "passA", "passB", "restored.png")
