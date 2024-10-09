def caesar_cipher(text, shift, mode):
  """
  Program Caesar Cipher sederhana untuk enkripsi dan dekripsi.

  Args:
    text: Teks yang akan dienkripsi atau didekripsi.
    shift: Jumlah pergeseran huruf.
    mode: 'encrypt' untuk enkripsi, 'decrypt' untuk dekripsi.

  Returns:
    Teks yang telah dienkripsi atau didekripsi.
  """
  result = ''
  for char in text:
    if char.isalpha():  # Periksa apakah karakter adalah huruf
      start = ord('a') if char.islower() else ord('A')  # Tentukan awal alfabet (huruf kecil atau besar)
      if mode == 'encrypt':
        shifted_char = chr((ord(char) - start + shift) % 26 + start)  # Geser karakter ke kanan (enkripsi)
      elif mode == 'decrypt':
        shifted_char = chr((ord(char) - start - shift) % 26 + start)  # Geser karakter ke kiri (dekripsi)
    elif char.isdigit():  # Periksa apakah karakter adalah angka
      if mode == 'encrypt':
        shifted_char = str((int(char) + shift) % 10)  # Geser angka ke kanan (enkripsi)
      elif mode == 'decrypt':
        shifted_char = str((int(char) - shift) % 10)  # Geser angka ke kiri (dekripsi)
    else:
      shifted_char = char  # Karakter selain huruf dan angka tetap sama
    result += shifted_char  # Tambahkan karakter yang telah digeser ke hasil
  return result


# Contoh penggunaan
text = "Richo123"
shift = 3

# Enkripsi
encrypted_text = caesar_cipher(text, shift, 'encrypt')
print("Teks terenkripsi:", encrypted_text)  # Output: Ulfkr456
decrypted_text = caesar_cipher(encrypted_text, shift, 'decrypt')
print("Teks terdekripsi:", decrypted_text)  # Output: Richo123