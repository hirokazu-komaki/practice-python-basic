class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def show_personal_info(self):
        print("名前：{}".format(self.name))
        print("年齢：{}".format(self.age))
        print("性別：{}".format(self.gender))


class Patient(Human):
    def __init__(self, name, age, gender, symptoms, patient_id, desired_date):
        super().__init__(name=name, age=age, gender=gender)
        self.symptoms = symptoms
        self.patient_id = patient_id
        self.desired_date = desired_date

    def show_personal_info(self):
        super().show_personal_info()
        print("あなたのID：{}".format(self.patient_id))
        print("症状：{}".format(self.symptoms))
        print("予約希望日時：{}".format(self.desired_date))

class Clinic:
    def __init__(self, clinic_name, *args):
        self.clinic_name = clinic_name
        self.patients_list = []
        for patient in args:
            self.patients_list.append(patient)

    def show_waiting_count(self ):
        pass

    def reserve(self):
        pass

    def diagnosis(self):
        pass

    @staticmethod
    def _check_reserved():
        pass



if __name__ == "__main__":
    # hiro = Patient("Hiro", 26, "man", "風を引いている、熱は38度", 1010, "2023-01-11")
    # hiro.show_personal_info()
    kodaira_clinic = Clinic("Kodaira Clinic", "Mike", "Risa", "Hiro")
    print(kodaira_clinic.patients_list)

