from configparser import ConfigParser

def config(filename='etc/database.ini', section='postgresql'):
    parser = ConfigParser()            # create a parser
    parser.read(filename)              # read config file

    db = {}                            # get section, default to postgresql
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

