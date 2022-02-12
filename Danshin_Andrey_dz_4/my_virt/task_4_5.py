import sys
import utils


value_list = sys.argv[1:]
value_str = ''.join(value_list)
print(utils.currency_rates(value_str))

'''
result = sum(map(int, sys.argv[1:4]))
print(sys.argv[:1])
print(f'результат: {result}')

#развернутый вид
def main(argv):
    program, *args = argv
    result = sum(map(int, args))
    print(f'Результат: {result}')

    return 0

if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
'''