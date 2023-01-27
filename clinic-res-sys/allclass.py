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
    def __init__(self, **kwargs):
        super().__init__(
            name=kwargs.get('name', None), 
            age=kwargs.get('age', None),
            gender=kwargs.get('gender', None)
            )
        self.patient_id = kwargs.get('patient_id', None)
        self.desired_date = kwargs.get('desired_date', None)
        self.symptoms = kwargs.get('symptoms', None)

    def show_personal_info(self):
        super().show_personal_info()
        print("あなたのID：{}".format(self.patient_id))


class Clinic:
    def __init__(self, clinic_name, *args):
        self.clinic_name = clinic_name
        self.patients_list = []
        for patient in args:
            self.patients_list.append(patient)

    def show_waiting_count(self):
        pass

    def reserve(self):
        # 予約はIDで管理
        # 予約済みかどうかを判断
        tmp_id = int(input("あなたの診察IDは?:"))
        if self._check_reserved(tmp_id):
            print("すでに予約は取れています")
            # for patient in self.patients_list:
            #     if patient.patient_id == tmp_id:
            #         print("あなたの予約情報は以下です\
            #               {}".format(patient))
            #         break
        else:
            print("まだ予約はされてません、以下に従って予約してください")
            # 希望日時を入力
            for patient in self.patients_list:
                if patient.patient_id == tmp_id:
                    patient.desired_date = input("予約希望日時を入力してください(例 01/20/13:00)\n:")
                    #症状を入力
                    patient.symptoms = input("症状を教えてください(例 熱38度/咳がよく出ます)\n:")

                    print("予約できました")
                    # print("あなたの予約情報は以下です\
                    #       \n{}".format(patient))
                    break
                     
    def diagnosis(self):
        pass

    def _check_reserved(self, tmp_id):
        for patient in self.patients_list:
            if patient.patient_id == tmp_id:    
                # すでに予約情報や症状が入ってるかどうか
                if patient.desired_date:
                    return True
                else:
                    return False
            else:
                continue
        # 以下のreturnの意味=そもそも診察IDがない=クリニックに登録されていない
        # 新規者だからpatientの新規登録と予約をここで行いたいけど今回は飛ばす
        return "あなたは{}に登録されていません".format(self.clinic_name)




if __name__ == "__main__":
    # インスタンス変数の数は統一していおいて、値が与えら得てないものはNone
    hiro = Patient(name="Hiro", age=26, gender="man", patient_id=1010, desired_date="01/23/13:00", symptoms=None)
    mika = Patient(name="Mika", age=28, gender="woman", patient_id=1011)
    yuki = Patient(name="Yuki", age=23, gender="man", patient_id=1012)

    kodaira_clinic = Clinic("Kodaira Clinic", hiro, mika, yuki)
    print(kodaira_clinic.patients_list)
    kodaira_clinic.reserve()