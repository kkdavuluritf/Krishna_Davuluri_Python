press_release = '  Doddy calls a nationwide leader in dog poop REMOval services,'
press_release = press_release + 'is increasing its footprint in the pooper service industry of dog poop removal, with the opening of office in IGH, MN.'
press_release = press_release + 'Dodd calls currenytly cleans up Dog Poop in 87 teritories and 25 states ' \
                                'has been named as number-one dog poop removal.\Its listd top 500 entrepreneur list '

temp_text = press_release
print('No change\n', temp_text)
temp_text = press_release.strip().lower()
print('Strip and lower\n', temp_text)
temp_text = press_release.strip().casefold()
print('Strip and Capt\n', temp_text)
temp_text = press_release.replace('dog poop', 'Waste')
print('Replce poop\n', temp_text)
temp_text = press_release.replace('Its', 'I')
print('Replce Its\n', temp_text)
