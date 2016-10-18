import csv, re, random

with open('gnaf_data.psv', newline='') as gnaf_file:
    gnaf_dialect = csv.Sniffer().sniff(gnaf_file.read(1024), delimiters="|")
    gnaf_file.seek(0)
    reader  = csv.DictReader(gnaf_file, dialect=gnaf_dialect)
    count = 0
    print('<AddressCollection>')

    for line in reader:
        count += 1
        address_text = line.pop("address")

        if line["lot_number"] == line["number_first"] or line["lot_number"] == line["number_last"]:
            continue
        for key, value in line.items():
            if key not in("locality_name", "state_code", "postcode"):
                if value:
                    address_text = re.sub(r"\b{}\b".format(value), '<{}>{}</{}>'.format(key,value,key), address_text, count=1)
        # print(address_text)
        if count % 2 == 0:
            print('<address_string>{}, <locality_name>{}</locality_name> <postcode>{}</postcode> <state_code>{}</state_code></address_string>'.format(output))
        else:
            print('<address_string>{}, <locality_name>{}</locality_name> <state_code>{}</state_code> <postcode>{}</postcode> </address_string>'.format(address_text, address_remainder))
    print('</AddressCollection>')
