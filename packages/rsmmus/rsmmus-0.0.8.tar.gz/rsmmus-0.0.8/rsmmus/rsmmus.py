import pandas as pd
import numpy as np
import xlsxwriter

class SampleGenerator:
    def __init__(self):

        self.sampling = None
        
        self.yesno = ("Y","y","N","n")
        self.ar = ("APNP", "Low", "Moderate", "High")

        ### Significant Risk
        while True:
            self.risk = str(input("Significant Risk? (Y/N): "))
            if self.risk not in self.yesno:
                print("Y 또는 N으로 입력해야 합니다.")
            else:
                self.risk = "Yes" if self.risk == "Y" or self.risk == "y" else "No"
                print(f"Significant Risk는 {self.risk} 으로 입력되었습니다.")
                break
            
            
        ### Reliance on Controls
        while True:
            self.roc = str(input("Reliance on Controls? (Y/N): "))
            if self.roc not in self.yesno:
                print("Y 또는 N으로 입력해야 합니다.")
            else:
                self.roc = "Yes" if self.roc == "Y" or self.roc == "y" else "No"
                print(f"Reliance on Controls는 {self.roc} 으로 입력되었습니다.")
                break
            
            
        ### Tolerable Misstatement
        while True:
            try:
                self.tm = int(input("Tolerable Misstatement? (숫자로 입력): "))
                print(f"Tolerable Misstatement는 {self.tm}입니다.")
                break
            except ValueError:
                print("입력값이 숫자가 아닙니다.")


        ### Expected Misstatement Rate
        self.emr = 0.05
        print(f"Expected Misstatement Rate는 {self.emr}입니다.")


        ### Substantive Analytical Procedures
        while True:
            try:
                self.sap_index = int(input("Substantive Analytical Procedures? [(1)APNP, (2)Low, (3)Moderate, (4)High] => 1,2,3,4 중 하나의 숫자로 입력 : "))
                if self.sap_index < 1 or self.sap_index > 4:
                    print("1,2,3,4 중 하나의 숫자로 입력해야 합니다.")
                else:
                    self.sap = self.ar[self.sap_index-1]
                    print(f"Substantive Analytical Procedures는 {self.sap} 으로 입력되었습니다.")
                    break
            except ValueError:
                print("입력값이 숫자가 아닙니다.")

        assurance_factor_raw = pd.DataFrame({"SignificantRisk" : ["Yes", "No", "Yes", "No"],
                                        "RelianceonControls" : ["No","No","Yes","Yes"],
                                        "High" : [1.1, 0 ,0 ,0],
                                        "Moderate" : [1.6,0.5,0.2,0],
                                        "Low" : [2.8,1.7,1.4,0.3],
                                        "APNP" : [3,1.9,1.6,0.5]})
        assurance_factor = pd.melt(assurance_factor_raw, id_vars = ["SignificantRisk", "RelianceonControls"],
                                var_name = "Planned_Level",
                                value_name = "Assurance_Factor")
        factor_filter = assurance_factor[assurance_factor['SignificantRisk'] == self.risk]
        factor_filter = factor_filter[factor_filter['RelianceonControls'] == self.roc]
        factor_filter = factor_filter[factor_filter['Planned_Level'] == self.sap]
        self.AF = factor_filter["Assurance_Factor"].values[0]


        print()
        print(f"Assurance Factor는 {self.AF} 입니다.")
        print()
        print("=============================================")
        print("Parameters")
        print("=============================================")
        print(f"Significant Risk : {self.risk}")
        print(f"Reliance on Controls? : {self.roc }")
        print(f"Tolerable Misstatement : {self.tm}")
        print(f"Expected Misstatement Rate : {self.emr*100}% ")
        print(f"Substantive Analytical Procedures : {self.sap}")
        print("=============================================")


    def save_file(self, pop, sampling_result, amount, file_path):
        try:
            Test = [' ',
                    'Test of Details - [BP70 Section A-B]',
                    ' ',
                    '회사명',
                    '작성일자',
                    '작성자',
                    '검토자',
                    ' ',
                    ' ',
                    'Section A: 목적 ',
                    ' ',
                    '표본감사를 사용할 때 감사인의 목적은 추출된 표본이 모집단에 대해 결론을 도출하는 데 합리적인 근거를 제공하는 것이다. ',
                    '표본감사란 계정잔액이나 특정 거래의 입증을 목적으로, 전체 항목보다 적은 수의 항목에 대해서 감사절차를 적용하는 것이다.',
                    '표본항목들은 표본이 모집단을 대표하는 방식으로 추출되어야 한다. 그러므로 모집단의 모든 항목들은 추출될 기회를 가져야 한다. ',
                    '감사인은 감사표본을 설계할 때 감사절차의 목적과 표본을 도출할 모집단의 특성을 고려하여야 한다. ',
                    '감사인은 감사표본을 설계할 때 달성할 특정 목적과 그러한 목적을 가장 잘 달성할 수 있는 감사절차의 조합을 고려해야 한다. ',
                    '감사인은 추출한 모집단의 표본이 감사 목적에 적절한 것인지 결정해야 한다.',
                    ' ',
                    ' ',
                    '(1) 계정명(FSLI)  :               ',
                    '(2) 기준일 (Coverage date)  :                ',
                    '(3) 테스트되는 경영자의 주장 (Assertion)  :    정확성 (A), 실재성 및 발생사실(E/O)',
                    ' ',
                    ' ',
                    'Section B: 표본 설계 - 모집단과 표본',
                    ' ',
                    '(1) 모집단의 성격 : ',
                    '(2) 모집단의 완전성 확인 방법 : ',
                    '(3) 표본단위의 정의  : ',
                    '(4) 전체 모집단이 추출 대상인가?  : ',
                    ' ',
                    ' ',
                    '* 표본 지표',
                    '---------------------------------------------------------------------------------------------------------------------------- ',
                    '모집단 크기 : ' + str(sum(pop[amount])),
                    '예상오류 : ' + str(float(self.tm) * float(self.tm)),
                    'Tolerable Misstatement : ' + str(float(self.tm)),
                    '표본대상 항목들의 위험평가 결과 SignificantRisk? : ' + str(self.risk),
                    '통제에 의존하는 경우 : ' + str(self.roc),
                    '실증적 분석적 검토 절차를 통해 기대수준의 확신을 얻었는가? : ' + str(self.sap),
                    '---------------------------------------------------------------------------------------------------------------------------- ',
                    ' ',
                    ' ',
                    ' ',
                    ' ',
                    ' ',
                    '---------------------------------------------------------------------------------------------------------------------------- ',
                    '[Assurance factor]                                Planned Level of Assurance from Substantive Analytical Procedures',
                    "SignificantRisk    RelianceonControls        High   Moderate   Low   APNP ",
                    "Yes                     No                             1.1         1.6          2.8         3",
                    "No                      No                             0          0.5          1.7         1,9",
                    "Yes                     Yes                             0          0.2          1.4         1.6",
                    "No                     Yes                             0          0            0.3         0.5",
                    '---------------------------------------------------------------------------------------------------------------------------- ',
                    ' ',
                    ' ',
                    '* 표본크기 결정',
                    '---------------------------------------------------------------------------------------------------------------------------- ',
                    '신뢰계수 (Assurance factor) : ' + str(self.AF),
                    '추출된 표본의 갯수 : '  + str(len(sampling_result)),
                    '---------------------------------------------------------------------------------------------------------------------------- ',
                    ' ',
                    ' ',
                    ' ']


            excel_file = file_path + '/test_summary.xlsx'
            workbook = xlsxwriter.Workbook(excel_file)
            worksheet = workbook.add_worksheet('ToD')

            for row_num, value in enumerate(Test):
                worksheet.write(row_num, 1, value)
            cell_format1 = workbook.add_format()
            cell_format1.set_bottom(5)
            for i in range(4, 8):
                worksheet.write(f'C{i}', " ", cell_format1)
            for i in [20, 21, 27, 28, 29, 30, 43, 63]:
                worksheet.write(f'C{i}', " ", cell_format1)
            worksheet.set_column(1, 3, 40)

            cell_format2 = workbook.add_format()
            cell_format2.set_bold()
            cell_format2.set_font_color('blue')
            worksheet.write('B43','추출 방법 (MUS or Random): ', cell_format2)
            worksheet.write('B63','Test에 대한 추가 기술 및 결론 : ', cell_format2)

            cell_format3 = workbook.add_format()
            cell_format3.set_bg_color('green')

            cell_format4 = workbook.add_format()
            cell_format4.set_bg_color('#0099FF')


            worksheet.write('B2', 'Test of Details - [BP70 Section A-B]', cell_format3)
            worksheet.write('C2',' ',cell_format3)
            worksheet.write('D2','표본추출절차서 ',cell_format3)

            worksheet.write('B10', 'Section A: 목적 ', cell_format4)
            worksheet.write('B25', 'Section B: 표본 설계 - 모집단과 표본 ', cell_format4)
            for i in ['C10','D10','C25', 'D25']:
                worksheet.write(i, " ", cell_format4)


            workbook.close()


            excel_writer = pd.ExcelWriter(file_path + '/test_sample.xlsx', engine='xlsxwriter')
            sampling_result.to_excel(excel_writer, sheet_name='test_sample',index=False)
            excel_writer.close()
            print("Save complete => test_sample.xlsx, test_summary.xlsx")

        except Exception as err:
            print("Error", err)

    def mus(self, pop, amount):
        try:
            if amount != 'amount':
                pop = pop.rename(columns = {amount : 'amount'}) 
            
            pop = pop.dropna(subset=['amount'], how='any', axis=0) 
            pop['amount'] = pd.to_numeric(pop['amount'])

            
            high = pop[pop['amount'] > int(self.tm) ]
            sum_High_value_items = sum(high['amount'])
            high_index = list(high.index)
            pop_remain = pop.drop(high_index)
            minus = pop[pop['amount'] <= 0]
            minus_index = list(minus.index)
            pop_remain = pop_remain.drop(minus_index)

            sampling_interval = np.int64((int(self.tm)  - int(self.tm) * float(self.emr)) / self.AF)
            print(f"Sampling Interval은 {sampling_interval} 입니다.")

            pop_amount = sum(np.int64(pop_remain['amount']))
            sample_size = int(np.int64(pop_amount * self.AF) / (int(self.tm)  - int(self.tm) * float(self.emr)))
            sampling_array = np.array(list(range(1, sample_size + 1)), dtype='int64')
            sampling_n = sampling_array * sampling_interval
            sampling_row = list(range(sample_size))
            pop_remain['cum'] = np.cumsum(pop_remain['amount'])
            for i in range(sample_size):
                sampling_row[i] = np.where(pop_remain['cum'] > sampling_n[i])[0][0]

            unique = set(sampling_row)
            sampling_row = list(unique)
            sampling_row.sort()

            ## 추출된 샘플의 갯수
            print("Sample Output Size : " + str(len(sampling_row) + len(high)))

            ## 샘플링 객체 생성
            pop_remain = pop_remain.drop('cum', axis = 1)
            pop_remain = pop_remain.reset_index()
            mus_sample = pop_remain.loc[sampling_row]
            self.sampling = pd.concat([high, mus_sample])
            self.sampling = self.sampling.rename(columns = {'amount': amount}) 

            return self.sampling

        except Exception as err:
            print("Error", err)
