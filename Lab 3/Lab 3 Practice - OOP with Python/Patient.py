from math import pow

LB_TO_KG = 0.453592
IN_TO_M = 0.0254

class Patient:
    """ A simple model of a Patient"""

    def __init__(self, name, weight_lbs, height_in, hospital= None):
        self.name = name
        self.weight_lbs = weight_lbs
        self.weight_kg = weight_lbs * LB_TO_KG
        self.height_in = height_in
        self.height_m = height_in * IN_TO_M
        self.hospital = hospital
        

    def calculate_bmi(self):
        return self.weight_kg / pow(self.height_m, 2)


class OutPatient(Patient):
    """ Extends Patient model to manage out patient information"""

    def __init__(self, name, weight, height, dept_name, doctor_name, appt_date, appt_time, isinsured, coverage_percent, hospital_fee):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an out patient.
        """

        super().__init__(name, weight, height)
        self.dept_name = dept_name
        self.doctor_name = doctor_name
        self.appt_date = appt_date
        self.appt_time = appt_time
        self.isinsured = isinsured
        self.coverage_percent = coverage_percent
        self.hospital_fee = hospital_fee
        self.calculate_payment()

    def calculate_payment(self):
        self.payment = self.hospital_fee
        if self.isinsured:
            self.payment = self.payment - (self.payment * self.coverage_percent)

        if self.dept_name == 'Dentistry':
            self.payment = self.payment - (self.payment * (self.coverage_percent/2))

        if self.dept_name == 'Optometry':
            self.payment = self.payment - (self.payment * (self.coverage_percent/3))

    def __str__(self):
        return f"{self.name}'s payment for an appointment with {self.doctor_name} on {self.appt_date} at {self.appt_time} is ${self.payment:.2f}."
