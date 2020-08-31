import csv, string

printable = set(string.printable)

sanitized_data = {}
key = 0

first_col = ''
prev_first_col = ''

with open('new_combi_sheet.csv', encoding='latin-1') as infile:   
    csv_raw = csv.reader(infile)

    for row_list in csv_raw:

        # remove non printable chars and leading and trailing whitespace
        for i in range(len(row_list)):
            row_list[i]=''.join(filter(lambda x: x in printable, row_list[i]))
            row_list[i] = row_list[i].strip()

        # process each row
        first_col = row_list[0]
        if (first_col):
            if not prev_first_col:
                key += 1

            # build sanitized_data
            if key not in sanitized_data:
                sanitized_data[key] = row_list
            else:
                for i in range(len(row_list)):
                    if row_list[i]:       
                        if sanitized_data[key][i]:
                            sanitized_data[key][i] = sanitized_data[key][i] + "~" + row_list[i]
                        else:
                            sanitized_data[key][i] = row_list[i]

        prev_first_col = first_col

# write out the sanitized data
with open('new_out.csv', mode='w') as outfile:
    csv_sanitized = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for key, val in sanitized_data.items():
        print(key, val)
        csv_sanitized.writerow(val)