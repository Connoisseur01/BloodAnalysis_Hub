from blood_analysis_hub import db, create_app
from blood_analysis_hub.models import Attribute
app = create_app()
app.app_context().push()

attribute = Attribute(name='Hemoglobin (Hb)', unit='g/L', min_male=2.09, max_male=2.71, min_female=1.86, max_female=2.48,
                      desc_over='High Hb levels (polycythemia) could indicate dehydration, lung disease, or a bone marrow disorder',
                      desc_under='Low levels (anemia) may suggest conditions like iron deficiency, chronic diseases, blood loss, or bone marrow problems')
db.session.add(attribute)
attribute = Attribute(name='Hematocrit (Hct)', unit='%', min_male=41, max_male=53, min_female=36, max_female=46,
                      desc_over='Elevated levels could signify dehydration, lung disease, or polycythemia',
                      desc_under='Low levels might indicate anemia, overhydration, blood loss, or conditions affecting red blood cell production')
db.session.add(attribute)
attribute = Attribute(name='Red Blood Cell Count (RBC)', unit='cells/L', min_male=4.3, max_male=5.9, min_female=3.5, max_female=5.5,
                      desc_over='Elevated RBC count could be due to dehydration, lung disease, or bone marrow disorders',
                      desc_under='Low RBC count could indicate anemia, bleeding, or bone marrow problems affecting RBC production')
db.session.add(attribute)
attribute = Attribute(name='Mean Corpuscular Volume (MCV)', unit='fL', min_male=80, max_male=100, min_female=80, max_female=100,
                      desc_over='High MCV could indicate vitamin deficiencies, liver disease, or certain types of anemia',
                      desc_under='Low MCV might suggest iron deficiency anemia or other conditions affecting red blood cell size')
db.session.add(attribute)
attribute = Attribute(name='Mean Corpuscular Hemoglobin (mch)', unit='pg', min_male=0.39, max_male=0.54, min_female=0.39, max_female=0.54,
                      desc_over='High MCH could indicate certain types of anemia or conditions affecting hemoglobin levels',
                      desc_under='Low MCH might suggest iron deficiency anemia or other types of anemia')
db.session.add(attribute)
attribute = Attribute(name='Mean Corpuscular Hemoglobin Concentration (MCHC)', unit='g/L', min_male=0.54, max_male=4.52, min_female=0.54, max_female=4.52,
                      desc_over='High MCHC levels might indicate conditions like spherocytosis or other disorders affecting hemoglobin concentration',
                      desc_under='Low MCHC might suggest conditions like iron deficiency anemia or thalassemia')
db.session.add(attribute)
attribute = Attribute(name='White Blood Cell Count (WBC)', unit='cells/L', min_male=4.5, max_male=11.0, min_female=4.5, max_female=11.0,
                      desc_over='Elevated WBC count might suggest infection, inflammation, leukemia, or stress',
                      desc_under='Low WBC count could indicate autoimmune disorders, bone marrow problems, or certain medications affecting WBC production')
db.session.add(attribute)
attribute = Attribute(name='Platelet Count', unit='cells/L', min_male=150, max_male=400, min_female=150, max_female=400,
                      desc_over='High platelet counts might indicate certain infections, inflammation, or bone marrow disorders',
                      desc_under='Low platelet counts might suggest bleeding disorders, autoimmune diseases, or liver problems')
db.session.add(attribute)
db.session.commit()