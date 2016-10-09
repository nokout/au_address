import csv, re

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
            print('<address_string>{}, <locality_name>{}</locality_name> <postcode>{}</postcode> <state_code>{}</state_code></address_string>'.format(address_text, line["locality_name"], line["postcode"], line["state_code"] ))
        else:
            print('<address_string>{}, <locality_name>{}</locality_name> <state_code>{}</state_code> <postcode>{}</postcode> </address_string>'.format(address_text, line["locality_name"], line["state_code"], line["postcode"] ))
    print('</AddressCollection>')
        # tagged_tokens = []
        # tokens = re.split('(\W)', line["address"])
        # for token in tokens:
        #         matched_key = None
        #         if value == token:
        #             matched_key = key
        #             break
        #     if matched_key:
        #         tagged_tokens.append("<{}>{}</{}>".format(key, value, key))
        #     else:
        #         tagged_tokens.append(token)
        #         if len(token) > 1:
        #             print('Miss: {}'.format(token))

                #     # for token in tokens:
                #     for
            # tokenise address
                #for each token
                    #if not delimiter
                        #match with value
                            #wrap in key based xml
            # for key, value in line.items():
