def compare():
    card_filename = 'cardnames.csv'
    scraped_filename = 'souptextdump.csv'

    with open(card_filename, 'r') as f:
        hosts = f.readlines()

    with open(scraped_filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()

        for line in lines:
            for host in hosts:
                if host in line:
                    print(line)