from django.db import models
from bitrix_base_app.models import BaseModel, ReferenceItem
 
 
# class Country(BaseModel):
#     country_name  = models.CharField(max_length=100,null=True,blank=True)
#     country_code  = models.CharField(max_length=10, null=True, blank=True)
    
#     class Meta:
#         db_table = "country"   

# class EmployeeInfo(BaseModel):
#     full_name          = models.CharField(max_length=50,null=True, blank=True)
#     family_name        = models.CharField(max_length=50,null=True, blank=True)
#     designation        = models.CharField(max_length=50, null=True, blank=True)
#     gender             = models.ForeignKey(ReferenceItem, on_delete=models.CASCADE, null=True, blank=True,related_name = "gender")
#     date_of_birth      = models.DateField( null=True, blank=True)
#     country            = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True,related_name = "country")
#     application_date   = models.DateField( max_length=30, null=True, blank=True)
#     phone_number       = models.CharField(max_length=50, null=True, blank=True)
#     location           = models.CharField(max_length=50, null=True, blank=True)
#     citizenship        = models.CharField(max_length=50, null=True, blank=True)
#     nationality        = models.CharField(max_length=50, null=True, blank=True)
#     address            = models.TextField(null=True, blank=True)
#     marital_status     = models.ForeignKey(ReferenceItem, on_delete=models.CASCADE, null=True, blank=True,related_name = "marital_status")
#     passport_no        = models.CharField(max_length=50, null=True, blank=True)
#     expiry_date        = models.DateField(null=True, blank=True)
#     occupation         = models.CharField(max_length=200, null=True, blank=True)
#     passport_issue_date  = models.DateField(null=True, blank=True)
#     passport_issue_place = models.CharField(max_length=100, null=True, blank=True)
#     passport_issue_authority = models.CharField(max_length=100, null=True, blank=True)
#     age                = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = "employee_info"
 
# class EntryPermitApplication(BaseModel):
#     employee           = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE, null=True, blank=True,related_name = "entry_permit_employee")
#     visit_purpose      = models.CharField(max_length=20, null=True, blank=True)
#     stay_duration      = models.IntegerField( null=True, blank=True)
#     stay_duration_type = models.CharField(max_length=20, null=True, blank=True)
#     flight_name        = models.CharField(max_length=50, null=True, blank=True)
#     departure_place    = models.CharField(max_length=50, null=True, blank=True)
#     departure_date     = models.DateField(null=True, blank=True)
#     arrival_place      = models.CharField(max_length=50, null=True, blank=True)
#     # arrival_place      = models.CharField(max_length=50, null=True, blank=True)
#     arrival_date       = models.DateField(null=True, blank=True)
#     employment_purpose = models.CharField(max_length=200, null=True, blank=True)
#     stay_fund          = models.CharField(max_length=200, null=True, blank=True)
#     # stay_fund          = models.CharField(max_length=10, null=True, blank=True)
#     previous_family_name = models.CharField(max_length=50, null=True, blank=True)
#     previous_given_name = models.CharField(max_length=50, null=True, blank=True)
#     previous_given_dob = models.DateField(null=True, blank=True)
#     previous_gender    = models.ForeignKey(ReferenceItem, on_delete=models.CASCADE, null=True, blank=True,related_name = "previous_gender")
#     previous_marital_status = models.ForeignKey(ReferenceItem, on_delete=models.CASCADE, null=True, blank=True,related_name = "previous_marital_status")
#     other_passport_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True,related_name = "other_passport_country")
#     # previous_marital_status = models.ForeignKey(ReferenceItem, on_delete=models.CASCADE, null=True, blank=True,related_name = "previous_marital_status")
#     other_passport_no        = models.CharField(max_length=50, null=True, blank=True)
#     other_passport_expiry_date = models.DateField(null=True, blank=True)
#     organization_name = models.CharField(max_length=100, null=True, blank=True)
#     agent = models.CharField(max_length=50, null=True, blank=True)
#     address = models.TextField(null=True, blank=True)
#     town = models.CharField(max_length=50,null=True, blank=True)
#     province = models.CharField(max_length=50,null=True, blank=True)
#     postcode = models.IntegerField(null=True, blank=True)
#     org_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True,related_name = "org_country")
#     business_telephone = models.CharField(max_length=20,null=True, blank=True)
#     fascsimile = models.CharField(max_length=30,null=True, blank=True)
#     visited_png_before = models.BooleanField(default=False)
#     last_visit_date = models.DateField(null=True, blank=True)
#     last_visit_purpose = models.CharField(max_length=200,null=True, blank=True)
#     last_visit_duration = models.CharField(max_length=30,null=True, blank=True)
#     last_visit_stay_address = models.TextField(null=True, blank=True)
#     criminal_offence_convicted = models.BooleanField(default=False)
#     criminal_offence_detail = models.TextField(null=True, blank=True)
#     criminal_offence_refused = models.BooleanField(default=False)
#     entry_refused_detail = models.TextField(null=True, blank=True)
#     mental_issue = models.BooleanField(default=False)
#     mental_issue_detail = models.TextField(null=True, blank=True)
#     res_addr_street = models.CharField(max_length=100,null=True, blank=True)
#     res_addr_town = models.CharField(max_length=100,null=True, blank=True)
#     res_addr_province = models.CharField(max_length=50,null=True, blank=True)
#     res_addr_postcode = models.CharField(max_length=100,null=True, blank=True)
#     res_addr_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True,related_name = "res_addr_country")
#     res_addr_home_tel = models.CharField(max_length=50,null=True, blank=True)
#     res_addr_mobile_tel = models.CharField(max_length=50,null=True, blank=True)
#     res_addr_email = models.CharField(max_length=200,null=True, blank=True)
#     res_addre_email_communication = models.BooleanField(default=False)
#     png_street = models.CharField(max_length=200,null=True, blank=True)
#     png_town = models.CharField(max_length=100,null=True, blank=True)
#     png_provice = models.CharField(max_length=75,null=True, blank=True)
#     png_postal_address = models.TextField(null=True, blank=True)
#     png_home_tel = models.CharField(max_length=50,null=True, blank=True)
#     png_mobile_tel = models.CharField(max_length=50,null=True, blank=True)
#     emergency_family_name = models.CharField(max_length=50,null=True, blank=True)
#     emergency_given_name = models.CharField(max_length=50,null=True, blank=True)
#     emergency_relationship = models.CharField(max_length=50,null=True, blank=True)
#     emergency_address = models.TextField(null=True, blank=True)
#     emergency_town = models.CharField(max_length=100,null=True, blank=True)
#     emergency_province = models.CharField(max_length=50,null=True, blank=True)
#     emergency_postcode = models.CharField(max_length=100,null=True, blank=True)
#     emergency_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True,related_name = "emergency_country")
#     emergency_home_tel = models.CharField(max_length=50,null=True, blank=True)
#     emergency_mobile_tel = models.CharField(max_length=50,null=True, blank=True)
#     emergency_date = models.DateField(null=True, blank=True)
#     class Meta:
#         db_table = "entry_permit_application"

# class SelfDeclarationCoronoVirus(BaseModel):
#     employee           = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE, null=True, blank=True,related_name = "self_declaration_employee")
#     arrival_date       = models.DateField(null=True, blank=True)
#     date               = models.DateField(null=True, blank=True)
#     corona_case_country_visit = models.BooleanField(default=False)
#     corona_case_country_visit_detail = models.TextField(default=False)
#     symptoms           = models.JSONField(null=True, blank=True)
#     symptoms_detail    = models.TextField(null=True, blank=True)
#     future_travel_to_corona_country = models.BooleanField(default=False)
#     class Meta:
#         db_table = "self_declaration_corona_virus"

# class MedicalExamination(BaseModel):
#     employee           = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE, null=True, blank=True,related_name = "medical_examination_employee")
#     family_illness_detail = models.TextField(null=True, blank=True)
#     family_illness_tb_detail = models.TextField(default=False)
#     family_mental_illness_detail = models.TextField(default=False)
#     required_medical_attention    = models.TextField(null=True, blank=True)
#     family_physical_disability_detail = models.TextField(null=True, blank=True)
#     class Meta:
#         db_table = "medical_examination"

# class WorkPermitApplication(BaseModel):
#     employee = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE, null=True, blank=True,related_name = "work_permit_employee")
#     application_checklist = models.TextField(null=True, blank=True)
#     general_work_permit= models.BooleanField(default=False)
#     volunteer_work_permit = models.BooleanField(default=False)
#     shortterm_work_permit = models.BooleanField(default=False)
#     longterm_work_permit = models.BooleanField(default=False)
#     workpermit_term = models.CharField(max_length=50,null=True, blank=True)
#     employer = models.CharField(max_length=100,null=True, blank=True)
#     employer_address =models.TextField(null=True, blank=True)
#     telephone = models.CharField(max_length=30,null=True, blank=True)
#     fax = models.CharField(max_length=50,null=True, blank=True)
#     email = models.TextField(null=True, blank=True)
#     industrial_division = models.CharField(max_length=100,null=True, blank=True)
#     industrial_subdivision = models.CharField(max_length=100,null=True, blank=True)
#     png_employees_employed = models.IntegerField(null=True, blank=True)
#     non_citizen_employed = models.IntegerField(null=True, blank=True)
#     job_title = models.CharField(max_length=200,null=True, blank=True)
#     occupation = models.CharField(max_length=200,null=True, blank=True)
#     job_code = models.CharField(max_length=200,null=True, blank=True)
#     company_position_code = models.CharField(max_length=200,null=True, blank=True)
#     primary_work_location = models.CharField(max_length=200,null=True, blank=True)
#     other_location_travel = models.BooleanField(default=False)
#     other_location_travel_detail = models.TextField(null=True, blank=True)
#     reserved_occupation_position = models.BooleanField(default=False)
#     advertised_position = models.BooleanField(default=False)
#     advertised_detail = models.TextField(null=True, blank=True)
#     dependent_accompany = models.BooleanField(default=False)
#     dependent_accompany_count =models.IntegerField(null=True, blank=True)
#     png_current_workpermit_holder = models.BooleanField(default=False)
#     workpermit_number =models.IntegerField(null=True, blank=True)
#     training_institution_1 = models.CharField(max_length=200,null=True, blank=True)
#     from_duration_1 = models.DateField(null=True, blank=True)
#     to_duration_1 = models.DateField(null=True, blank=True)
#     field_study_1 = models.CharField(max_length=200,null=True, blank=True)
#     training_institution_2 = models.CharField(max_length=200,null=True, blank=True)
#     from_duration_2 = models.DateField(null=True, blank=True)
#     to_duration_2 = models.DateField(null=True, blank=True)
#     field_study_2 = models.CharField(max_length=200,null=True, blank=True)
#     employer_location_1 = models.CharField(max_length=200,null=True, blank=True)
#     industry_1 = models.CharField(max_length=200,null=True, blank=True)
#     employment_from_duration_1 = models.DateField(null=True, blank=True)
#     employment_to_duration_1 = models.DateField(null=True, blank=True)
#     occupation_1 = models.CharField(max_length=200,null=True, blank=True)
#     employer_location_2 = models.CharField(max_length=200,null=True, blank=True)
#     industry_2 = models.CharField(max_length=200,null=True, blank=True)
#     employment_from_duration_2 = models.DateField(null=True, blank=True)
#     employment_to_duration_2 = models.DateField(null=True, blank=True)
#     occupation_2 = models.CharField(max_length=200,null=True, blank=True)
#     origin_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True,related_name = "emp_country")
#     origin_city = models.CharField(max_length=50,null=True, blank=True)
#     english_speaking_country = models.BooleanField(default=False)
#     passed_english_proficiency = models.BooleanField(default=False)
#     english_proficiency_institution = models.CharField(max_length=200,null=True, blank=True)
#     test_undertaken = models.DateField(null=True, blank=True)
#     results = models.CharField(max_length=200,null=True, blank=True)
#     alternative_proof = models.CharField(max_length=200,null=True, blank=True)
#     take_home_salary =models.IntegerField(null=True, blank=True)
#     non_salary_allowance =models.IntegerField(null=True, blank=True)
#     total_salary_package =models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = "work_permit_application"

# class VisaImage(BaseModel):
#     document_reference_name  = models.CharField(max_length=50, null=True, blank=True)
#     employee                 = models.ForeignKey(EmployeeInfo, on_delete = models.CASCADE, related_name = "visa_image_employee")
#     file_name                = models.CharField(max_length=100, null=True, blank=True)
#     file_path                = models.CharField(max_length=100, null=True, blank=True)
#     file_format              = models.CharField(max_length=20, null=True, blank=True)
#     document_type            = models.CharField(max_length=20, null=True, blank=True)
#     reason                   = models.TextField(null=True, blank=True)
#     class Meta:
#         db_table = "visa_image"

# class VisaDocumentRemark(BaseModel):
#     employee                 = models.ForeignKey(EmployeeInfo, on_delete = models.CASCADE, related_name = "visa_document_employee")
#     remarks                  = models.JSONField(null=True, blank=True)
#     class Meta:
#         db_table = "visa_document_remark"
