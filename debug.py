import traceback


def boxPrint(symbol, height, width):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + ' ' * (width - 2) + symbol)
    print(symbol * width)


try: 
    boxPrint('*', 1, 50)
except:
    errorFile = open('error_log.txt', 'at')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The program failed. See error_log.txt for more information.')


#boxPrint('*', 1, 50)
