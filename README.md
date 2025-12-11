# SecurePixelShuffle
A lightweight Python tool that encrypts and decrypts images by shuffling their pixels using NumPy.  
The shuffle order is generated from **two passwords**, and the image can only be restored when **both passwords are correct**.

This project uses:
- NumPy for pixel manipulation  
- SHA-256 to combine passwords into a deterministic random seed  
- Pillow (PIL) for image loading and saving  

---

## 🚀 Features
- 🔐 Two-password protection  
- 🔁 Fully reversible pixel shuffling  
- 🎲 Deterministic randomness using SHA-256  
- 🖼 Works with PNG, JPG, and any Pillow-supported format  
- 🧩 Produces scrambled images that cannot be visually understood  
- 💡 Simple, clean Python code (great for learning!)

---


