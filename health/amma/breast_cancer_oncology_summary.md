# Breast Cancer Oncology Record Summary

Prepared from Kaiser Permanente IHE/XDM XML records exported 2026-09-17. This is a record abstraction for oncology review, not a treatment recommendation.

## Patient Context

- Female, born 1940-04-21.
- Major comorbidities in chart: type 2 diabetes with hyperlipidemia, uncontrolled hypertension, fall risk/frailty, chemotherapy-induced peripheral neuropathy.
- Functional status noted in oncology visits as ECOG 2 in 2024 and ECOG 3 by late 2025/2026.
- Allergy/intolerance: metformin listed as diarrhea.

## Cancer Diagnosis and Staging

- Primary diagnosis: right central breast invasive carcinoma with micropapillary features, grade 3, ER positive, PR positive, HER2 positive.
- Initial imaging, 2023-04-28: diagnostic mammogram/ultrasound showed a diffusely infiltrating right breast mass measuring 8.3 x 6.3 cm with skin thickening/lymphedema and shrunken right breast; enlarged right axillary tail lymph node 1.9 x 1.3 x 0.8 cm. Left breast had an indeterminate 4:00 mass measuring 2.0 x 0.9 x 1.3 cm, biopsy recommended.
- Left breast biopsy, 2023-05-18: left breast 4:00, 5 cm from nipple, sclerotic fibroadenoma; no malignancy.
- Biopsy, 2023-05-18:
  - Right breast retroareolar 9:00: invasive carcinoma with micropapillary features, grade 3, Nottingham 8, maximum tumor dimension in sampled material 1.4 cm.
  - Right axillary tail: extensive invasive carcinoma with micropapillary features, grade 3; comment said this may represent a lymph node with extensive metastatic carcinoma.
  - Receptors:
    - Breast site: ER 100% strong, PR 40%, HER2 IHC 3+, Ki-67 30%.
    - Axillary site: ER 100% strong, PR 50%, HER2 IHC 3+, Ki-67 40%.
- Initial multidisciplinary clinic, 2023-05-31: assessed as HER2-positive breast cancer with dermal involvement, T4N1, clinical stage IIIB. Plan was PET to rule out distant disease, port, baseline echo, and neoadjuvant chemotherapy.
- Oncology visit, 2023-06-19: PET described as suggestive of metastatic disease with mediastinal and contralateral axillary lymph nodes. Metastatic disease was not biopsy-confirmed in the note. Treatment changed from TCH to TCHP, with low threshold to drop carboplatin if poorly tolerated.
- Left axillary lymph node biopsy, 2023-07-31: benign lymph node, negative for malignancy.
- Oncology staging entry, 2023-09-27: clinical Stage IV, cM1.
- Germline genetics, 2023-06-21: Invitae Breast and Gyn Cancers Panel, 21 genes, no pathogenic mutations, gross deletions/duplications, or variants of uncertain significance identified.
- Family history recorded in breast clinic intake: sister with breast cancer diagnosed around age 50, deceased in her 50s; no Ashkenazi Jewish heritage reported.

## Treatment Timeline

| Date/period | Treatment or decision | Details from records |
| --- | --- | --- |
| 2023-05-31 | Initial treatment plan | TCH q21 days x 6 cycles planned; goal documented as curative/neoadjuvant before PET clarification. |
| 2023-06-15 | Port placement | Left internal jugular Bard PowerPort placed. Meds included Ancef 1 g IV, Versed 2 mg IV, fentanyl 100 mcg IV. |
| 2023-06-21 | Cycle 1 TCHP | Carboplatin 289.6 mg IV, target AUC 4; docetaxel 102.6 mg IV, 60 mg/m2; pertuzumab 840 mg IV loading dose; trastuzumab-anns 526.47 mg IV, 8 mg/kg loading dose. Premeds included ondansetron 16 mg PO and olanzapine 5 mg PO. Home meds included dexamethasone 8 mg BID for 5 doses around docetaxel, filgrastim-aafi 300 mcg SC daily days 3-7, ondansetron/prochlorperazine/loperamide PRN. |
| 2023-06-24 to 2023-06-29 | Post-cycle-1 acute care/hospitalization | Seen for nausea/vomiting after chemotherapy, then admitted 2023-06-28 to 2023-06-29 for intractable nausea/vomiting, hypertensive urgency, and presumed inflammatory vs infectious colitis. Managed with IV fluids, scheduled ondansetron, PRN prochlorperazine, BP medications, antibiotics; oncology was informed. |
| 2023-07-12 | Cycle 2 TCHP | Docetaxel 102.6 mg IV, 60 mg/m2; pertuzumab 420 mg IV; trastuzumab-anns 394.8 mg IV, 6 mg/kg. Carboplatin is not shown in the extracted administered-medication block for this visit. |
| 2023-08-02 | Cycle 3 THP | Doses adjusted for 10.6% weight loss. Docetaxel reduced to 79.5 mg IV, 50 mg/m2; pertuzumab 420 mg IV; trastuzumab-anns 352.8 mg IV, 6 mg/kg. Hypertension during infusion required clonidine 0.1 mg PO. |
| 2023-08-23 | Cycle 4 HP only | Docetaxel was held due to increased neuropathy and bilateral lower-extremity edema; continued pertuzumab 420 mg IV and trastuzumab-anns 352.8 mg IV. Short course furosemide 20 mg daily x 3 days ordered. |
| 2023-09-13 | Cycle 5 THP | Docetaxel 79.5 mg IV, 50 mg/m2; pertuzumab 420 mg IV; trastuzumab-anns 352.8 mg IV, 6 mg/kg. Carboplatin not shown in the extracted administered-medication snippet. |
| 2023-09-27 | Response and treatment change | Oncologist documented "good response to treatment." Because cancer was stage IV, surgery/radiation were not expected to benefit; recommendation was palliative systemic therapy with trastuzumab/pertuzumab without chemotherapy, start anastrozole daily 2023-10-04, PET again in 4-5 months, bone density scan, calcium/vitamin D. |
| 2023-10-04 through 2024-10-25 | HER2 maintenance | Pertuzumab 420 mg IV q3 weeks plus trastuzumab-anns 352.8 mg IV, 6 mg/kg, generally over 30 minutes. |
| 2024-11-14 | HER2 regimen de-escalation | Due to side effects, pertuzumab was dropped; plan was to continue trastuzumab and anastrozole. |
| 2024-11-16 through 2025-02-15 | Trastuzumab alone | Trastuzumab-anns 352.8 mg IV q3 weeks documented. |
| 2025-03-10 | Enhertu started | Fam-trastuzumab deruxtecan-nxki 341.2 mg IV, 5.4 mg/kg, over 90 minutes. Premeds: dexamethasone 12 mg PO, ondansetron 16 mg PO, olanzapine 5 mg PO. Treatment goal in oncology history: palliative after first line. |
| 2025-05-16 to 2025-08-09 | Enhertu dose reduced | Enhertu 278 mg IV, 4.4 mg/kg, over 30 minutes. Same premed pattern. |
| 2025-08-29 | Further dose reduction planned | Oncologist: continue Enhertu, reduce dose slightly again; PET as scheduled. Noted that other options exist but have toxicity; anastrozole alone could be tried with progression or if Enhertu not tolerated. |
| 2025-10-03, 2025-10-24, 2025-12-11 | Further reduced Enhertu | Enhertu 200 mg IV, 3.2 mg/kg, over 30 minutes. Same premed pattern. Last documented Enhertu dose in records: 2025-12-11. |
| 2026-01-20 | Patient considering stopping IV therapy | Son reported patient did not want next chemo because of fatigue lasting most of the cycle despite dose reduction. Oncologist advised she could resume anastrozole and keep March appointment; infusion appointments were canceled. |
| 2026-03-04 | Current accepted therapy at that time | Oncology note: patient decided to suspend IV therapy/therapy causing significant side effects. She was on anastrozole and accepting only that. Continue anastrozole if tolerating; PET again in early June; labs then follow-up. |
| 2026-06-08 PET | Disease status | PET/CT impression: slight interval increase in size and metabolic activity of right breast lesions; no signs of distant metastasis. |
| 2026-09-10 | Most recent oncology plan | Oncologist documented right breast progression, not unexpected without therapy. Plan: repeat PET. If disease only in breast, refer to radiation oncology for local control; if visible outside breast, plan to resume Enhertu. Follow-up in 3 months. |

## Current / Recent Medications Relevant to Oncology

- Anastrozole (Arimidex) 1 mg PO daily: active on medication list as of 2026-09-17, last filled/start shown 2026-08-24 to 2027-08-24.
- Chart discrepancy: 2026-03-04 oncology note says she was taking anastrozole as the only accepted therapy. The 2026-09-10 oncology note states she "was on anastrozole but stopped this as well due to ineffective therapy," while the medication list still shows anastrozole active. This should be reconciled directly with patient/family and pharmacy fill history.
- Pregabalin 50 mg PO twice daily for neuropathy.
- Famotidine 40 mg PO bedtime for reflux.
- Other active chronic meds include telmisartan, bisoprolol, glipizide, metformin XR, atorvastatin, acetaminophen PRN, topical agents.

## Imaging / Response Highlights

- 2023-06 PET: described in oncology note as concerning for metastatic disease involving mediastinal and contralateral axillary lymph nodes; biopsy confirmation was not documented in the note.
- 2023-09 oncology note: documented good response to treatment and decision to avoid surgery/radiation because of stage IV disease, continuing palliative systemic HER2-directed therapy.
- 2026-06-08 PET/CT: slight interval increase in size/metabolic activity of right breast lesions; no distant metastasis.
- 2026-09-10: clinical concern for progression in right breast. Repeat PET scheduled for 2026-09-24 per future appointments in chart.

## Toxicities / Treatment-Limiting Issues

- Peripheral neuropathy in hands/feet after chemotherapy; treated with pregabalin. Neuropathy persisted but was variably described as improving or residual.
- Early TCHP toxicity included nausea/vomiting requiring acute care and short hospitalization after cycle 1; later docetaxel was held once for worsening neuropathy and edema.
- Fatigue was a major limiting toxicity on Enhertu; by 2026-01 patient/family reported she remained in bed after infusion and did not recover until near next cycle despite dose reductions.
- Hypertension often elevated in visits.
- Frailty/fall risk and mobility limitations; uses walker/wheelchair at some visits.
- Diabetes control suboptimal in multiple labs/notes.

## Key Questions for Next Oncologist

1. Reconcile current therapy: is she actually taking anastrozole 1 mg daily, or was it stopped despite being active in the medication list?
2. Review 2026-09-24 PET results when available: is disease confined to right breast/local-regional sites, or is distant disease again visible?
3. If PET shows only local progression, discuss goals and expected benefit/risks of breast/chest wall radiation for local control, including skin breakdown prevention, pain/bleeding prevention, and toxicity.
4. If distant progression is present, discuss whether resuming Enhertu is acceptable given prior severe fatigue, and whether alternative lower-toxicity HER2+/ER+ metastatic options fit her goals and frailty.
5. Clarify whether prior stage IV status was biopsy-confirmed or based on PET only; this may matter if current PET remains local-only.
6. Revisit goals of care: patient has repeatedly expressed concern about side effects and willingness to avoid IV therapy; treatment decisions should explicitly balance disease control, local symptoms, independence, fatigue, neuropathy, and quality of life.

## Source Documents Reviewed Most Closely

- DOC0131.XML: 2023-05-18 biopsy/pathology.
- DOC0128.XML: 2023-05-19 notification and breast cancer clinic intake.
- DOC0125.XML: 2023-05-31 multidisciplinary clinic, initial plan.
- DOC0117.XML: 2023-06-19 oncology plan after PET concern for metastatic disease.
- DOC0116.XML, DOC0108.XML, DOC0103.XML, DOC0100.XML: early infusion chemotherapy administrations.
- DOC0099.XML: 2023-09-27 response and switch to palliative HER2 therapy/anastrozole.
- DOC0055.XML: 2024-11-14 pertuzumab stopped, trastuzumab/anastrozole continued.
- DOC0041.XML, DOC0033.XML, DOC0029.XML, DOC0028.XML, DOC0022.XML, DOC0020.XML, DOC0016.XML: Enhertu administrations and dose reductions.
- DOC0012.XML, DOC0010.XML, DOC0003.XML: treatment pause, anastrozole-only phase, and latest plan.
- DOC0001.XML/DOC0002.XML: exported health summary/result blocks including 2026-06 PET.
