


if __name__ == '__main__':
    with open('requirements.txt', 'r') as f:
        contents = [i.replace('\n', '') for i in f.readlines()]
    print(contents)