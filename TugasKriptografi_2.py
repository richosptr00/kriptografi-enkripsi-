def caesar_cipher(text, shift):
  """
  Program Caesar Cipher sederhana untuk enkripsi.

  Args:
    text: Teks yang akan dienkripsi.
    shift: Jumlah pergeseran huruf.

  Returns:
    Teks yang telah dienkripsi.
  """
  result = ''
  for char in text:
    if char.isalpha():  # Periksa apakah karakter adalah huruf
      start = ord('a') if char.islower() else ord('A')  # Tentukan awal alfabet (huruf kecil atau besar)
      shifted_char = chr((ord(char) - start + shift) % 26 + start)  # Geser karakter ke kanan (enkripsi)
    else:
      shifted_char = char  # Karakter selain huruf tetap sama
    result += shifted_char  # Tambahkan karakter yang telah digeser ke hasil
  return result

# Teks yang akan dienkripsi
text = "KRIPTOGRAFI"
# Jumlah pergeseran
shift = 5

# Enkripsi
encrypted_text = caesar_cipher(text, shift)
print("Teks terenkripsi:", encrypted_text)