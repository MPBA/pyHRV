vh = open('version', 'r')
lines = vh.readlines()
version = lines[-1].rstrip('\n').rstrip('\r').split('.')
vh.close()
vh = open('version', 'a')
version[-1] = (int(version[-1]) + 1).__str__()
vh.writelines("\n" + ".".join(version))
vh.close()
