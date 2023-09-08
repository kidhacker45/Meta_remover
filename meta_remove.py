print(" _  _ ___ ____  _   _    _    ____ _  _______ ____   ")
print("| |/ /_ _|  _ \| | | |  / \  / ___| |/ / ____|  _ \  ")
print("| ' / | || | | | |_| | / _ \| |   | ' /|  _| | |_) | ")
print("| . \ | || |_| |  _  |/ ___ \ |___| . \| |___|  _ <  ")
print("|_|\_\___|____/|_| |_/_/   \_\____|_|\_\_____|_| \_\ ")
                                                                   

from PIL import Image
image_path = str(input('[+] Enter Image path: '))
image = Image.open(image_path)
data = list(image.getdata())
image_without_metadata = Image.new(image.mode, image.size)
image_without_metadata.putdata(data)
print("Metadata removed :")
output_path = str(input('[+] Enter Image_remove path: '))
image_without_metadata.save(output_path)
print("file saved,(output_path) :")
