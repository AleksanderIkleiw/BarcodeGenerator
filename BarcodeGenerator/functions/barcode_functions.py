import PIL, barcode, os, sys, win32clipboard
from functions import settings_functions
from io import BytesIO
from PIL.Image import Image
from barcode.writer import ImageWriter


def generate_barcode(num):
    dir = os.getcwd().split('user_interface')[0]

    data = settings_functions.read_settings()

    writer = ImageWriter()

    if data['checksum'] == 'T':
        ean = barcode.codex.Code39(num, writer, add_checksum=True)
    else:
        ean = barcode.codex.Code39(num, writer, add_checksum=False)
    d = {}
    for i, j in data.items():
        if i != 'checksum':
            if '.' in j:
                d[i] = float(j)
            else:
                d[i] = int(j)

    ean.save(f'{dir}images\\temp\\barcode', d)

    image = PIL.Image.open(f'{dir}\\images\\temp\\barcode.png')

    output = BytesIO()

    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]

    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

