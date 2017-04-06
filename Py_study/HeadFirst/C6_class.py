#coding=utf-8


class Athlete:
    def __init__(self,a_name,a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    @staticmethod
    def sanitize(time_string):
        time_string = time_string.replace('-', '.').replace(':', '.')
        mins, secs = time_string.split('.')
        return (mins+'.'+secs)

    def top3(self):
        return sorted(set([self.sanitize(i) for i in self.times]))[0:3]

    def add_time(self,timeval):
        self.times.append(timeval)

    def add_times(self,timevalList):
        self.times.extend(timevalList)

def get_coatch_data(fname):
    try:
        with open(fname) as fp:
            data = fp.readline()
        tmp = data.strip().split(',')
        return Athlete(tmp.pop(0),tmp.pop(0),tmp)
    except IOError as err:
        print(err)

james = get_coatch_data('james.txt')
# james.add_time("2.00")
# james.add_times(["2.01","2.11","1-99"])
print(james.name,str(james.top3()))

vera = Athlete("vtest")
vera.add_time("2.00")
#x1 = a("Sarah james","2008-09-18",["2-34","3:21","2.34","2.45","3.01","2:01","2:01","3:10","2-22"])

print(vera.name,str(vera.top3()))
vera.add_times(["1.99","2.03","1.98"])
print(vera.name,str(vera.top3()))
