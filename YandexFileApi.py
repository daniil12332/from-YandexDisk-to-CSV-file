import yadisk
import csv
import config


y = yadisk.YaDisk(token=config.TOKEN)

data = [("Link", "Name", "Created", "Size")]

def scan_disk(addr, data):
    for item in y.listdir(addr):
        print(f"Название: {item['name']}")
        print(f'Размер: {item["size"]} байт')
        print(f"Тип файла: {item['type']}")
        print(f"Тип документа: {item['media_type']}")
        print(f"Дата создания: {item['created']}\n")
        new_addr = addr
        if item['type'] == "dir":
            if addr[-1] == "/":
                new_addr = addr+item['name']
            else:
                new_addr = addr+"/"+item['name']
            print(new_addr)
            print()
            scan_disk(new_addr, data)
        data.append((new_addr, item['name'], item['created'], item["size"]))

scan_disk(config.LINK, data)

with open('yadisk.csv', 'w', newline='') as f:
    csv.writer(f).writerows(data)