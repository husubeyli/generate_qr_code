import qrcode

img = qrcode.make(
    'https://github.com/husubeyli'
)

img.save('husubayli_gitub.png')
