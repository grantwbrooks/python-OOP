class Call(object):
    def __init__(self,call_id,caller_name,phone,call_time,call_reason):
        self.call_id = call_id
        self.caller_name = caller_name
        self.phone = phone
        self.call_time = call_time
        self.call_reason = call_reason
    def display(self):
        print "unique id:", self.call_id
        print "caller name:", self.caller_name
        print "phone number:", self.phone
        print "call time:", self.call_time
        print "reason for call:", self.call_reason
        print ""
        return self


class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.quesize = 0
    
    def add_call(self,addedcall):
        self.calls.append(addedcall)
        print self.calls
        return self
    def remove_call(self):
        self.calls.pop(0)
        print self.calls
        return self
    def info(self):
        print "Length of Que:", len(self.calls)
        print ""
        for x in self.calls:
            print "Caller name:", x.caller_name
            print "Phone number", x.phone
            print ""
        return self
#Ninja Level Answer:
    def findandremove(self,q):
        for x in self.calls:
            if x.phone == q:
                self.calls.remove(x)
        print self.calls
#Hacker Lever: didn't figure this out



    

call1 = Call(1,"grant","283-122-2939","12:34pm","arm pain")
call1.display()

call2 = Call(2,"james","432-122-2939","12:04pm","leg pain")
call3 = Call(3,"toro","284523-122-2939","12:14pm","neck pain")

callcenter1 = CallCenter()
callcenter1.add_call(call1).add_call(call2).add_call(call3).remove_call().info()

callcenter1.findandremove("284523-122-2939")
