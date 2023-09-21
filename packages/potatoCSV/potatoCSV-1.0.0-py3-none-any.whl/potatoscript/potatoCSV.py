import csv
class Config:
    def __init__(self, input_file):
        self.input_file=input_file

    def readCSV(self):
        # Read the input CSV file
        with open(self.input_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            return list(reader)

    def appendValues(self,lines,start,end):
        # Extract values and split by semicolons if present
        values = []
        for line in lines[start:end]:
            item, value = line
            item = item.strip()
            
            # Split value by semicolons
            for v in value.split(';'):
                v = v.strip()
                
                # Split value by hyphen if it exists
                if '-' in v:
                    a = v.split('-')
                    original_value, lotno, wno  = v, a[0], a[1]
                else:
                    original_value, lotno, wno = v, '', ''
                
                values.append((original_value, lotno, wno))
        return values

    def writeOutput(output_file,values):
        # Create a new CSV file and write the extracted values
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Write the extracted values
            for original_value, lotno, wno in values:
                writer.writerow([original_value, lotno, wno])
