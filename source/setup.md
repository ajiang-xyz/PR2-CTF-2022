# Generate HTML file
1. generate flag at https://www.ascii-art-generator.org; replace all # with 0
2. run generator.py to generate unique ciphertext banner
3. append to js array in html file

# Hide HTML file in image
1. stegano-lsb-set hide -i (input image file) -g eratosthenes -f (file to hide) -o (out image file)
       stegano-lsb-set hide -i space.jpg -g eratosthenes -f flag.html -o flag.png

# Mess up image header
1. use a tool like hexedit to corrupt the bytes however you want (u could even do smth like "deadbeefcafe")