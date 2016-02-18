# Code by Guy Shapira
import glob

NUM_STRING = '1234567890'

def file_fixer(dir_path):
        """
        This script gets a dir location of the file to fix, fix them
        and also create a file that merge all the files
        """
        files = glob.glob(r'%s\*.txt' %dir_path)
        for f in files:
                data = open(f, 'rb').read().splitlines()
                fixed_file = '\r\n'.join([line for line in data if not (line == '' or '-->' in line or (line[0] in NUM_STRING and line[-1] in NUM_STRING))])
                open(f, 'wb').write(fixed_file)
        merged_file_data = '\r\n\r\n'.join([open(f, 'rb').read() for f in files])
        open(r'%s\merged_file.txt' %dir_path, 'wb').write(merged_file_data)
				
