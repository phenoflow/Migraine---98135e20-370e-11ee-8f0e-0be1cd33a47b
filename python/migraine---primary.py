# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"1474.00","system":"readv2"},{"code":"1474000.0","system":"readv2"},{"code":"8B6N.00","system":"readv2"},{"code":"F26..00","system":"readv2"},{"code":"F260.00","system":"readv2"},{"code":"F260.11","system":"readv2"},{"code":"F261.11","system":"readv2"},{"code":"F261000","system":"readv2"},{"code":"F262200","system":"readv2"},{"code":"F262300","system":"readv2"},{"code":"F262400","system":"readv2"},{"code":"F262800","system":"readv2"},{"code":"F26y000","system":"readv2"},{"code":"F26y300","system":"readv2"},{"code":"F26z.00","system":"readv2"},{"code":"K584.11","system":"readv2"},{"code":"103502.0","system":"med"},{"code":"103602.0","system":"med"},{"code":"103973.0","system":"med"},{"code":"10583.0","system":"med"},{"code":"11138.0","system":"med"},{"code":"12511.0","system":"med"},{"code":"14700.0","system":"med"},{"code":"161.0","system":"med"},{"code":"22685.0","system":"med"},{"code":"23621.0","system":"med"},{"code":"2424.0","system":"med"},{"code":"27930.0","system":"med"},{"code":"28031.0","system":"med"},{"code":"28092.0","system":"med"},{"code":"2861.0","system":"med"},{"code":"3220.0","system":"med"},{"code":"3658.0","system":"med"},{"code":"41497.0","system":"med"},{"code":"53813.0","system":"med"},{"code":"5509.0","system":"med"},{"code":"65262.0","system":"med"},{"code":"9004.0","system":"med"},{"code":"9633.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('migraine-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["migraine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["migraine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["migraine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
