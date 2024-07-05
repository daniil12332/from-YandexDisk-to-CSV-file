import yadisk
import csv
import config


y = yadisk.YaDisk(token=config.TOKEN)

with open(config.FILENAME+".csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows([["Link", "Name", "Created", "Size(KB)"]])

def scan_disk(addr):
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
            scan_disk(new_addr)
        if item["size"] == None:
            with open(config.FILENAME+".csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerows([[new_addr, item['name'], item['created'], " "]])
        else:
            with open(config.FILENAME+".csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerows([[new_addr, item['name'], item['created'], int(item["size"])/1000]])

scan_disk(config.LINK)
