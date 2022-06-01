class Article:
    def __init__(self, id, body):
        self.id = id
        self.body = body


def parse_file():
    f = open('./News.txt', 'r')
    lines = f.readlines()

    for line in lines:
        id = -1
        body = ""
        if line[0:4] == '<ID>':
            id = line[4:-6]

        Article(id, "")


if __name__ == "__main__":
    # run code
    parse_file()
