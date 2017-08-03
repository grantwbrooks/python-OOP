class Hospital(object):
    def __init__(self, hosp_name, capacity):
        self.patients = []
        self.hosp_name = hosp_name
        self.capacity = capacity
    def admit(self,addedpatient,bed_numberx):
        self.patients.append(addedpatient)
        if len(self.patients) >= self.capacity:
            print "Admissin NOT complete"
        else:
            addedpatient.bed_number = bed_numberx
            print "Admission COMPLETE"
            print addedpatient.bed_number
            print self.patients
        return self
    
    def remove_patient(self,q):
        for x in self.patients:
            if x.name == q:
                x.bed_number = None
                self.patients.remove(x)
        return self



class Patient(object):
    def __init__(self,patient_id,name,allergies,bed_number=None):
        self.patient_id = patient_id
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number
        # print self.bed_number


hospital1 = Hospital("TGH",3)
print hospital1

patient1 = Patient(1,"Toro","food")
patient2 = Patient(2,"Juan","meds")
patient3 = Patient(3,"Grant","apples")
print patient1

hospital1.admit(patient1,23).admit(patient2,33).admit(patient3,99).remove_patient("Toro")
print hospital1.patients
print patient1.bed_number

